# Historical documentation archive

Source: https://github.com/MillenRosen/tnlearn_doc
Snapshot: a44f8bec1f6d8339527527c16421f9deb85e5bfa (2024-03-23, earliest commit).
The complete original checkout is retained separately at the workspace's
`tnlearn-doc-old/`; this directory vendors the reader-facing historical pages.

The 0.1.1 archive label follows the project's release-documentation naming.
The original snapshot called its documentation `v1` and displayed a 0.1.0
PyPI badge; it was not a tagged 0.1.1 documentation release.

Preserved: introductory theory and references, benchmark values, historical
API descriptions, diagrams, contributor and license statements.

Editorial changes: replace the placeholder homepage, remove unfinished
overview/citation placeholders, correct build formatting and broken navigation,
and pin installation instructions to 0.1.1. The original homepage's unsupported
JMLR-publication announcement is not reproduced. These edits do not update the
historical API to 0.2.0 or equate it with current legacy mode.
Figure alternative text was added, and the duplicated title in reference [16]
was corrected against its linked arXiv record (1610.01145).

The main Sphinx build invokes this archive as a separate site at
`build/html/0.1.1/`. Its navigation and search index remain independent.
It shares the current site's stylesheet, system color preference, and version
selector. No network checkout or TNLearn installation is needed at build time.
