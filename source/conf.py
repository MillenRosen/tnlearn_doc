"""Documentation for the TNLearn 0.2.0 public API."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent / "_ext"))

project = "TNLearn"
author = "The TNLearn contributors"
copyright = "2024-2026, The TNLearn contributors"
version = "0.2"
release = "0.2.0"
language = "en"
extensions = ["myst_parser", "sphinx_copybutton", "legacy_redirects", "version_archive"]
source_suffix = {".rst": "restructuredtext", ".md": "markdown"}
exclude_patterns = ["_includes/**"]
myst_enable_extensions = ["dollarmath", "deflist", "colon_fence"]
myst_heading_anchors = 3
nitpicky = True

html_theme = "sphinx_rtd_theme"
html_title = "TNLearn 0.2.0 documentation"
html_logo = "_static/logo.png"
html_static_path = ["_static"]
html_css_files = ["custom.css"]
html_js_files = [("versions.js", {"defer": "defer"}), ("docs.js", {"defer": "defer"})]
templates_path = ["_templates"]
html_context = {"is_archive": False}
html_theme_options = {
    "logo_only": False,
    "version_selector": False,
    "language_selector": False,
    "collapse_navigation": True,
    "navigation_depth": 3,
    "prev_next_buttons_location": "bottom",
}
