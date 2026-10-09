# Building and maintaining the documentation

The documentation is a standalone Sphinx project. Building HTML requires the
documentation dependencies only; it does not import TNLearn, PyTorch, or an
LLM client.

## Local build

Run from the documentation repository:

```bash
python -m pip install -r source/requirements.txt
make html
```

The output is `build/html/index.html`. The `build/` directory is ignored by
Git. To check every page and treat warnings as failures:

```bash
make html SPHINXOPTS="-E -a -n -W --keep-going"
python tools/check_links.py build/html
```

The same strict build runs in GitHub Actions and Read the Docs.

## Preview

```bash
python -m http.server 8000 --bind 127.0.0.1 --directory build/html
```

On a remote server, forward a local port from your workstation:

```bash
ssh -N -o ExitOnForwardFailure=yes -L 127.0.0.1:18000:127.0.0.1:8000 user@server
```

Then visit `http://127.0.0.1:18000/`. Keep that terminal open while previewing.
The local and remote port numbers do not need to match.

For automatic local rebuilds:

```bash
sphinx-autobuild source build/html --host 127.0.0.1 --port 8000 --watch examples --watch archive
```

Use this instead of another server bound to the same port.

## Page conventions

- Use descriptive lowercase filenames and hyphens, such as
  `symbolic-regression/polytensor.md`.
- Add every reader-facing page to a toctree. Keep concepts, discovery methods,
  estimator APIs, and layer APIs in their respective directories.
- Write the API against the documented release. Include mode, data shapes,
  return values, and expression-transfer behavior.
- Keep executable examples in `examples/` and include them with MyST
  `literalinclude`, so the displayed and checked code stay identical. Add a
  `:caption:` containing the example's filename.
- Put original adaptive SVG figures in `source/_static/paper/`, preserve
  attribution, and document any difference between a paper diagram and code.
- Extend `source/_ext/legacy_redirects.py` when replacing a published URL.

## Versions and appearance

The main site documents 0.2.1.dev0. The sidebar selector also opens the complete
0.2.0 stable reference and the 0.1.1 historical archive. Each has its own
navigation and search index.

| Source | HTML output | Purpose |
| --- | --- | --- |
| `source/` and `examples/` | `build/html/` | Development API and examples |
| `archive/0.2.0/` | `build/html/0.2.0/` | Frozen stable reference and example downloads |
| `archive/0.1.1/` | `build/html/0.1.1/` | Early API, theory, and benchmarks |

The main build includes both versioned builds. It uses only files in this
repository, with no Git history or sibling TNLearn checkout required on
Read the Docs or in CI. Version navigation is shared; stable content and its
example sources remain frozen. These selector entries are paths within the
same documentation build, independent of Read the Docs' project-level versions.

The earliest snapshot and editorial adjustments are recorded in
`archive/0.1.1/README.md`. Keep historical material in that archive;
current legacy-mode features belong in the main reference. The 0.2.0 snapshot
and its source commits are recorded in `archive/0.2.0/README.md`.

When publishing a new stable release, save the previous reference and examples
before changing the main version. Update version labels, installation commands,
release notes, and archive build configuration together. Check all version
selectors from nested pages and keep each search index scoped to its version.

The stylesheet follows `prefers-color-scheme`. Original SVG figures also
contain adaptive colors, so they follow the system preference without bitmap
inversion. Check both color schemes when updating styles or illustrations.
The shared `source/_static/docs.js` keeps wide tables accessible by keyboard
and synchronizes the mobile navigation button with the theme. Check narrow
screens as well as desktop layouts when changing tables or navigation.

## Check examples

In a separate environment containing the documented development revision:

```bash
python -m pip install "tnlearn @ git+https://github.com/NewT123-WM/tnlearn.git"
python tools/check_examples.py
```

This runs the local CPU examples, including forward/backward checks for layers
and a checkpoint round trip. It excludes `examples/llm.py` because that file
contacts an external provider and needs credentials. Run the LLM example
explicitly only after configuring the provider. The examples also cover random
formula generation and candidate filtering. The development update was checked
with Python 3.9 and PyTorch 2.5.1 CPU; this is not a full dependency compatibility
matrix. Because this command follows the official `main` branch, rerun it after
source updates to check the current development API.

To validate the frozen examples, use a separate environment with TNLearn 0.2.0:

```sh
python -m pip install "tnlearn==0.2.0"
python tools/check_examples.py archive/0.2.0/examples
```
