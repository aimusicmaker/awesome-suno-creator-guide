#!/usr/bin/env python3
"""Render source-attributed X community cards in all desktop homepages."""
import json
import re
import sys
from pathlib import Path
from html import escape

ROOT = Path(__file__).resolve().parents[1]
data = json.loads((ROOT / 'data/x-community-examples.json').read_text())
locales = json.loads((ROOT / 'data/x-community-locales.json').read_text())
changed = []
for lang, labels in locales.items():
    path = ROOT / ('README.md' if lang == 'en' else f'README_{lang.upper()}.md')
    old = path.read_text()
    rows = []
    for start in range(0, len(data['examples']), 3):
        cards = []
        for n, item in enumerate(data['examples'][start:start + 3], start):
            title = escape(labels['titles'][n])
            url = escape(item['url'], quote=True)
            thumb = escape(item['thumbnail'], quote=True)
            status = labels['published'] if item['prompt'] else labels['workflow']
            detail = f"docs/x-community-examples.md#case-{item['id']}"
            cards.append(f'<td width="33%" align="center" valign="top"><a href="{url}"><img src="{thumb}" width="1200" alt="{title} — @{item["author"]} — {escape(labels["alt"], quote=True)}"></a><br><b>{title}</b><br><sub><a href="{url}">@{item["author"]}</a> · {item["date"]}</sub><br><sub>{escape(status)}</sub><br><a href="{url}">▶ {escape(labels["watch"])}</a> · <a href="{detail}">{escape(labels["notes"])} →</a></td>')
        rows.append('<tr>\n' + '\n'.join(cards) + '\n</tr>')
    block = '<!-- COMMUNITY-CASES:START -->\n' + labels['intro'] + '\n\n<table width="100%">\n' + '\n'.join(rows) + '\n</table>\n<!-- COMMUNITY-CASES:END -->'
    if '<!-- COMMUNITY-CASES:START -->' in old:
        new = re.sub(r'<!-- COMMUNITY-CASES:START -->.*?<!-- COMMUNITY-CASES:END -->', lambda _: block, old, flags=re.S)
    else:
        # Replace the old section introduction and nine brand briefs together.
        a = old.index('<!-- CREATION-BRIEFS:START -->')
        heading = old.rfind('\n## ', 0, a)
        body_start = old.index('\n', heading + 1)
        b = old.index('<!-- CREATION-BRIEFS:END -->', a) + len('<!-- CREATION-BRIEFS:END -->')
        new = old[:body_start] + '\n\n' + block + old[b:]
    if new != old:
        changed.append(path.name)
        if '--check' not in sys.argv:
            path.write_text(new)
if '--check' in sys.argv and changed:
    raise SystemExit('Stale community cards: ' + ', '.join(changed))
print('PASS: community cards match source records and locale text' if '--check' in sys.argv else f'Updated {len(changed)} community grids')
