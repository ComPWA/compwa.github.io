# Common Partial Wave Analysis

```{title} Welcome

```

<!-- prettier-ignore-start -->
{{ '[![Google Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ComPWA/compwa.github.io/blob/{})'.format(branch) }} {{ '[![Binder](https://static.mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/ComPWA/compwa.github.io/{}?filepath=docs/usage)'.format(branch) }}
<!-- prettier-ignore-end -->

The ["Common Partial Wave Analysis"](https://github.com/ComPWA) organization (ComPWA) aims to make amplitude analysis accessible through transparent and interactive documentation, modern software development tools, and collaboration-independent frameworks. One major novelty is that we [formulate amplitude models symbolically](./symbolics.ipynb) with a Computer Algebra System, which results in a **self-documenting workflow** with high-performance, **backend-agnostic computations**.

Contact details can be found [here](https://github.com/ComPWA) on our GitHub organization page.

:::{card} {material-outlined}`calculate;1.5em` Symbolic amplitude models
:link: symbolics
:link-type: doc
Read more about computations with symbolic amplitude models here.
:::

## Main projects

ComPWA maintains **three main Python packages** with which you can do a full partial wave analysis. The packages are designed as **libraries**, so that they can be used separately by other projects.

Each of these libraries come with **interactive and interlinked documentation** that is intended to bring theory and code closer together. The PWA Pages takes that one step further: it is an independent and easy-to-maintain documentation project that can serve as a central place to gather links to PWA theory and software.

<!-- prettier-ignore -->
::::{grid} 1 2 2 2
:gutter: 2

:::{grid-item-card}

```{button-link} https://github.com/ComPWA/qrules
:color: primary
:expand:
:outline:
QRules
```

[![Documentation build status](https://readthedocs.org/projects/qrules/badge/?version=latest)](https://qrules.readthedocs.io)
[![10.5281/zenodo.5526360](https://zenodo.org/badge/doi/10.5281/zenodo.5526360.svg)](https://doi.org/10.5281/zenodo.5526360)
[![PyPI package](https://img.shields.io/pypi/pyversions/qrules)](https://pypi.org/project/qrules)
[![Conda package](https://anaconda.org/conda-forge/qrules/badges/version.svg)](https://anaconda.org/conda-forge/qrules)<br>
Rule-based particle reaction problem solver on a quantum number level

:::

:::{grid-item-card}

```{button-link} https://github.com/ComPWA/ampform
:color: primary
:expand:
:outline:
AmpForm
```

[![Documentation build status](https://readthedocs.org/projects/ampform/badge/?version=latest)](https://ampform.readthedocs.io)
[![10.5281/zenodo.5526648](https://zenodo.org/badge/doi/10.5281/zenodo.5526648.svg)](https://doi.org/10.5281/zenodo.5526648)
[![PyPI package](https://img.shields.io/pypi/pyversions/ampform)](https://pypi.org/project/ampform)
[![Conda package](https://anaconda.org/conda-forge/ampform/badges/version.svg)](https://anaconda.org/conda-forge/ampform)<br>
Automatically generate symbolic amplitude models for Partial Wave Analysis

:::

:::{grid-item-card}

```{button-link} https://github.com/ComPWA/tensorwaves
:color: primary
:expand:
:outline:
TensorWaves
```

[![Documentation build status](https://readthedocs.org/projects/tensorwaves/badge/?version=latest)](https://tensorwaves.readthedocs.io)
[![10.5281/zenodo.5526650](https://zenodo.org/badge/doi/10.5281/zenodo.5526650.svg)](https://doi.org/10.5281/zenodo.5526650)
[![PyPI package](https://img.shields.io/pypi/pyversions/tensorwaves)](https://pypi.org/project/tensorwaves)
[![Conda package](https://anaconda.org/conda-forge/tensorwaves/badges/version.svg)](https://anaconda.org/conda-forge/tensorwaves)<br>
Convert large symbolic expressions to numerical differentiable functions for performing
fast fits on large data samples

:::

:::{grid-item-card}

```{button-link} https://github.com/ComPWA/PWA-pages
:color: primary
:expand:
:outline:
PWA Pages
```

[![Documentation build status](https://readthedocs.org/projects/pwa/badge/?version=latest)](https://pwa.readthedocs.io)<br>
A central knowledge-base for Partial Wave Analysis theory and software

:::

::::

Finally, the {doc}`technical reports </reports>` on these pages
([compwa.github.io](https://compwa.github.io)) describe more general tips and
tricks, some of which can be of interest to general Python users as well!

:::{dropdown} Deprecated projects

The main packages listed above originate from the following, deprecated projects:

<!-- cspell:ignore pycompwa -->

- [ComPWA](https://compwa.github.io/legacy): a single framework for Partial Wave Analysis written in C++.
- [pycompwa](https://github.com/ComPWA/pycompwa): the Python interface of ComPWA, which also hosted a first version of the PWA Expert System.
- {doc}`PWA Expert System <expertsystem:index>` (split into {doc}`QRules <qrules:index>` and {doc}`AmpForm <ampform:index>`).

:::

## Long-term development

Partial Wave Analysis is a complicated research discipline, where several aspects of
quantum field theory, experimental physics, statistics, regression analysis, and
high-performance computing come together. This has led to
{ref}`a large number of PWA frameworks <pwa:software:Software inventory>` that taylor to
the need of each collaboration.

This state of affairs is only natural: research requires a flexible and specialized
approach. If, say, some background component shows up in an ongoing analysis, one may
need to implement some formalism that can handle it or add some alignment parameters
that were not yet supplied by the framework. It's therefore hard to facilitate ongoing
research, while at the same time developing a general, long-term PWA tool.

This situation however has a few major disadvantages:

- Collaborations usually start developing a PWA framework from scratch. It therefore
  takes years for packages to move beyond the basic PWA formalisms.
- Development is slow, because expertise is splintered: every group is working on their
  own package.
- Results become unreliable: the fewer people use a package, the more bugs will remain
  unnoticed.
- Once developers leave, the framework collapses. Sadly, this happens more often than
  not, as developers are usually scientists on short-term contracts.

ComPWA attempts to break this with the following ideals:

- Prioritize {ref}`index:Developer Experience` over functionality.
- Have everything {ref}`open source <index:Open source>` and remain
  collaboration-independent
- Offer functionality in the form of modules (libraries) that can serve as building
  blocks in more specialized scripts and frameworks ({ref}`index:Design`).
- Record and share acquired knowledge through
  {ref}`modern, interlinked documentation <index:User Experience>`.
- Follow industry standards and tools (e.g.
  {doc}`ticket system, CI, ADR, etc... </develop>`).

The first point is crucial. ComPWA rather sacrifices functionality for design and
developer experience related developments. Many other frameworks have started with the
same ideal of having a good software design etc., but soon begin to drop those ideals
for the understandable reasons described above. We believe that only by sticking to
those ideals, it is possible to maintain a long-term and collaboration-independent
common tool.

## Developer Experience

PWA is performed by researchers and this field of study is but relatively small. In
practice, users of PWA frameworks are therefore close to the development of the
framework itself. This means that, ideally, the gap between the developer and the user
should remain as small as possible.

In order to close this gap as best as possible, ComPWA follows the following ideas:

1. Frameworks are built up as **modular libraries with an accessible and well-documented
   [API](https://en.wikipedia.org/wiki/API)** (see for example
   [here](https://ampform.readthedocs.io/en/stable/api/ampform.html)). Users preferably
   set up their analysis through Jupyter notebooks or scripts that use these libraries.
   This allows the user to adapt to the specific challenges that their research
   challenges pose, while at the same time thinking along or improving the with the
   design and features offered by the library.
2. **New features are added to the library with care**, as to not let the library grow
   over time with features that are specific to certain analyses. Procedures are kept
   small and general enough, so that they can be used by different user scripts. This
   relates to 1., because the API and underlying code base should remain understandable.
3. It should be **easy to make the step from using the library to contributing to the
   source code**. The main starting points are the
   {ref}`example pages provided by each library <index:User experience>` (accessible
   without any software but a browser). From there, it should be just a matter of a
   running few command lines to start modifying and trying out changes to the code-bases
   (see e.g. {ref}`develop:Local set-up`) in a
   {ref}`standardized and automated environment <develop:Automated coding conventions>`.
4. **Developments industry techniques and software development tools are followed
   closely.** Despite the specific nature of PWA, many aspects can be performed or
   supported by existing technologies or packages. Think of the regression process that
   forms the basis of Machine Learning, but also the growing number of tools that are
   popular in data science, like [Pandas](https://pandas.pydata.org) and
   [Jupyter notebooks](https://jupyter.org).
5. As frameworks are {ref}`open source <index:Open source>` and users and developers
   come and go, **decision making is recorded as thoroughly as possible**. Fortunately,
   Git (commit history) and GitHub
   ({ref}`issues, PRs, and discussions <develop:Collaboration>`) make this extremely
   easy. In addition, larger decisions are recorded in the form of {doc}`ADRs </adr>`
   and explorations of challenges posed by physics and software are hosted in the form
   of {doc}`/reports`.

### Design

- Code modularity and transparency. For example, separation of {mod}`qrules`,
  {mod}`ampform`, and {mod}`tensorwaves`. The former two include all of the physics,
  while {mod}`tensorwaves` can use these amplitude models and perform fits, but aims to
  keep physics logic contained upstream.
- Keep the code simple by sticking to the core responsibility: construct amplitude
  models and fitting them to data. Avoid
  ["feature creep"](https://en.wikipedia.org/wiki/Feature_creep)!
- Accommodate both stable development and flexibility for ongoing analyses (see e.g.
  {ref}`develop:Branching model`).
- ComPWA values the
  [open-closed principle](https://en.wikipedia.org/wiki/Open%E2%80%93closed_principle).
  Where possible, libraries are intended to give users the flexibility to insert custom
  behavior (like custom dynamics) without having to introduce new updates to the
  library.

### Open source

ComPWA repositories are intended to be collaboration-independent. As such, they are
always public and open source and free to try out and re-use under the
[GPLv3+ license](https://www.gnu.org/licenses/gpl-3.0-standalone.html).

At the same time, open source projects come with many challenges: it is crucial to
{ref}`maintain strict standards for the code-base <develop:Automated coding conventions>`
from the start, when anyone is allowed to contribute.

## User Experience

PWA is a difficult field to get into and to navigate around. ComPWA therefore puts most
effort into maintaining **easily navigable and interactive documentation** that
**narrows the gap between code and theory**.

- All libraries provide example pages (see e.g. {doc}`here <ampform:usage>`). These
  pages are written as Jupyter notebook and provide a close link between code (how to
  use the library in a script, with links to the API) and theory (explanations of the
  basics being performed).
- Texts on the web-pages are thoroughly interlinked, so that the reader can easily to
  navigate to literature or external resources for more information. The intention is to
  make PWA a more accessible field for newcomers and to provide reference to the
  literature that was consulted for the implementation.
- Almost all ComPWA libraries are written in Python. This makes it easy for analysis
  users to install and use. In addition, the Python community has developed excellent
  tools that make it easy to document and maintain a clean codebase, so that is easy to
  make the step to become a {ref}`developer <index:Developer Experience>`.

This page is combines documentation on projects provided by the
[ComPWA organization on GitHub](https://github.com/ComPWA). It is more technical than
the [PWA Pages](https://pwa.rtfd.io) and focuses on the ComPWA organization only. Read
more about our ideals and ongoing projects on the {doc}`main</index>` page.

```{toctree}
---
caption: Resources
hidden:
---
test
symbolics
develop
adr
reports
references
Demo notebooks <https://github.com/ComPWA/demo/blob/main/README.md>
GitHub Repositories <https://github.com/ComPWA>
```

```{toctree}
---
caption: Main projects
hidden:
---
QRules <https://qrules.rtfd.io>
AmpForm <https://ampform.rtfd.io>
TensorWaves <https://tensorwaves.rtfd.io>
PWA Pages <https://pwa.rtfd.io>
```
