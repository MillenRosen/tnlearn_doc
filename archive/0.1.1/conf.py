"""Compatibility build configuration for the early documentation archive."""

from pathlib import Path

project = "TNLearn"
author = "The TNLearn contributors"
copyright = "2024, The TNLearn contributors"
version = release = "0.1.1"
language = "en"
extensions = ["myst_parser", "sphinx_copybutton"]
source_suffix = {".rst": "restructuredtext", ".md": "markdown"}
myst_enable_extensions = ["dollarmath", "deflist"]
myst_heading_anchors = 3
html_theme = "sphinx_rtd_theme"
html_title = "TNLearn 0.1.1 archive"
html_logo = "source/_static/logo.png"
html_static_path = ["source/_static"]
templates_path = [str(Path(__file__).resolve().parents[2] / "source" / "_templates")]
html_css_files = ["../../_static/custom.css"]
html_js_files = [
    ("../../_static/versions.js", {"defer": "defer"}),
    ("../../_static/docs.js", {"defer": "defer"}),
]
html_context = {"is_archive": True}
html_theme_options = {
    "version_selector": False,
    "language_selector": False,
    "collapse_navigation": True,
    "navigation_depth": 2,
}
