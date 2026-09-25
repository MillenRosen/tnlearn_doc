# TNLearn documentation

Sphinx documentation for **TNLearn 0.2.0**, using MyST Markdown and the
Read the Docs theme.

- [Published documentation](https://tnlearn-documentation.readthedocs.io/en/latest/)
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
| `source/api/` | MLP estimators, preprocessing, expression utilities |
| `source/modules/` | Fully connected, convolutional, recurrent, Transformer layers |
| `source/about/` | Manuscript, citations, project, contributors |
| `source/_static/paper/` | Attributed manuscript PDF and original adaptive SVG figures |
| `source/_ext/` | Redirects from old numbered pages |
| `examples/` | Executable code included directly in the documentation |
| `tools/` | Local link and example checks |
| `archive/0.1.1/` | Early documentation, theory, API, and benchmarks; independently built under `0.1.1/` |

## Validation

```bash
make html SPHINXOPTS="-E -a -n -W --keep-going"
python tools/check_links.py build/html
```

For runtime checks, use a separate environment with the library installed:

```bash
python -m pip install "tnlearn==0.2.0"
python tools/check_examples.py
```

To validate a sibling source checkout, install `../tnlearn` instead.
The initial update was checked against source commit
`0ae14184a0e15bca352eb8a22c6ca6a005ba4a8a`, Python 3.9, and PyTorch 2.5.1
CPU. The LLM example is excluded from automated execution because it contacts
an external provider. It is syntax-checked with the other examples; its
search/export/training path was also checked separately with a fixed offline
provider response.

The [package paper](https://arxiv.org/abs/2609.27564) informs the method explanations.
API behavior follows the inspected source, including documented differences
from the paper and implementation limitations. See
`source/_static/paper/README.txt` for figure provenance.

See [the maintainer guide](source/contributing.md) for page conventions and
remote preview commands. Legacy `Page_*.html` links remain usable through
build-time redirects; add new content under descriptive filenames.
