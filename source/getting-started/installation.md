# Installation

## Install the development version

These pages document **0.2.1.dev0** at source revision
[`d5d6b01`](https://github.com/NewT123-WM/tnlearn/commit/d5d6b01ff84d90d6f4539d45a898dd2fc7e9839f).
The random-formula APIs require this development code; they are not included
in the published 0.2.0 package.

For a separate Conda environment and a reproducible source checkout:

```sh
conda create -n tnlearn-dev python=3.11
conda activate tnlearn-dev
git clone https://github.com/NewT123-WM/tnlearn.git
cd tnlearn
git checkout d5d6b01ff84d90d6f4539d45a898dd2fc7e9839f
python -m pip install -e .
python -c "import tnlearn; print(tnlearn.__version__)"
```

The version check should print `0.2.1.dev0`. The pinned commit keeps these
examples aligned with the documented API. To follow ongoing development,
switch the checkout to `main` and pull future updates; its behavior may change.

For GPU use, install a PyTorch build appropriate for your hardware using the
[official PyTorch selector](https://pytorch.org/get-started/locally/) before
installing TNLearn. An existing compatible installation satisfies the PyTorch
dependency.

## Install the stable release

```sh
python -m pip install "tnlearn==0.2.0"
python -c "import tnlearn; print(tnlearn.__version__)"
```

For this installation, use the
<a href="../0.2.0/index.html">0.2.0 stable documentation</a>.

## Dependencies

The development package metadata declares Python `>=3.8` and PyTorch `>=1.12.0`.
These are declared lower bounds, not a tested compatibility matrix for every
module. In particular, the Transformer implementation uses newer PyTorch
interfaces. Use a recent compatible PyTorch build for Transformer workflows.

The development package declares the following dependencies in `pyproject.toml`.
Pip installs them automatically; the historical pinned package list from the
0.1 documentation is no longer required.

| Package | Declared requirement |
| --- | --- |
| PyTorch | `torch>=1.12.0` |
| NumPy | `numpy>=1.19.0` |
| scikit-learn | `scikit-learn>=1.0.0` |
| pandas | `pandas>=1.3.0` |
| SymPy | `sympy>=1.7` |
| tqdm | `tqdm>=4.64.0` |
| Matplotlib | `matplotlib>=3.5.0` |
| IPython | `ipython>=8.0.0` |
| torchinfo | `torchinfo>=1.5.0` |
| h5py | `h5py>=3.1.0` |
| Requests | `requests>=2.28.0` |
| setuptools | `setuptools>=61.0.0` |

SciPy is used by the symbolic search code and is also installed through
scikit-learn's dependencies.

## Build the documentation

Building this site only requires the [documentation dependencies](../contributing.md).
It does not import TNLearn, train a model, require CUDA, or contact an LLM.

Continue with the [quick start](quickstart.md).
