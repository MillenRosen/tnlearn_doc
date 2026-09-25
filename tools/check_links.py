"""Check local HTML links, fragments, and assets after a Sphinx build."""

from html.parser import HTMLParser
from pathlib import Path
import sys
from urllib.parse import unquote, urlsplit


class Page(HTMLParser):
    def __init__(self, path):
        super().__init__(convert_charrefs=True)
        self.ids = set()
        self.links = []
        self.feed(path.read_text(encoding="utf-8"))

    def handle_starttag(self, tag, attrs):
        values = dict(attrs)
        if "id" in values:
            self.ids.add(values["id"])
        if tag == "a" and "name" in values:
            self.ids.add(values["name"])
        for attribute in ("href", "src"):
            if values.get(attribute):
                self.links.append(values[attribute])
        if tag == "option" and values.get("value"):
            self.links.append(values["value"])


def main():
    root = Path(sys.argv[1] if len(sys.argv) > 1 else "build/html").resolve()
    pages = {path: Page(path) for path in root.rglob("*.html")}
    if not pages:
        print("No HTML pages found in {}".format(root), file=sys.stderr)
        return 1
    errors = []
    links_checked = 0
    for path, page in pages.items():
        for link in page.links:
            url = urlsplit(link)
            if url.scheme or url.netloc:
                continue
            target_path = unquote(url.path)
            if target_path.startswith("/"):
                target = root / target_path.lstrip("/")
            elif target_path:
                target = path.parent / target_path
            else:
                target = path
            target = target.resolve()
            if target.is_dir():
                target = target / "index.html"
            links_checked += 1
            if not target.is_file():
                errors.append("{}: missing {}".format(path.relative_to(root), link))
            elif url.fragment and target in pages:
                fragment = unquote(url.fragment)
                if fragment not in pages[target].ids:
                    errors.append(
                        "{}: missing fragment {}".format(path.relative_to(root), link)
                    )
    for error in errors:
        print(error, file=sys.stderr)
    print("{} HTML pages, {} local links, {} errors.".format(
        len(pages), links_checked, len(errors)
    ))
    return bool(errors)


if __name__ == "__main__":
    sys.exit(main())
