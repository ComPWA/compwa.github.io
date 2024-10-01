"""Enforce adding a pip install statement in the notebook.

In the `compwa.github.io repo <https://github.com/ComPWA/compwa.github.io>`_, notebooks
should specify which package versions should be used to run the notebook. This hook
checks whether a notebook has such install statements and whether they comply with the
expected formatting.
"""
# cspell:ignore oneline precommit

from __future__ import annotations

import argparse
import re
import sys
from functools import lru_cache
from textwrap import dedent
from typing import TYPE_CHECKING, Callable, TypeVar

import attr
import nbformat
from nbformat import NotebookNode

if TYPE_CHECKING:
    from collections.abc import Sequence

if sys.version_info >= (3, 10):
    from typing import ParamSpec
else:
    from typing_extensions import ParamSpec

__EXPECTED_PIP_INSTALL_LINE = "%pip install -q"


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(__doc__)
    parser.add_argument("filenames", nargs="*", help="Filenames to check.")
    args = parser.parse_args(argv)

    errors: list[PrecommitError] = []
    for filename in args.filenames:
        try:
            check_pinned_requirements(filename)
        except PrecommitError as exception:  # noqa: PERF203
            errors.append(exception)
    if errors:
        for error in errors:
            error_msg = "\n ".join(error.args)
            print(error_msg)  # noqa: T201
        return 1
    return 0


def check_pinned_requirements(filename: str) -> None:
    notebook = load_notebook(filename)
    if not __has_python_kernel(notebook):
        return
    for cell_id, cell in enumerate(notebook["cells"]):
        if cell["cell_type"] != "code":
            continue
        source = __to_oneline(cell["source"])
        pip_requirements = extract_pip_requirements(source)
        if pip_requirements is None:
            continue
        executor = Executor()
        executor(_check_pip_requirements, filename, pip_requirements)
        executor(_format_pip_requirements, filename, source, notebook, cell_id)
        executor(_update_metadata, filename, cell["metadata"], notebook)
        executor.finalize()
        return
    msg = (
        f'Notebook "{filename}" does not contain a pip install cell of the form'
        f" {__EXPECTED_PIP_INSTALL_LINE} some-package==0.1.0 package2==3.2"
    )
    raise PrecommitError(msg)


def __has_python_kernel(notebook: dict) -> bool:
    # cspell:ignore kernelspec
    metadata = notebook.get("metadata", {})
    kernel_specification = metadata.get("kernelspec", {})
    kernel_language = kernel_specification.get("language", "")
    return "python" in kernel_language


@lru_cache(maxsize=1)
def __to_oneline(source: str) -> str:
    src_lines = source.split("\n")
    return "".join(s.rstrip().rstrip("\\") for s in src_lines)


@lru_cache(maxsize=1)
def extract_pip_requirements(source: str) -> list[str] | None:
    r"""Check if the source in a cell is a pip install statement.

    >>> extract_pip_requirements("Not a pip install statement")
    >>> extract_pip_requirements("pip install")
    []
    >>> extract_pip_requirements("pip3 install attrs")
    ['attrs']
    >>> extract_pip_requirements("pip3 install -q attrs")
    ['attrs']
    >>> extract_pip_requirements("pip3 install  attrs &> /dev/null")
    ['attrs']
    >>> extract_pip_requirements("%pip install attrs  numpy==1.24.4 ")
    ['attrs', 'numpy==1.24.4']
    >>> extract_pip_requirements("!python3 -mpip install sympy")
    ['sympy']
    >>> extract_pip_requirements('''
    ...     python3 -m pip install \
    ...         attrs  numpy \
    ...         sympy \
    ...         tensorflow
    ... ''')
    ['attrs', 'numpy', 'sympy', 'tensorflow']
    """
    # cspell:ignore mpip
    matches = re.match(
        r"[%\!]?\s*(python3?\s+-m\s*)?pip3?\s+install\s*(-q)?(.*?)(&?>\s*/dev/null)?$",
        __to_oneline(source).strip(),
    )
    if matches is None:
        return None
    packages = matches.group(3).split(" ")
    packages = [p.strip() for p in packages]
    return [p for p in packages if p]


