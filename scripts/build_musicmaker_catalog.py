#!/usr/bin/env python3
"""Render the complete public MusicMaker catalog from the checked source snapshot."""
from pathlib import Path
import json, html, collections, sys
P = Path(__file__).resolve().parents[1]
D = json.loads((P / 'data/musicmaker-discover.json').read_text())
records = D['tracks']
cats = {k: (v['zh'], v['en']) for k, v in D['categories'].items()}
esc = html.escape
counts=collections.Counter(t['category'] for t in records)
s='''# MusicMaker 全部试听素材 · Complete listening catalog

[← 中文首页](../README_ZH.md#想换一种风格) · [English home](../README.md#want-a-different-direction)

**148 首现有作品，来自 [MusicMaker Discover](https://musicmaker.im/discover/)。** 核对日期：2026-09-23；覆盖公开曲库当时的 10 页，包括 108 条新版记录和 40 条早期记录，不代表网站未来新增或非公开作品。

**148 existing tracks from the public Discover collection, checked September 23, 2026.** Each cover opens its original track; audio links open the source recording. Expand **Style** to read the published description where available. Published Style is not the full generation prompt or editing history.

按公开风格、标签和生日主题分组，分类用于浏览，不是平台官方分类，也不代表我们逐首试听鉴定。没有风格资料的作品单列。图片打开原作品，音频链接直接试听；展开 **Style** 可读来源风格。公开 Style 是风格字段，不等于完整生成提示词或编辑记录。歌词如有，留在原作品页，封面和音频引用原地址，不重新托管。

这些是品牌原作品，不是本仓库练习的生成结果。公开试听不等于授权复用；模型字段仅保留在[来源数据](../data/musicmaker-discover.json)中，不作为独立鉴定结论。 / Source tracks are not outputs of our exercises. Public access is not a reuse license.

## 按类型浏览 · Browse by type

'''
s+=' · '.join(f'[{zh} / {en} ({counts[k]})](#{k})' for k,(zh,en) in cats.items() if counts[k])+'\n'
for k,(zh,en) in cats.items():
 ts=[t for t in records if t['category']==k]
 if not ts:continue
 s+=f'\n<a id="{k}"></a>\n## {zh} · {en} · {len(ts)}\n\n<table>\n'
 for t in ts:
  st=esc(t['style']);style=f'<details><summary>来源风格 · Published Style</summary><p>{st}</p></details>' if st else '<small>未公开风格描述 / No published Style</small>'
  tags=', '.join(v.strip() for v in t['tags'].split(','));tagtext=esc(tags[:140]+('…' if len(tags)>140 else '')) if tags else '—'
  s+=f'<tr><td width="30%" valign="top"><a href="{t["sourceUrl"]}"><img src="{t["coverUrl"]}" width="128" height="128" alt="{esc(t["title"])} — 打开原作品 / Open source track"></a></td><td width="70%" valign="top"><a id="{t["id"]}"></a><b>{esc(t["title"])}</b><br><a href="{t["sourceUrl"]}">▶ 作品页 / Track page</a> · <a href="{t["audioUrl"]}">♫ 音频 / Audio</a><br><small>标签 / Tags: {tagtext}</small>{style}</td></tr>\n'
 s+='</table>\n'
out = P / 'docs/musicmaker-catalog.md'
if '--check' in sys.argv:
    if not out.exists() or out.read_text() != s:
        raise SystemExit('Catalog is out of date: run python3 scripts/build_musicmaker_catalog.py')
    print('PASS: complete catalog matches source snapshot')
else:
    out.write_text(s)
