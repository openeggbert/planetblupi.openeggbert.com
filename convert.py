#!/usr/bin/env python3
"""Convert all .md files in the doc/ directory tree to styled .html files.

Features:
- Shared CSS with dark sidebar navigation
- Code syntax highlighting via <pre><code> styling
- Internal .md links automatically rewritten to .html
- Sidebar navigation auto-generated from directory structure
- Breadcrumb trail
- Nothing from the Markdown source is lost
"""

import os
import re
import markdown
from pathlib import Path

DOC_ROOT = Path(__file__).parent

CSS = """
:root {
    --bg:        #0d1117;
    --sidebar-bg:#161b22;
    --border:    #30363d;
    --text:      #c9d1d9;
    --heading:   #e6edf3;
    --link:      #58a6ff;
    --link-hover:#79c0ff;
    --code-bg:   #161b22;
    --code-text: #f0f6fc;
    --pre-bg:    #161b22;
    --table-hd:  #21262d;
    --table-alt: #161b22;
    --accent:    #f78166;
    --sidebar-w: 280px;
}

*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

body {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
    background: var(--bg);
    color: var(--text);
    line-height: 1.65;
    display: flex;
    min-height: 100vh;
}

/* ── Sidebar ─────────────────────────────────────────── */
#sidebar {
    width: var(--sidebar-w);
    min-width: var(--sidebar-w);
    background: var(--sidebar-bg);
    border-right: 1px solid var(--border);
    position: sticky;
    top: 0;
    height: 100vh;
    overflow-y: auto;
    padding: 0 0 2rem 0;
    flex-shrink: 0;
}

#sidebar .logo {
    display: block;
    padding: 1rem 1rem 0.75rem 1rem;
    border-bottom: 1px solid var(--border);
    text-decoration: none;
    font-weight: 700;
    font-size: 0.95rem;
    color: var(--heading);
    letter-spacing: 0.02em;
}
#sidebar .logo span { color: var(--accent); }

#sidebar nav { padding: 0.5rem 0; }

#sidebar .section-title {
    display: block;
    font-size: 0.7rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    color: #6e7681;
    padding: 0.85rem 1rem 0.2rem 1rem;
}

#sidebar a.nav-link {
    display: block;
    padding: 0.28rem 1rem 0.28rem 1.3rem;
    font-size: 0.83rem;
    color: #8b949e;
    text-decoration: none;
    border-left: 2px solid transparent;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
    transition: color 0.15s, border-color 0.15s, background 0.15s;
}
#sidebar a.nav-link:hover {
    color: var(--link-hover);
    background: rgba(88,166,255,0.06);
    border-left-color: var(--link);
}
#sidebar a.nav-link.active {
    color: var(--link);
    border-left-color: var(--accent);
    background: rgba(247,129,102,0.08);
    font-weight: 600;
}
#sidebar a.nav-link.top-link {
    font-size: 0.85rem;
    color: #adbac7;
    padding-left: 1rem;
    font-weight: 600;
}

/* ── Main content ────────────────────────────────────── */
#main {
    flex: 1;
    min-width: 0;
    padding: 2.5rem 3rem 4rem 3rem;
    max-width: 960px;
}

/* ── Breadcrumb ──────────────────────────────────────── */
.breadcrumb {
    font-size: 0.78rem;
    color: #6e7681;
    margin-bottom: 1.5rem;
    display: flex;
    flex-wrap: wrap;
    gap: 0.25rem;
    align-items: center;
}
.breadcrumb a { color: var(--link); text-decoration: none; }
.breadcrumb a:hover { text-decoration: underline; }
.breadcrumb .sep { color: #6e7681; }

/* ── Typography ──────────────────────────────────────── */
h1, h2, h3, h4, h5, h6 {
    color: var(--heading);
    font-weight: 600;
    line-height: 1.3;
    margin-top: 1.8em;
    margin-bottom: 0.6em;
    border-bottom: 1px solid var(--border);
    padding-bottom: 0.3em;
}
h1 { font-size: 1.9rem; margin-top: 0; }
h2 { font-size: 1.4rem; }
h3 { font-size: 1.15rem; border-bottom: none; }
h4 { font-size: 1rem; border-bottom: none; color: var(--text); }

p { margin: 0.75em 0; }

a { color: var(--link); text-decoration: none; }
a:hover { text-decoration: underline; color: var(--link-hover); }

ul, ol { padding-left: 1.5em; margin: 0.5em 0; }
li { margin: 0.25em 0; }

/* ── Code ────────────────────────────────────────────── */
code {
    background: var(--code-bg);
    color: var(--code-text);
    padding: 0.15em 0.45em;
    border-radius: 4px;
    font-family: "SFMono-Regular", Consolas, "Liberation Mono", Menlo, monospace;
    font-size: 0.85em;
    border: 1px solid var(--border);
}

pre {
    background: var(--pre-bg);
    border: 1px solid var(--border);
    border-radius: 6px;
    padding: 1em 1.2em;
    overflow-x: auto;
    margin: 1em 0;
    line-height: 1.55;
}
pre code {
    background: transparent;
    border: none;
    padding: 0;
    font-size: 0.83rem;
    color: #e6edf3;
}

/* ── Tables ──────────────────────────────────────────── */
table {
    border-collapse: collapse;
    width: 100%;
    margin: 1em 0;
    font-size: 0.88rem;
    overflow-x: auto;
    display: block;
}
thead tr { background: var(--table-hd); }
th {
    border: 1px solid var(--border);
    padding: 0.5em 0.85em;
    text-align: left;
    color: var(--heading);
    font-weight: 600;
    white-space: nowrap;
}
td {
    border: 1px solid var(--border);
    padding: 0.45em 0.85em;
    vertical-align: top;
}
tbody tr:nth-child(even) { background: var(--table-alt); }
tbody tr:hover { background: #1c2128; }

/* ── Blockquote ──────────────────────────────────────── */
blockquote {
    border-left: 3px solid var(--accent);
    margin: 1em 0;
    padding: 0.5em 1em;
    background: rgba(247,129,102,0.07);
    border-radius: 0 4px 4px 0;
    color: #adbac7;
    font-style: italic;
}

/* ── HR ──────────────────────────────────────────────── */
hr {
    border: none;
    border-top: 1px solid var(--border);
    margin: 2em 0;
}

/* ── Responsive ──────────────────────────────────────── */
@media (max-width: 768px) {
    body { flex-direction: column; }
    #sidebar {
        width: 100%;
        height: auto;
        position: relative;
        border-right: none;
        border-bottom: 1px solid var(--border);
    }
    #main { padding: 1.5rem 1.2rem 3rem 1.2rem; }
}

/* ── Scroll ──────────────────────────────────────────── */
::-webkit-scrollbar { width: 6px; height: 6px; }
::-webkit-scrollbar-track { background: var(--bg); }
::-webkit-scrollbar-thumb { background: #30363d; border-radius: 3px; }
::-webkit-scrollbar-thumb:hover { background: #484f58; }
"""

