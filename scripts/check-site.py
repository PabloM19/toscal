#!/usr/bin/env python3
"""Check local routes, anchors, HTML metadata and media in the static site."""
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import json

ROOT = Path(__file__).resolve().parents[1] / 'prototype'
class Page(HTMLParser):
    def __init__(self, path):
        super().__init__()
        self.path = path
        self.ids, self.refs, self.images, self.iframes = [], [], [], []
        self.h1 = 0
        self.feed(path.read_text())
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if 'id' in attrs: self.ids.append(attrs['id'])
        if tag == 'h1': self.h1 += 1
        if tag in ['a', 'link', 'script', 'use']:
            ref = attrs.get('href') or attrs.get('src')
            if ref: self.refs.append(ref)
        if tag == 'img':
            self.images.append(attrs)
            self.refs.append(attrs.get('src', ''))
            self.refs.extend(item.strip().split()[0] for item in attrs.get('srcset', '').split(',') if item.strip())
        if tag == 'iframe': self.iframes.append(attrs)
pages = {p.resolve(): Page(p) for p in ROOT.glob('*.html')}
errors, ref_count, image_count = [], 0, 0
for path, page in pages.items():
    if page.h1 != 1: errors.append(f'{path.name}: {page.h1} H1 headings')
    for value, count in Counter(page.ids).items():
        if count > 1: errors.append(f'{path.name}: duplicate id {value}')
    for ref in page.refs:
        url = urlsplit(ref)
        if url.scheme or url.netloc: continue
        ref_count += 1
        target = (path.parent / unquote(url.path)).resolve() if url.path else path
        if not target.is_file(): errors.append(f'{path.name}: missing local resource {ref}')
        elif url.fragment and target in pages and url.fragment not in pages[target].ids:
            errors.append(f'{path.name}: missing anchor {ref}')
    for image in page.images:
        image_count += 1
        if not all(key in image for key in ['src', 'alt', 'width', 'height']):
            errors.append(f'{path.name}: incomplete image metadata {image.get("src")}')
    for frame in page.iframes:
        if not frame.get('title'): errors.append(f'{path.name}: iframe has no title')
print(json.dumps({'pages': len(pages), 'local_references': ref_count, 'images': image_count, 'errors': errors}, ensure_ascii=False, indent=2))
raise SystemExit(bool(errors))
