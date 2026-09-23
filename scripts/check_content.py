#!/usr/bin/env python3
"""Check repository navigation, anchors, media references, and recipe structure.

Run from any directory. Standard library only; does not claim to validate audio
quality, remote availability, or how GitHub renders the page.
"""
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
FILES = sorted(p for p in ROOT.rglob('*.md') if not any(x.startswith('.') for x in p.relative_to(ROOT).parts))
errors = []

def plain(text):
    return re.sub(r'```.*?```', '', text, flags=re.S)

def anchors(text):
    result = set(re.findall(r'<a\s+(?:id|name)="([^"]+)"', text))
    seen = {}
    for title in re.findall(r'^#{1,6}\s+(.+)', plain(text), re.M):
        title = re.sub(r'\[([^]]+)\]\([^)]*\)', r'\1', title)
        slug = re.sub(r'[^\w\-\s]', '', title.lower()).replace(' ', '-')
        count = seen.get(slug, 0)
        seen[slug] = count + 1
        result.add(slug + (f'-{count}' if count else ''))
    return result

for path in FILES:
    text = path.read_text()
    rel = path.relative_to(ROOT)
    if text.count('```') % 2:
        errors.append(f'{rel}: unclosed code fence')
    body = plain(text)
    targets = re.findall(r'\]\(([^)\s]+)(?:\s+"[^"]*")?\)', body)
    targets += re.findall(r'(?:href|src)="([^"]+)"', body)
    for target in targets:
        url = urlsplit(target)
        if url.scheme or url.netloc:
            continue
        dest = (path.parent / unquote(url.path)).resolve() if url.path else path
        if not dest.is_relative_to(ROOT):
            errors.append(f'{rel}: link leaves repository: {target}')
        elif not dest.exists():
            errors.append(f'{rel}: missing target: {target}')
        elif url.fragment and dest.suffix == '.md' and unquote(url.fragment) not in anchors(dest.read_text()):
            errors.append(f'{rel}: missing anchor: {target}')
    if re.search(r'!\[\]\(', body):
        errors.append(f'{rel}: image without alt text')

recipes = sorted((ROOT / 'prompts').glob('[0-9][0-9]-*.md'))
if len(recipes) != 12:
    errors.append(f'Expected 12 recipes, found {len(recipes)}')
for recipe in recipes:
    text = recipe.read_text()
    for section in ['## Paste into Style', '## Make it yours', '## Listen for', '## If it misses']:
        if section not in text:
            errors.append(f'{recipe.name}: missing {section}')
    if not ('## Paste into Lyrics' in text or '## Instrumental setup' in text):
        errors.append(f'{recipe.name}: missing input setup')
    if 'Not generation-tested' not in text:
        errors.append(f'{recipe.name}: missing test status')
    for index in [ROOT / 'prompts/README.md']:
        if recipe.name not in index.read_text():
            errors.append(f'{index.name}: recipe not discoverable: {recipe.name}')


for homepage in [ROOT / 'README.md', ROOT / 'README_ZH.md']:
    body = homepage.read_text()
    if 'prompts/README.md' not in body:
        errors.append(f'{homepage.name}: missing supplementary recipe index')
    for fragment in ['1-it-takes-another-shape', '2-what-love-can-lose', '3-morning-with-healing-hands', '4-the-secret-is-you']:
        if f'docs/listening-lab.md#{fragment}' not in body:
            errors.append(f'{homepage.name}: missing brand creation brief: {fragment}')

# All brand-supported entry languages must remain real, mutually linked pages.
home_names = ['README.md'] + [f'README_{code}.md' for code in
    ['ZH', 'TW', 'JA', 'KO', 'ID', 'IT', 'PT', 'ES', 'DE', 'RU', 'FR', 'TH', 'VI', 'AR']]
for name in home_names:
    path = ROOT / name
    if not path.exists():
        errors.append(f'Missing localized entry: {name}')
        continue
    body = path.read_text()
    languages = re.search(r'<!-- LANGUAGES:START -->(.*?)<!-- LANGUAGES:END -->', body, re.S)
    if not languages or set(re.findall(r'href="([^"]+)"', languages[1])) != set(home_names):
        errors.append(f'{name}: language navigation must link all 15 entry pages')
    gallery = re.search(r'<!-- MUSICMAKER-GALLERY:START -->(.*?)<!-- MUSICMAKER-GALLERY:END -->', body, re.S)
    rows = re.findall(r'<tr>(.*?)</tr>', gallery[1], re.S) if gallery else []
    if len(rows) != 3 or any(len(re.findall(r'<td\b', row)) != 3 for row in rows):
        errors.append(f'{name}: brand gallery must contain 3 rows of 3 cards')
    elif len(set(re.findall(r'<img src="([^"]+)"', gallery[1]))) != 9:
        errors.append(f'{name}: brand gallery needs 9 distinct covers')
    for img in re.findall(r'<img\b[^>]*>', body):
        if not re.search(r'alt="[^"\s][^"]*"', img):
            errors.append(f'{name}: image needs descriptive alt text')

if errors:
    print('\n'.join(errors))
    sys.exit(1)
print(f'PASS: {len(FILES)} Markdown files; {len(recipes)} recipes; local links, anchors, fences and recipe fields.')