# ── Sidebar navigation structure (ordered) ─────────────────────────────────

NAV = [
    ("Overview", [
        ("Overview",       "overview.html"),
        ("History & Speedy Blupi", "history.html"),
    ]),
    ("Architecture", [
        ("System Architecture",    "architecture/overview.html"),
        ("Source Files Reference", "architecture/source-files.html"),
    ]),
    ("Engine Internals", [
        ("Data Structures",      "engine/data-structures.html"),
        ("Game Phases",          "engine/game-phases.html"),
        ("Rendering",            "engine/rendering.html"),
        ("Pathfinding (A*)",     "engine/pathfinding.html"),
        ("Fog of War",           "engine/fog-of-war.html"),
        ("Minimap",              "engine/minimap.html"),
        ("Demo Recording",       "engine/demo.html"),
        ("Undo System",          "engine/undo.html"),
    ]),
    ("World (Map)", [
        ("World File Format",  "world/file-format.html"),
        ("World Grid",         "world/grid.html"),
        ("Terrain & Auto-tiling", "world/terrain.html"),
        ("Object Layer",       "world/objects.html"),
    ]),
    ("Characters", [
        ("Character Overview", "characters/overview.html"),
        ("Player (Blupi)",     "characters/blupi.html"),
        ("Enemies",            "characters/enemies.html"),
        ("Vehicles",           "characters/vehicles.html"),
        ("ACTION_* Codes",     "characters/actions.html"),
        ("GOAL_* Interpreter", "characters/goals.html"),
    ]),
    ("Gameplay", [
        ("Win Conditions",     "gameplay/win-conditions.html"),
        ("Toolbar Buttons",    "gameplay/toolbar.html"),
        ("Directions",         "gameplay/directions.html"),
        ("Skill Levels",       "gameplay/skill-levels.html"),
        ("Regions / Themes",   "gameplay/regions.html"),
        ("Cheat Codes",        "gameplay/cheat-codes.html"),
    ]),
    ("Assets", [
        ("Image Assets",   "assets/images.html"),
        ("Sound Effects",  "assets/sounds.html"),
        ("Music Tracks",   "assets/music.html"),
        ("Data Files",     "assets/data-files.html"),
        ("Movies",         "assets/movies.html"),
    ]),
    ("User Interface", [
        ("Windows Messages",     "ui/messages.html"),
        ("Cursor Sprites",       "ui/cursor-sprites.html"),
        ("Statistics Panel",     "ui/statistics.html"),
        ("Error Codes",          "ui/error-codes.html"),
    ]),
    ("Platforms", [
        ("Build System",     "platform/build.html"),
        ("Configuration",    "platform/config.html"),
        ("Localisation",     "platform/localisation.html"),
        ("Web / Emscripten", "platform/web.html"),
    ]),
    ("Speedy Blupi Reference", [
        ("Relation to Speedy Blupi", "speedy-blupi/overview.html"),
        ("actions.h Reference",      "speedy-blupi/actions-h.html"),
    ]),
]


