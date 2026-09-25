"""Keep published page URLs usable after the 0.2.0 reorganization."""

import html
import json
from pathlib import Path

PAGES = {
    "README_Page_1": "index",
    "Page_1": "index",
    "Page_2": "guide/task-based-neurons",
    "Page_3": "getting-started/installation",
    "Page_4": "api/index",
    "Page_5": "symbolic-regression/index",
    "1page/index": "../index",
}
API_ANCHORS = {
    "tnlearn-vecsymregressor": "migration",
    "tnlearn-mlpclassifier": "api/mlp-classifier",
    "tnlearn-mlpregressor": "api/mlp-regressor",
    "tnlearn-llmsymregressor": "symbolic-regression/llm",
    "tnlearn-rlregressor": "migration",
    "tnlearn-modules-taskbased-neural-modules": "modules/index",
    "tnlinear": "modules/linear",
}
for name in ("tnconv1d", "tnconv2d", "tnconv3d",
             "tnconvtranspose1d", "tnconvtranspose2d", "tnconvtranspose3d"):
    API_ANCHORS[name] = "modules/convolution"
for name in ("tnrnn", "tnlstm", "tngru", "tnrnncell", "tnlstmcell", "tngrucell"):
    API_ANCHORS[name] = "modules/recurrent"
for name in ("tntransformer", "tntransformerencoder", "tntransformerdecoder",
             "tntransformerencoderlayer", "tntransformerdecoderlayer"):
    API_ANCHORS[name] = "modules/transformer"

PAGE_ANCHORS = {
    "Page_4": {key: value + ".html" for key, value in API_ANCHORS.items()},
    "README_Page_1": {
        "benchmarks": "0.1.1/README_Page_1.html#benchmarks",
    },
    "Page_2": {
        anchor: "0.1.1/Page_2.html#" + anchor
        for anchor in (
            "why-task-based-neurons", "what-are-task-based-neurons",
            "when-to-use-task-based-neurons", "reference",
        )
    },
}


def write_redirects(app, exception):
    if exception is not None or app.builder.name != "html":
        return
    for old, new in PAGES.items():
        target = new + ".html"
        destination = Path(app.outdir, old + ".html")
        destination.parent.mkdir(parents=True, exist_ok=True)
        anchors = PAGE_ANCHORS.get(old, {})
        destination.write_text(
            '<!doctype html><html lang="en"><head><meta charset="utf-8">'
            '<title>TNLearn documentation has moved</title>'
            f'<meta http-equiv="refresh" content="0; url={html.escape(target)}">'
            '<script>const pages=' + json.dumps(anchors) + ';'
            'location.replace(pages[location.hash.slice(1)] || '
            + json.dumps(target) + ');</script></head><body>'
            f'<p>This page has moved to <a href="{html.escape(target)}">'
            'TNLearn 0.2.0 documentation</a>.</p></body></html>',
            encoding="utf-8",
        )


def setup(app):
    app.connect("build-finished", write_redirects)
    return {"parallel_read_safe": True, "parallel_write_safe": True}
