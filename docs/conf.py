"""Configuration file for the Sphinx documentation builder.

This file only contains a selection of the most common options. For a full list see the
documentation: https://www.sphinx-doc.org/en/master/usage/configuration.html
"""

from __future__ import annotations

import os
import shutil
import sys

from sphinx_api_relink.helpers import (
    get_branch_name,
    get_execution_mode,
    pin,
    pin_minor,
    set_intersphinx_version_remapping,
)

sys.path.insert(0, os.path.abspath("."))
import _list_technical_reports


def get_nb_exclusion_patterns() -> list[str]:
    exclusions = [
        "adr/001/*",
        "adr/002/*",
        "report/000*",
        "report/001*",
        "report/002*",
        "report/003*",
        "report/005*",
        "report/008*",
        "report/009*",
        "report/01*",
        "report/020*",
        "report/021*",
        "report/022*",
    ]
    julia_notebooks = [
        "report/019*",
    ]
    if "READTHEDOCS" not in os.environ and shutil.which("julia") is None:
        exclusions.extend(julia_notebooks)
    return exclusions


_list_technical_reports.main()
set_intersphinx_version_remapping({
    "ipython": {
        "8.12.2": "8.12.1",
        "8.12.3": "8.12.1",
    },
    "ipywidgets": {
        "8.0.3": "8.0.5",
        "8.0.4": "8.0.5",
        "8.0.6": "8.0.5",
        "8.1.1": "8.1.2",
    },
    "matplotlib": {"3.5.1": "3.5.0"},
    "mpl-interactions": {"0.24.1": "0.24.0"},
})

BRANCH = get_branch_name()
ORGANIZATION = "ComPWA"
REPO_NAME = "compwa-org"
REPO_TITLE = "ComPWA Organization"

BINDER_LINK = (
    f"https://mybinder.org/v2/gh/ComPWA/{REPO_NAME}/{BRANCH}?filepath=docs/usage"
)

