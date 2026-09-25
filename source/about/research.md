# Research and citation

## TNLearn package paper

**TNLearn: An Open Source Python Package for Task-based Neurons**  
Meng Wang, Tieyun Li, Juntong Fan, Hanyu Pei, Jing-Xiao Liao, Yaodong Yang,
Jianwei Ma, and Fenglei Fan. 2026.

[Read the arXiv preprint](https://arxiv.org/abs/2609.27564) ·
[arXiv PDF](https://arxiv.org/pdf/2609.27564) ·
[Local manuscript PDF](../_static/paper/tnlearn-paper.pdf).

The first three authors contributed equally. The preprint was submitted to
arXiv on September 23, 2026. The package paper has also been submitted to
JMLR and is currently **under review**.

| Paper section | Documentation |
| --- | --- |
| Framework and task-based neurons | [Task-based neurons](../guide/task-based-neurons.md) |
| Appendix C.1: genetic programming | [GPSymRegressor](../symbolic-regression/gp.md) |
| Appendix C.2: LLM-guided search | [LLMSymRegressor](../symbolic-regression/llm.md) |
| Appendix C.3: reinforcement learning | [RLSymRegressor](../symbolic-regression/rl.md) |
| Appendix C.4: polynomial tensor search | [PolyTensorRegressor](../symbolic-regression/polytensor.md) |

The paper provides the mathematical motivation and algorithm descriptions;
the API pages follow the 0.2.0 source. In particular, the paper uses
feature-by-sample notation in places. The public examples store samples in
rows and features in columns; `X` has shape `(n_samples, n_features)`.
The PolyTensor periodic branch and
the RL risk-seeking formulation described in the paper are not fully
implemented in this release. The method pages explain the implemented paths.

Cite the publicly available package paper as:

```bibtex
@misc{wang2026tnlearn,
  title={TNLearn: An Open Source Python Package for Task-based Neurons},
  author={Wang, Meng and Li, Tieyun and Fan, Juntong and Pei, Hanyu
          and Liao, Jing-Xiao and Yang, Yaodong and Ma, Jianwei
          and Fan, Fenglei},
  year={2026},
  eprint={2609.27564},
  archivePrefix={arXiv},
  primaryClass={cs.LG},
  url={https://arxiv.org/abs/2609.27564}
}
```

## Foundational work

The following citation is reproduced from the
[TNLearn source README](https://github.com/NewT123-WM/tnlearn#citation):

```bibtex
@article{fan2026no,
  title={No one-size-fits-all neurons: Task-based neurons for artificial neural networks},
  author={Fan, Feng-Lei and Wang, Meng and Dong, Hang-Cheng and Ma, Jianwei and Zeng, Tieyong},
  journal={IEEE Transactions on Pattern Analysis and Machine Intelligence},
  year={2026},
  publisher={IEEE}
}
```

## Benchmarks and related work

The <a href="../0.1.1/README_Page_1.html#benchmarks">0.1.1 benchmark table</a> preserves
the original numerical results and baseline references. It reports comparisons
against XGBoost, LightGBM, CatBoost,
TabNet, TabTransformer, FT-Transformer, and DANETs on particle-collision and
asteroid-diameter datasets. The small examples in this documentation verify
API usage; they do not reproduce those experiments or establish a new 0.2.0
performance claim.

Related resources collected in the source README include
[QuadraLib](https://github.com/zarekxu/QuadraLib),
[polynomial networks](https://github.com/grigorisg9gr/polynomial_nets), and
[Fenglei Fan's research code](https://github.com/FengleiFan).
