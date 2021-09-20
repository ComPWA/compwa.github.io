# About

The ["Common Partial Wave Analysis"](https://github.com/ComPWA) organization
(ComPWA) aims to make amplitude analysis accessible through transparent and
interactive documentation, modern software development tools, and
collaboration-independent frameworks. **Contact details** can be found
[here](https://github.com/ComPWA).

:::{note}

This page sets out some of the ideals of the ComPWA organization. For practical
details, see the {doc}`develop page <develop>`.

:::

## Main projects

The main projects that ComPWA is currently developing are:

- {doc}`QRules <qrules:index>`, a package that helps generating allowed
  transitions between quantum states on the basis of quantum number
  conservation rules.
- {doc}`AmpForm <qrules:index>`, which helps to formulate amplitude models for
  different spin formalisms and with different dynamics.
- {doc}`TensorWaves <qrules:index>`, a fitter and data generation package for
  multiple computational back-ends.
- {doc}`PWA Pages <pwa:index>`, an overview of the basis of Partial Wave
  Analysis that provides links to the most important literature and software in
  the field.

Finally, the {doc}`technical reports </reports>` on these pages
([compwa-org.rtfd.io](https://compwa-org.readthedocs.io)) describe more general
tips and tricks, some of which can be of interest to general Python users as
well!

:::{dropdown} Deprecated projects

The main packages listed above originate from the following, deprecated
projects:

<!-- cspell:ignore pycompwa -->

- {doc}`ComPWA <ComPWA:index>`: a single framework for Partial Wave Analysis
  written in C++.
- {doc}`pycompwa <pycompwa:index>`: the Python interface of ComPWA, which also
  hosted a first version of the PWA Expert System.
- {doc}`PWA Expert System <expertsystem:index>` (split into
  {doc}`QRules <qrules:index>` and {doc}`AmpForm <ampform:index>`).

:::

## Long-term development

Partial Wave Analysis is a complicated research discipline, where several
aspects of quantum field theory, experimental physics, statistics, regression
analysis, and high-performance computing come together. This has led to
{ref}`a large number of PWA frameworks <pwa:software:Inventory of PWA projects>`
that taylor to the need of each collaboration.

This state of affairs is only natural: research requires a flexible and
specialized approach. If, say, some background component shows up in an ongoing
analysis, one may need to implement some formalism that can handle it or add
some alignment parameters that were not yet supplied by the framework. It's
therefore hard to facilitate ongoing research, while at the same time
developing a general, long-term PWA tool.

This situation however has a few major disadvantages:

- Collaborations usually start developing a PWA framework from scratch. It
  therefore takes years for packages to move beyond the basic PWA formalisms.
- Development is slow, because expertise is splintered: every group is working
  on their own package.
- Results become unreliable: the fewer people use a package, the more bugs will
  remain unnoticed.
- Once developers leave, the framework collapses. Sadly, this happens more
  often than not, as developers are usually scientists on short-term contracts.

ComPWA attempts to break this with the following ideals:

- Put {ref}`about:Developer Experience` before functionality.
- Have everything {ref}`open source <about:Open source>`.
- Remain collaboration-independent and general in applicability
  ({ref}`about:Design`).
- Record and share acquired knowledge through
  {ref}`modern, interlinked documentation <about:User Experience>`.
- Follow industry standards and tools (e.g.
  {doc}`ticket system, CI, ADR, etc... </develop>`).

The first point is crucial. ComPWA rather sacrifices functionality for design
and developer experience related developments. Many other frameworks have
started with the same ideal of having a good software design etc., but soon
begin to drop those ideals for the understandable reasons described above. We
believe that only by sticking to those ideals, it is possible to maintain a
long-term and collaboration-independent common tool.

## Developer Experience

PWA is performed by researchers and this field of study is but relatively
small. In practice, users of PWA frameworks are therefore close to the
development of the framework itself. This means that, ideally, the gap between
the developer and the user should remain as small as possible.

In order to close this gap as best as possible, ComPWA follows the following
ideas:

1. Frameworks are built up as **modular libraries with an accessible and
   well-documented [API](https://en.wikipedia.org/wiki/API)** (see for example
   [here](https://ampform.readthedocs.io/en/stable/api/ampform.html)). Users
   preferably set up their analysis through Jupyter notebooks or scripts that
   use these libraries. This allows the user to adapt to the specific
   challenges that their research challenges pose, while at the same time
   thinking along or improving the with the design and features offered by the
   library.
2. **New features are added to the library with care**, as to not let the
   library grow over time with features that are specific to certain analyses.
   Procedures are kept small and general enough, so that they can be used by
   different user scripts. This relates to 1., because the API and underlying
   code base should remain understandable.
3. It should be **easy to make the step from using the library to contributing
   to the source code**. The main starting points are the
   {ref}`example pages provided by each library <about:User experience>`
   (accessible without any software but a browser). From there, it should be
   just a matter of a running few command lines to start modifying and trying
   out changes to the code-bases (see e.g. {ref}`develop:Local set-up`) in a
   {ref}`standardized and automated environment <develop:Automated coding conventions>`.
4. **Developments industry techniques and software development tools are
   followed closely.** Despite the specific nature of PWA, many aspects can be
   performed or supported by existing technologies or packages. Think of the
   regression process that forms the basis of Machine Learning, but also the
   growing number of tools that are popular in data science, like
   [Pandas](https://pandas.pydata.org) and
   [Jupyter notebooks](https://jupyter.org).
5. As frameworks are {ref}`open source <about:Open source>` and users and
   developers come and go, **decision making is recorded as thoroughly as
   possible**. Fortunately, Git (commit history) and GitHub
   ({ref}`issues, PRs, and discussions <develop:Collaboration>`) make this
   extremely easy. In addition, larger decisions are recorded in the form of
   {doc}`ADRs </adr>` and explorations of challenges posed by physics and
   software are hosted in the form of {doc}`/reports`.

### Design

- Code modularity and transparency. For example, separation of {mod}`qrules`,
  {mod}`ampform`, and {mod}`tensorwaves`. The former two include all of the
  physics, while {mod}`tensorwaves` can use these amplitude models and perform
  fits, but aims to keep physics logic contained upstream.
- Keep the code simple by sticking to the core responsibility: construct
  amplitude models and fitting them to data.
- Accommodate both stable development and flexibility for ongoing analyses (see
  e.g. {ref}`develop:Branching model`).
- ComPWA values the
  [open-closed principle](https://en.wikipedia.org/wiki/Open%E2%80%93closed_principle).
  Where possible, libraries are intended to give users the flexibility to
  insert custom behavior (like custom dynamics) without having to introduce new
  updates to the library.

### Open source

ComPWA repositories are intended to be collaboration-independent. As such, they
are always public and open source and free to try out and re-use under the
[GPLv3+ license](https://www.gnu.org/licenses/gpl-3.0-standalone.html).

At the same time, open source projects come with many challenges: it is crucial
to
{ref}`maintain strict standards for the code-base <develop:Automated coding conventions>`
from the start, when anyone is allowed to contribute.

## User Experience

PWA is a difficult field to get into and to navigate around. ComPWA therefore
puts most effort into maintaining **easily navigable and interactive
documentation** that **narrows the gap between code and theory**.

- All libraries provide example pages (see e.g. {doc}`here <ampform:usage>`).
  These pages are written as Jupyter notebook and provide a close link between
  code (how to use the library in a script, with links to the API) and theory
  (explanations of the basics being performed).
- Texts on the web-pages are thoroughly interlinked, so that the reader can
  easily to navigate to literature or external resources for more information.
  The intention is to make PWA a more accessible field for newcomers and to
  provide reference to the literature that was consulted for the
  implementation.
- Almost all ComPWA libraries are written in Python. This makes it easy for
  analysis users to install and use. In addition, the Python community has
  developed excellent tools that make it easy to document and maintain a clean
  codebase, so that is easy to make the step to become a
  {ref}`developer <about:Developer Experience>`.