def rel(from_html: Path, to_html_rel: str) -> str:
    """Return a relative URL from one HTML file to another (both relative to DOC_ROOT)."""
    from_dir = from_html.parent
    to = DOC_ROOT / to_html_rel
    return os.path.relpath(to, from_dir).replace(os.sep, "/")


def build_sidebar(current_html: Path) -> str:
    """Build the sidebar HTML for a given page."""
    current_rel = str(current_html.relative_to(DOC_ROOT)).replace(os.sep, "/")
    parts = ['<nav>']
    # Index link
    index_href = rel(current_html, "index.html")
    parts.append(
        f'<a class="nav-link top-link" href="{index_href}">&#8962; Index</a>'
    )
    for section_title, links in NAV:
        parts.append(f'<span class="section-title">{section_title}</span>')
        for label, href_rel in links:
            href = rel(current_html, href_rel)
            active = "active" if href_rel == current_rel else ""
            parts.append(
                f'<a class="nav-link {active}" href="{href}">{label}</a>'
            )
    parts.append('</nav>')
    return "\n".join(parts)


def build_breadcrumb(html_path: Path) -> str:
    """Build a breadcrumb like  Home > Architecture > Overview"""
    rel_path = html_path.relative_to(DOC_ROOT)
    parts = list(rel_path.parts)  # e.g. ['architecture', 'overview.html']
    crumbs = []
    # Home
    depth = len(parts) - 1
    home_href = "../" * depth + "index.html"
    crumbs.append(f'<a href="{home_href}">Home</a>')
    if len(parts) > 1:
        # Directory level
        dir_name = parts[0].replace("-", " ").title()
        crumbs.append(f'<span class="sep">/</span>')
        if len(parts) > 2:
            crumbs.append(f'<span>{dir_name}</span>')
        else:
            crumbs.append(f'<span>{dir_name}</span>')
    if len(parts) > 1:
        page_name = parts[-1].replace(".html", "").replace("-", " ").title()
        crumbs.append(f'<span class="sep">/</span>')
        crumbs.append(f'<span>{page_name}</span>')
    return '<div class="breadcrumb">' + " ".join(crumbs) + "</div>"


def rewrite_links(html_content: str) -> str:
    """Replace .md links with .html links in rendered HTML."""
    return re.sub(r'href="([^"]*?)\.md([^"]*?)"', r'href="\1.html\2"', html_content)


def md_to_html(md_path: Path) -> str:
    """Convert a .md file to HTML body content."""
    text = md_path.read_text(encoding="utf-8")
    md = markdown.Markdown(extensions=["tables", "fenced_code", "toc"])
    html = md.convert(text)
    return rewrite_links(html)


def page_title(md_path: Path) -> str:
    """Extract the first H1 heading from markdown as the page title."""
    text = md_path.read_text(encoding="utf-8")
    m = re.search(r'^#\s+(.+)$', text, re.MULTILINE)
    return m.group(1).strip() if m else md_path.stem.replace("-", " ").title()


def build_page(md_path: Path, html_path: Path) -> None:
    """Build a full HTML page from a markdown file."""
    body = md_to_html(md_path)
    title = page_title(md_path)
    sidebar = build_sidebar(html_path)
    breadcrumb = build_breadcrumb(html_path)

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} — Planet Blupi Docs</title>
<style>
{CSS}
</style>
</head>
<body>
<aside id="sidebar">
  <a class="logo" href="{rel(html_path, 'index.html')}">
    <span>&#9679;</span> Planet Blupi Docs
  </a>
  {sidebar}
</aside>
<main id="main">
  {breadcrumb}
  {body}
</main>
<script>
// Highlight active nav link also by current URL
(function(){{
  var links = document.querySelectorAll('#sidebar a.nav-link');
  var cur = window.location.pathname.split('/').pop() || 'index.html';
  links.forEach(function(a){{
    if(a.getAttribute('href').split('/').pop() === cur) a.classList.add('active');
  }});
}})();
</script>
</body>
</html>"""
    html_path.parent.mkdir(parents=True, exist_ok=True)
    html_path.write_text(html, encoding="utf-8")
    print(f"  {html_path.relative_to(DOC_ROOT)}")


def build_index(html_path: Path) -> None:
    """Build the index.html from README.md (or a dedicated index page)."""
    readme = DOC_ROOT / "README.md"
    build_page(readme, html_path)


def main():
    print("Converting Markdown → HTML ...")
    count = 0

    # Convert all .md files except convert.py itself and README (handled separately)
    for md_path in sorted(DOC_ROOT.rglob("*.md")):
        if md_path.name == "README.md":
            # Also convert as index.html at its level
            html_path = md_path.with_suffix(".html")
            build_page(md_path, html_path)
            count += 1
            # For root README, also write as index.html
            if md_path.parent == DOC_ROOT:
                index_html = DOC_ROOT / "index.html"
                build_page(md_path, index_html)
                count += 1
            continue
        html_path = md_path.with_suffix(".html")
        build_page(md_path, html_path)
        count += 1

    print(f"\nDone. {count} HTML files written.")


if __name__ == "__main__":
    main()
