"""Configuration file for the Sphinx documentation builder.

This file only contains a selection of the most common options. For a full
list see the documentation:
https://www.sphinx-doc.org/en/master/usage/configuration.html
"""

import os

import nbformat  # pyright: reportMissingImports=false

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
    "numpy": ("https://numpy.org/doc/stable", None),
    "pycompwa": ("https://compwa.github.io", None),
    "python": ("https://docs.python.org/3", None),
    "qrules": ("https://qrules.readthedocs.io/en/stable", None),
    "sympy": ("https://docs.sympy.org/latest", None),
    "tensorwaves": ("https://tensorwaves.readthedocs.io/en/stable", None),
}

# Settings for autosectionlabel
autosectionlabel_prefix_document = True

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
]
myst_update_mathjax = False

# Settings for Thebe cell output
thebe_config = {
    "repository_url": html_theme_options["repository_url"],
    "repository_branch": html_theme_options["repository_branch"],
}

with open("demo.template.md") as stream:
    demo_template = stream.read()

demo_template += "\n"
demo_template += "```{toctree}\n"
for root, _, files in os.walk("../demo"):
    if ".ipynb_checkpoints" in root:
        continue
    for filename in files:
        if not filename.endswith(".ipynb"):
            continue
        filepath = os.path.join(root, filename)
        notebook = nbformat.read(filepath, as_version=nbformat.NO_CONVERT)
        notebook_title = ""
        for cell in notebook.cells:
            if not cell.cell_type == "markdown":
                continue
            if not cell.source.startswith("# "):
                continue
            notebook_title = cell.source
            notebook_title = notebook_title[1:]
            notebook_title = notebook_title.strip()
            break
        if not notebook_title:
            raise ValueError(f'Notebook "{filepath}" does not have a title')
        link = f"https://mybinder.org/v2/gh/ComPWA/compwa-org/stable?urlpath=apps%2Fdemo%2F{filename}"
        demo_template += f"{notebook_title} <{link}>\n"
demo_template += "```\n"


with open("demo.md", "w") as stream:
    stream.write(demo_template)
