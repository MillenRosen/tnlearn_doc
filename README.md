# TNLearn documentation

Sphinx documentation for **TNLearn 0.2.1.dev0**, with the complete **0.2.0
stable reference** and **0.1.1 archive**, using MyST Markdown and the Read the
Docs theme.

- [Published documentation](https://tnlearn-documentation.readthedocs.io/en/latest/)
- [0.2.0 stable reference](https://tnlearn-documentation.readthedocs.io/en/latest/0.2.0/)
- [Library source](https://github.com/NewT123-WM/tnlearn)
- [Documentation source](https://github.com/MillenRosen/tnlearn_doc)

## Build

```bash
conda create -n tnlearn-doc python=3.9
conda activate tnlearn-doc
python -m pip install -r source/requirements.txt
make html
```

Open `build/html/index.html` or serve it with:

```bash
python -m http.server 8000 --bind 127.0.0.1 --directory build/html
```

Generated files stay in the ignored `build/` directory. The build does not
need TNLearn, PyTorch, or API keys.

## Structure

| Directory | Contents |
| --- | --- |
| `source/getting-started/` | Installation and complete first workflow |
| `source/examples/` | Examples organized by task, with code downloads |
| `source/guide/` | Neuron principles, base/legacy expressions, training |
| `source/symbolic-regression/` | GP, LLM, RL, and PolyTensor methods |
| `source/api/` | MLP estimators, random formulas, preprocessing, expression utilities |
| `source/modules/` | Fully connected, convolutional, recurrent, Transformer layers |
| `source/about/` | Manuscript, citations, project, contributors |
| `source/_static/paper/` | Attributed manuscript PDF and original adaptive SVG figures |
| `source/_ext/` | Versioned builds and redirects from old numbered pages |
| `examples/` | Executable code included directly in the documentation |
| `tools/` | Local link and example checks |
| `archive/0.2.0/` | Frozen stable pages, media, and examples; independently built under `0.2.0/` |
| `archive/0.1.1/` | Early documentation, theory, API, and benchmarks; independently built under `0.1.1/` |

## Validation

```bash
make html SPHINXOPTS="-E -a -n -W --keep-going"
python tools/check_links.py build/html
```

For runtime checks, use a separate environment with the library installed:

```bash
python -m pip install "tnlearn @ git+https://github.com/NewT123-WM/tnlearn.git"
python tools/check_examples.py
```

To validate a sibling source checkout, install `../tnlearn` instead.
The development documentation follows the latest official `main` source and
was checked with Python 3.9 and PyTorch 2.5.1 CPU. The LLM example is excluded
from automated execution because it contacts an external provider. It is
syntax-checked with the other examples; its search/export/training path was
also checked separately with a fixed offline provider response.

The 0.2.0 snapshot records its original source revision in
`archive/0.2.0/README.md`. To check its examples against a separate 0.2.0
installation, run `python tools/check_examples.py archive/0.2.0/examples`.

The version selector uses paths within one HTML build, so local preview and
Read the Docs expose all three references without additional hosted-version
configuration. Stable and historical search indexes exclude development pages.

The [package paper](https://arxiv.org/abs/2609.27564) informs the method explanations.
API behavior follows the inspected source, including documented differences
from the paper and implementation limitations. See
`source/_static/paper/README.txt` for figure provenance.

See [the maintainer guide](source/contributing.md) for page conventions and
remote preview commands. Legacy `Page_*.html` links remain usable through
build-time redirects; add new content under descriptive filenames.
