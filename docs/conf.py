"""Configuration file for the Sphinx documentation builder.

This file only contains a selection of the most common options. For a full
list see the documentation:
https://www.sphinx-doc.org/en/master/usage/configuration.html
"""

import dataclasses
import os
from typing import Union

import nbformat  # pyright: reportMissingImports=false
import sphinxcontrib.bibtex.plugin
from pybtex.database import Entry
from pybtex.plugin import register_plugin
from pybtex.richtext import BaseText, Tag, Text
from pybtex.style.formatting.unsrt import Style as UnsrtStyle
from pybtex.style.template import (
    FieldIsMissing,
    Node,
    _format_list,
    field,
    href,
    join,
    node,
    sentence,
    words,
)
from sphinxcontrib.bibtex.style.referencing import BracketStyle
from sphinxcontrib.bibtex.style.referencing.author_year import (
    AuthorYearReferenceStyle,
)

# -- Project information -----------------------------------------------------
project = "ComPWA Organization"
repo_name = "compwa-org"
copyright = "2021, ComPWA"  # noqa: A001
author = "Common Partial Wave Analysis"


# -- General configuration ---------------------------------------------------
master_doc = "index.md"
source_suffix = {
    ".ipynb": "myst-nb",
    ".md": "myst-nb",
}

# The master toctree document.
master_doc = "index"

extensions = [
    "myst_nb",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosectionlabel",
    "sphinx.ext.intersphinx",
    "sphinx.ext.mathjax",
    "sphinx.ext.napoleon",
    "sphinx_copybutton",
    "sphinx_math_dollar",
    "sphinx_panels",
    "sphinx_thebe",
    "sphinx_togglebutton",
    "sphinxcontrib.bibtex",
    "sphinxcontrib.hep.pdgref",
]
exclude_patterns = [
    "**.ipynb_checkpoints",
    "*build",
    "*template.md",
    "adr/template.md",
    "tests",
]

# General sphinx settings
add_module_names = False
autodoc_default_options = {
    "members": True,
    "undoc-members": True,
    "show-inheritance": True,
    "special-members": ", ".join(
        [
            "__call__",
            "__eq__",
        ]
    ),
}
graphviz_output_format = "svg"
html_copy_source = True  # needed for download notebook button
html_css_files = ["custom.css"]
html_favicon = "_static/favicon.ico"
html_show_copyright = False
html_show_sourcelink = False
html_show_sphinx = False
html_sourcelink_suffix = ""
html_static_path = ["_static"]
html_theme = "sphinx_book_theme"
html_theme_options = {
    "repository_url": f"https://github.com/ComPWA/{repo_name}",
    "repository_branch": "stable",
    "path_to_docs": "docs",
    "use_download_button": True,
    "use_edit_page_button": True,
    "use_issues_button": True,
    "use_repository_button": True,
    "launch_buttons": {
        "binderhub_url": "https://mybinder.org",
        "colab_url": "https://colab.research.google.com",
        "notebook_interface": "jupyterlab",
        "thebe": True,
        "thebelab": True,
    },
    "theme_dev_mode": True,
}
html_title = "Common Partial Wave Analysis"
pygments_style = "sphinx"
todo_include_todos = False
viewcode_follow_imported_members = True

# Cross-referencing configuration
default_role = "py:obj"
primary_domain = "py"
nitpicky = True  # warn if cross-references are missing

# Intersphinx settings
intersphinx_mapping = {
    "ampform": ("https://ampform.readthedocs.io/en/stable", None),
    "ComPWA": ("https://compwa.readthedocs.io/en/latest", None),
    "expertsystem": ("https://expertsystem.readthedocs.io/en/stable", None),
    "jax": ("https://jax.readthedocs.io/en/latest", None),
    "ipywidgets": ("https://ipywidgets.readthedocs.io/en/stable", None),
    "matplotlib": ("https://matplotlib.org/stable", None),
    "numpy": ("https://numpy.org/doc/stable", None),
    "pwa": ("https://pwa.readthedocs.io", None),
    "pycompwa": ("https://compwa.github.io", None),
    "python": ("https://docs.python.org/3", None),
    "qrules": ("https://qrules.readthedocs.io/en/stable", None),
    "scipy": ("https://docs.scipy.org/doc/scipy", None),
    "sympy": ("https://docs.sympy.org/latest", None),
    "tensorwaves": ("https://tensorwaves.readthedocs.io/en/stable", None),
}

# Settings for autosectionlabel
autosectionlabel_prefix_document = True

# Settings for bibtex
bibtex_bibfiles = ["bibliography.bib"]
suppress_warnings = [
    "myst.domains",
]
bibtex_reference_style = "author_year_no_comma"

# Settings for copybutton
copybutton_prompt_is_regexp = True
copybutton_prompt_text = r">>> |\.\.\. "  # doctest

# Settings for linkcheck
linkcheck_anchors = False
linkcheck_ignore = [
    "http://127.0.0.1:8000",
]

# Settings for myst_nb
execution_timeout = -1
execution_excludepatterns = [
    "adr/001/*",
    "adr/002/*",
    "report/000*",
    "report/001*",
    "report/002*",
    "report/003*",
    "report/006*",
]
nb_output_stderr = "remove"
nb_render_priority = {
    "html": (
        "application/vnd.jupyter.widget-view+json",
        "application/javascript",
        "text/html",
        "image/svg+xml",
        "image/png",
        "image/jpeg",
        "text/markdown",
        "text/latex",
        "text/plain",
    )
}

