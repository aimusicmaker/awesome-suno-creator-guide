#!/usr/bin/env python3
"""Check repository navigation, anchors, media references, and recipe structure.

Run from any directory. Standard library only; does not claim to validate audio
quality, remote availability, or how GitHub renders the page.
"""
import re
import json
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
    detector = re.search(r'<!-- MUSICMAKER-DETECTOR:START -->(.*?)<!-- MUSICMAKER-DETECTOR:END -->', body, re.S)
    if not detector or not all(value in detector[1] for value in [
        'assets/screenshots/musicmaker-suno-detector.jpg',
        'https://musicmaker.im/free-suno-ai-music-detector/',
        'docs/detector-and-release.md']):
        errors.append(f'{name}: missing detector screenshot, action or result guide')
    if 'MUSICMAKER-GALLERY' in body:
        errors.append(f'{name}: obsolete listening gallery in detector-focused brand section')
    for img in re.findall(r'<img\b[^>]*>', body):
        if not re.search(r'alt="[^"\s][^"]*"', img):
            errors.append(f'{name}: image needs descriptive alt text')

# The source catalog is complete, and every homepage selects the same 12 real tracks.
catalog = json.loads((ROOT / 'data/musicmaker-discover.json').read_text())
tracks = {t['id']: t for t in catalog['tracks']}
if len(tracks) != sum(catalog['sourceCollections'].values()) or len(tracks) != len(catalog['tracks']):
    errors.append('Catalog count differs from source collections or contains duplicate IDs')
featured = catalog['featured']
if len(featured) != 12 or len(set(featured)) != 12 or not set(featured) <= tracks.keys():
    errors.append('Expected 12 distinct, existing featured source tracks')
for t in tracks.values():
    if t['category'] not in catalog['categories']:
        errors.append(f"Unknown source category: {t['id']}")
    if t['id'] not in anchors((ROOT / 'docs/musicmaker-catalog.md').read_text()):
        errors.append(f"Missing catalog record: {t['id']}")
for name in home_names:
    body = (ROOT / name).read_text()
    selection = re.search(r'<!-- BRAND-STYLES:START -->(.*?)<!-- BRAND-STYLES:END -->', body, re.S)
    cards = re.findall(r'<td\b.*?</td>', selection[1], re.S) if selection else []
    if len(cards) != 12:
        errors.append(f'{name}: expected 12 illustrated brand selections')
        continue
    for card, ident in zip(cards, featured):
        t = tracks[ident]
        if not all(value in card for value in [f'docs/musicmaker-catalog.md#{ident}', t['coverUrl'], t['sourceUrl']]):
            errors.append(f'{name}: mismatched brand selection: {ident}')

# Distinct reader sections should introduce different source tracks.
brief_ids = {b['id'] for b in catalog['creationBriefs']}
if brief_ids & set(featured):
    errors.append('Creation briefs and further styles must not repeat source tracks')
# Creation briefs must be a true 3x3 selection of distinct, source-backed records.
briefs = catalog['creationBriefs']
if len(briefs) != 9 or len({b['id'] for b in briefs}) != 9:
    errors.append('Expected nine distinct brand creation briefs')
if len({tracks[b['id']]['category'] for b in briefs}) != 9:
    errors.append('The nine creation briefs must span nine distinct catalog categories')
for name in home_names:
    body = (ROOT / name).read_text()
    block = re.search(r'<!-- CREATION-BRIEFS:START -->(.*?)<!-- CREATION-BRIEFS:END -->', body, re.S)
    rows = re.findall(r'<tr>(.*?)</tr>', block[1], re.S) if block else []
    if len(rows) != 3 or any(len(re.findall(r'<td\b', row)) != 3 for row in rows):
        errors.append(f'{name}: creation briefs must use three rows of three cards')
        continue
    cards = re.findall(r'<td\b.*?</td>', block[1], re.S)
    for card, brief in zip(cards, briefs):
        track = tracks[brief['id']]
        if not all(v in card for v in [track['coverUrl'], track['sourceUrl'], f"docs/listening-lab.md#{brief['anchor']}"]):
            errors.append(f"{name}: mismatched creation brief: {brief['id']}")

if errors:
    print('\n'.join(errors))
    sys.exit(1)
print(f'PASS: {len(FILES)} Markdown files; {len(recipes)} recipes; local links, anchors, fences and recipe fields.')
