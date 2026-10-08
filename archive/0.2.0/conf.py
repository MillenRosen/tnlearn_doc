"""Build the frozen 0.2.0 reference with shared version navigation."""

from pathlib import Path
import sys

root = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(root / "source" / "_ext"))

project = "TNLearn"
author = "The TNLearn contributors"
copyright = "2024-2026, The TNLearn contributors"
version = release = "0.2.0"
language = "en"
extensions = ["myst_parser", "sphinx_copybutton", "legacy_redirects"]
source_suffix = {".rst": "restructuredtext", ".md": "markdown"}
exclude_patterns = ["_includes/**"]
myst_enable_extensions = ["dollarmath", "deflist", "colon_fence"]
myst_heading_anchors = 3
nitpicky = True
legacy_archive_path = "../0.1.1"

html_theme = "sphinx_rtd_theme"
html_title = "TNLearn 0.2.0 documentation"
html_logo = "source/_static/logo.png"
html_static_path = ["source/_static"]
templates_path = [str(root / "source" / "_templates")]
html_css_files = ["../../_static/custom.css"]
html_js_files = [
    ("../../_static/versions.js", {"defer": "defer"}),
    ("../../_static/docs.js", {"defer": "defer"}),
]
html_context = {"is_archive": False, "doc_channel": "stable", "version_root": "../"}
html_theme_options = {
    "logo_only": False,
    "version_selector": False,
    "language_selector": False,
    "collapse_navigation": True,
    "navigation_depth": 3,
    "prev_next_buttons_location": "bottom",
}