def _check_pip_requirements(filename: str, requirements: list[str]) -> None:
    if len(requirements) == 0:
        msg = f'At least one dependency required in install cell of "{filename}"'
        raise PrecommitError(msg)
    for req in requirements:
        req = req.strip()
        if not req:
            continue
        if "git+" in req:
            continue
        unpinned_requirements = []
        for req in requirements:
            if req.startswith("git+"):
                continue
            if any(equal_sign in req for equal_sign in ["==", "~="]):
                continue
            package = req.split("<")[0].split(">")[0].strip()
            unpinned_requirements.append(package)
        if unpinned_requirements:
            msg = (
                f'Install cell in notebook "{filename}" contains requirements without'
                "pinning (== or ~=):"
            )
            for req in unpinned_requirements:
                msg += f"\n   - {req}"
            msg_unformatted = f"""
            Get the currently installed versions with:

                python3 -m pip freeze | grep -iE '{"|".join(sorted(unpinned_requirements))}'
            """
            msg += dedent(msg_unformatted)
            raise PrecommitError(msg)


def _format_pip_requirements(
    filename: str, install_statement: str, notebook: NotebookNode, cell_id: int
) -> None:
    requirements = extract_pip_requirements(install_statement)
    if requirements is None:
        return
    git_requirements = {r for r in requirements if r.startswith("git+")}
    pip_requirements = set(requirements) - git_requirements
    pip_requirements = {r.lower().replace("_", "-") for r in pip_requirements}
    sorted_requirements = sorted(pip_requirements) + sorted(git_requirements)
    expected = f"{__EXPECTED_PIP_INSTALL_LINE} {' '.join(sorted_requirements)}"
    if install_statement != expected:
        notebook["cells"][cell_id]["source"] = expected
        nbformat.write(notebook, filename)
        msg = f'Ordered and formatted pip install cell in "{filename}"'
        raise PrecommitError(msg)


def _update_metadata(filename: str, metadata: dict, notebook: NotebookNode) -> None:
    updated_metadata = False
    jupyter_metadata = metadata.get("jupyter")
    if jupyter_metadata is not None and jupyter_metadata.get("source_hidden"):
        if len(jupyter_metadata) == 1:
            metadata.pop("jupyter")
        else:
            jupyter_metadata.pop("source_hidden")
        updated_metadata = True
    tags = set(metadata.get("tags", []))
    expected_tags = {"remove-cell"}
    if expected_tags != tags:
        metadata["tags"] = sorted(expected_tags)
        updated_metadata = True
    if updated_metadata:
        nbformat.write(notebook, filename)
        msg = f'Updated metadata of pip install cell in notebook "{filename}"'
        raise PrecommitError(msg)


def load_notebook(path: str) -> NotebookNode:
    return nbformat.read(path, as_version=nbformat.NO_CONVERT)


T = TypeVar("T")
P = ParamSpec("P")


@attr.s(on_setattr=attr.setters.frozen)
class Executor:
    # https://github.com/ComPWA/policy/blob/359331f/src/compwa_policy/utilities/executor.py
    error_messages: list[str] = attr.ib(factory=list, init=False)

    def __call__(
        self, function: Callable[P, T], *args: P.args, **kwargs: P.kwargs
    ) -> T | None:
        """Execute a function and collect any `.PrecommitError` exceptions."""
        try:
            result = function(*args, **kwargs)
        except PrecommitError as exception:
            error_message = str("\n".join(exception.args))
            self.error_messages.append(error_message)
            return None
        else:
            return result

    def finalize(self, exception: bool = True) -> int:
        error_msg = self.merge_messages()
        if error_msg:
            if exception:
                raise PrecommitError(error_msg)
            print(error_msg)  # noqa: T201
            return 1
        return 0

    def merge_messages(self) -> str:
        stripped_messages = (s.strip() for s in self.error_messages)
        return "\n--------------------\n".join(stripped_messages)


class PrecommitError(RuntimeError): ...


if __name__ == "__main__":
    raise SystemExit(main())
