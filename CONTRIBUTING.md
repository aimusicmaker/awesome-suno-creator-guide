# Share something another creator can use

[← Home](README.md) · [Get help](SUPPORT.md) · [Code of conduct](CODE_OF_CONDUCT.md) · [Editorial policy](docs/editorial-policy.md)

Use the [creation-case form](https://github.com/aimusicmaker/awesome-suno-creator-guide/issues/new?template=creation-case.yml) or [correction form](https://github.com/aimusicmaker/awesome-suno-creator-guide/issues/new?template=content-correction.yml), or open a pull request with a focused improvement. A small, reproducible improvement is enough.

For a recipe, include:

- A concrete use case and genre.
- Separate Style and Lyrics blocks, or an instrumental setup.
- Original lyrics or clear permission to reuse them.
- The model, date, controls, and what you actually tested.
- One useful variation and an audible quality check.
- A public output link only if you have permission to share it.

Label untested prompts as untested. Do not present a reference song as your generated result. Give the original author and source when discussing someone else's method; do not copy their lyrics or media into this repository without permission.

The original repository text and code use the existing MIT license. Linked third-party recordings and cover art retain their own rights; see [media notes](assets/README.md).

Before submitting, regenerate community cards with `python3 scripts/build_community_cards.py` if their data or localized labels changed, then run `python3 scripts/build_mobile_readmes.py` after any homepage edit. From the repository root, run:

```sh
python3 scripts/check_content.py
python3 scripts/build_musicmaker_catalog.py --check
python3 scripts/build_community_cards.py --check
python3 scripts/build_mobile_readmes.py --check
```

Preview Markdown tables, image links, and collapsed sections on GitHub. No account credentials or private receipts belong in a contribution.

Maintainers: see [repository settings and maintenance](docs/repository-maintenance.md) for discovery metadata, the social preview and update conventions.