jupyter_execute_notebooks = "off"
if "EXECUTE_NB" in os.environ:
    print("\033[93;1mWill run Jupyter notebooks!\033[0m")
    jupyter_execute_notebooks = "force"

# Settings for myst-parser
myst_enable_extensions = [
    "amsmath",
    "colon_fence",
    "dollarmath",
    "smartquotes",
    "substitution",
]
BINDER_LINK = (
    f"https://mybinder.org/v2/gh/ComPWA/{repo_name}/stable?filepath=docs"
)
myst_substitutions = {
    "run_interactive": f"""
```{{margin}}
Run this notebook [on Binder]({BINDER_LINK}) or
{{ref}}`locally on Jupyter Lab <pwa:develop:Jupyter Notebooks>` to
interactively modify the parameters.
```
"""
}
myst_update_mathjax = False

# Settings for Thebe cell output
thebe_config = {
    "repository_url": html_theme_options["repository_url"],
    "repository_branch": html_theme_options["repository_branch"],
}

with open("demo.template.md") as stream:
    demo_template = stream.read()


# Embed links to demos on Binder
demo_template += "\n"
demo_template += "```{toctree}\n"
for root, _, files in os.walk("../demo"):
    if ".ipynb_checkpoints" in root:
        continue
    for filename in sorted(files):
        if not filename.endswith(".ipynb"):
            continue
        filepath = os.path.join(root, filename)
        notebook = nbformat.read(filepath, as_version=nbformat.NO_CONVERT)
        notebook_title = ""
        app_mode = False
        for cell in notebook.cells:
            if not cell.cell_type == "markdown":
                continue
            if not app_mode and (
                "<!-- appmode -->" in cell.source
                or "<!-- app-mode -->" in cell.source
            ):
                app_mode = True
            if not cell.source.startswith("# "):
                continue
            notebook_title = cell.source
            notebook_title = notebook_title[1:]
            notebook_title = notebook_title.strip()
            break
        if not notebook_title:
            raise ValueError(f'Notebook "{filepath}" does not have a title')
        link = "https://mybinder.org/v2/gh/ComPWA/compwa-org/stable"
        if app_mode:
            link += f"?urlpath=apps%2Fdemo%2F{filename}"
        else:
            link += f"?filepath=demo%2F{filename}"
        demo_template += f"{notebook_title} <{link}>\n"
demo_template += "```\n"


with open("demo.md", "w") as stream:
    stream.write(demo_template)


# Specify bibliography style

no_brackets = BracketStyle(
    left="",
    right="",
)


@dataclasses.dataclass
class NoCommaReferenceStyle(AuthorYearReferenceStyle):
    author_year_sep: Union["BaseText", str] = " "
    bracket_parenthetical: BracketStyle = no_brackets


sphinxcontrib.bibtex.plugin.register_plugin(
    "sphinxcontrib.bibtex.style.referencing",
    "author_year_no_comma",
    NoCommaReferenceStyle,
)


@node
def et_al(children, data, sep="", sep2=None, last_sep=None):
    if sep2 is None:
        sep2 = sep
    if last_sep is None:
        last_sep = sep
    parts = [part for part in _format_list(children, data) if part]
    if len(parts) <= 1:
        return Text(*parts)
    elif len(parts) == 2:
        return Text(sep2).join(parts)
    elif len(parts) == 3:
        return Text(last_sep).join([Text(sep).join(parts[:-1]), parts[-1]])
    else:
        return Text(parts[0], Tag("em", " et al"))


@node
def names(children, context, role, **kwargs):
    """Return formatted names."""
    assert not children
    try:
        persons = context["entry"].persons[role]
    except KeyError:
        raise FieldIsMissing(role, context["entry"])

    style = context["style"]
    formatted_names = [
        style.format_name(person, style.abbreviate_names) for person in persons
    ]
    return et_al(**kwargs)[formatted_names].format_data(context)


class MyStyle(UnsrtStyle):
    def __init__(self):
        super().__init__(abbreviate_names=True)

    def format_names(self, role, as_sentence=True) -> Node:
        formatted_names = names(
            role, sep=", ", sep2=" and ", last_sep=", and "
        )
        if as_sentence:
            return sentence[formatted_names]
        else:
            return formatted_names

    def format_eprint(self, e):
        if "doi" in e.fields:
            return ""
        return super().format_eprint(e)

    def format_url(self, e: Entry) -> Node:
        if "doi" in e.fields or "eprint" in e.fields:
            return ""
        return words[
            href[
                field("url", raw=True),
                field("url", raw=True, apply_func=remove_http),
            ]
        ]

    def format_isbn(self, e: Entry) -> Node:
        return href[
            join[
                "https://isbnsearch.org/isbn/",
                field("isbn", raw=True, apply_func=remove_dashes_and_spaces),
            ],
            join[
                "ISBN:",
                field("isbn", raw=True),
            ],
        ]


def remove_dashes_and_spaces(isbn: str) -> str:
    to_remove = ["-", " "]
    for remove in to_remove:
        isbn = isbn.replace(remove, "")
    return isbn


def remove_http(input_str: str) -> str:
    to_remove = ["https://", "http://"]
    for remove in to_remove:
        input_str = input_str.replace(remove, "")
    return input_str


register_plugin("pybtex.style.formatting", "unsrt_et_al", MyStyle)