add_module_names = False
author = "Common Partial Wave Analysis"
autodoc_default_options = {
    "members": True,
    "undoc-members": True,
    "show-inheritance": True,
    "special-members": ", ".join([
        "__call__",
        "__eq__",
    ]),
}
autosectionlabel_prefix_document = True
bibtex_bibfiles = ["bibliography.bib"]
codeautolink_concat_default = True
codeautolink_global_preface = """
import matplotlib.pyplot as plt
import numpy as np
import sympy as sp
from IPython.display import display
"""
comments_config = {
    "hypothesis": True,
    "utterances": {
        "repo": f"{ORGANIZATION}/{REPO_NAME}",
        "issue-term": "pathname",
        "label": "📝 Docs",
    },
}
copybutton_prompt_is_regexp = True
copybutton_prompt_text = r">>> |\.\.\. "  # doctest
copyright = f"2020, {ORGANIZATION}"
default_role = "py:obj"
exclude_patterns = [
    "**.ipynb_checkpoints",
    "*build",
    "*template.md",
    "adr/template.md",
    "tests",
]
extensions = [
    "myst_nb",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosectionlabel",
    "sphinx.ext.intersphinx",
    "sphinx.ext.mathjax",
    "sphinx.ext.napoleon",
    "sphinx_api_relink",
    "sphinx_codeautolink",
    "sphinx_comments",
    "sphinx_copybutton",
    "sphinx_design",
    "sphinx_hep_pdgref",
    "sphinx_pybtex_etal_style",
    "sphinx_remove_toctrees",
    "sphinx_thebe",
    "sphinx_togglebutton",
    "sphinxcontrib.bibtex",
]
graphviz_output_format = "svg"
html_favicon = "_static/favicon.ico"
html_js_files = [
    "https://cdn.datatables.net/1.13.6/js/jquery.dataTables.min.js",
    "https://cdnjs.cloudflare.com/ajax/libs/require.js/2.3.4/require.min.js",
]
html_last_updated_fmt = "%-d %B %Y"
html_logo = (
    "https://raw.githubusercontent.com/ComPWA/ComPWA/04e5199/doc/images/logo.svg"
)
html_show_copyright = False
html_show_sourcelink = False
html_show_sphinx = False
html_sourcelink_suffix = ""
html_static_path = ["_static"]
html_theme = "sphinx_book_theme"
html_theme_options = {
    "icon_links": [
        {
            "name": "GitHub",
            "url": f"https://github.com/{ORGANIZATION}",
            "icon": "fa-brands fa-github",
        },
        {
            "name": "Zenodo",
            "url": "https://doi.org/10.5281/zenodo.6908149",
            "icon": "https://zenodo.org/badge/DOI/10.5281/zenodo.6908149.svg",
            "type": "url",
        },
    ],
    "logo": {"text": "The ComPWA project"},
    "repository_url": f"https://github.com/{ORGANIZATION}/{REPO_NAME}",
    "repository_branch": BRANCH,
    "path_to_docs": "docs",
    "use_download_button": False,
    "use_edit_page_button": True,
    "use_issues_button": True,
    "use_repository_button": True,
    "use_source_button": True,
    "launch_buttons": {
        "binderhub_url": "https://mybinder.org",
        "colab_url": "https://colab.research.google.com",
        "deepnote_url": "https://deepnote.com",
        "notebook_interface": "jupyterlab",
        "thebe": True,
    },
    "show_toc_level": 2,
}
html_title = "Common Partial Wave Analysis Project"
intersphinx_mapping = {
    "IPython": (f"https://ipython.readthedocs.io/en/{pin('IPython')}", None),
    "ampform": ("https://ampform.readthedocs.io/en/stable", None),
    "attrs": (f"https://www.attrs.org/en/{pin('attrs')}", None),
    "expertsystem": ("https://expertsystem.readthedocs.io/en/stable", None),
    "graphviz": ("https://graphviz.readthedocs.io/en/stable", None),
    "hepstats": ("https://scikit-hep.org/hepstats", None),
    "ipywidgets": (f"https://ipywidgets.readthedocs.io/en/{pin('ipywidgets')}", None),
    "jax": ("https://jax.readthedocs.io/en/latest", None),
    "matplotlib": (f"https://matplotlib.org/{pin('matplotlib')}", None),
    "mpl_interactions": (
        f"https://mpl-interactions.readthedocs.io/en/{pin('mpl-interactions')}",
        None,
    ),
    "numpy": (f"https://numpy.org/doc/{pin_minor('numpy')}", None),
    "plotly": ("https://plotly.com/python-api-reference/", None),
    "pwa": ("https://pwa.readthedocs.io", None),
    "python": ("https://docs.python.org/3", None),
    "qrules": ("https://qrules.readthedocs.io/en/stable", None),
    "qrules-0.9.x": ("https://qrules.readthedocs.io/en/0.9.x", None),
    "scipy": ("https://docs.scipy.org/doc/scipy-1.7.0", None),
    "sympy": ("https://docs.sympy.org/latest", None),
    "tensorwaves": ("https://tensorwaves.readthedocs.io/en/stable", None),
    "zfit": ("https://zfit.readthedocs.io/en/latest", None),
}
linkcheck_anchors = False
linkcheck_ignore = [
    "http://127.0.0.1:8000",
    "https://atom.io",  # often instable
    "https://doi.org/10.1002/andp.19955070504",  # 403 for onlinelibrary.wiley.com
    "https://github.com/organizations/ComPWA/settings/repository-defaults",  # private
    "https://github.com/orgs/ComPWA/projects/5",  # private
    "https://github.com/orgs/ComPWA/projects/6",  # private
    "https://ieeexplore.ieee.org/document/6312940",  # 401
    "https://mybinder.org",  # often instable
    "https://open.vscode.dev",
    "https://rosettacode.org",
    "https://via.placeholder.com",  # irregular timeout
    "https://www.andiamo.co.uk/resources/iso-language-codes",  # 443, but works
    "https://www.bookfinder.com",
]
master_doc = "index"
myst_enable_extensions = [
    "amsmath",
    "colon_fence",
    "dollarmath",
    "smartquotes",
    "substitution",
]
myst_heading_anchors = 4
myst_substitutions = {
    "branch": BRANCH,
    "remark_019": (
        "Notice how a new file [`019/Project.toml`](./019/Project.toml) and "
        " [`019/Manifest.toml`](./019/Manifest.toml) are automatically generated."
        if get_execution_mode() != "off"
        else ""
    ),
    "run_interactive": f"""
```{{margin}}
Run this notebook [on Binder]({BINDER_LINK}) or
{{ref}}`locally on Jupyter Lab <develop:Jupyter Notebooks>` to interactively
modify the parameters.
```
""",
}
myst_update_mathjax = False
nb_execution_excludepatterns = get_nb_exclusion_patterns()
nb_execution_mode = get_execution_mode()
nb_execution_show_tb = True
nb_execution_timeout = -1
nb_output_stderr = "remove"
nitpicky = True
primary_domain = "py"
project = REPO_TITLE
pygments_style = "sphinx"
remove_from_toctrees = [
    "adr/*",
    "report/*",
]
source_suffix = {
    ".ipynb": "myst-nb",
    ".md": "myst-nb",
}
suppress_warnings = [
    "myst.domains",
    "mystnb.unknown_mime_type",
]
thebe_config = {
    "repository_url": html_theme_options["repository_url"],
    "repository_branch": html_theme_options["repository_branch"],
}
