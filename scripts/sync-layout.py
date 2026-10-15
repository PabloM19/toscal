#!/usr/bin/env python3
"""Share the approved home header and footer without a runtime dependency."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / 'prototype'
source = (ROOT / 'index.html').read_text()
header = source[source.index('    <a class="skip-link"'):source.index('    <main id="contenido">')]
footer = source[source.index('    <footer class="home-footer">'):source.index('    <script src="site.js"')]
for path in sorted(ROOT.glob('*.html')):
    if path.name == 'index.html':
        continue
    page = path.read_text()
    start = page.index('    <a class="skip-link"')
    main = page.index('    <main id="contenido">')
    footer_start = page.index('    <footer class="home-footer">')
    footer_end = page.index('</footer>', footer_start) + len('</footer>')
    tail = page[footer_end:].lstrip('\n')
    current = header
    current = current.replace(f'href="{path.name}"', f'href="{path.name}" aria-current="page"')
    path.write_text(page[:start] + current + page[main:footer_start] + footer + tail)
    print(f'Layout común: {path.name}')
