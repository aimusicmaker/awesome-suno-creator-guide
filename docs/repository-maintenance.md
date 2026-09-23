# Repository settings and maintenance

[← Home](../README.md) · [Contributing](../CONTRIBUTING.md) · [Editorial policy](editorial-policy.md)

## Discovery settings

The intended settings are stored in [repository-settings.json](../data/repository-settings.json):

- **Description:** A visual Suno music-making guide with prompts, creator examples, step-by-step workflows, and troubleshooting. Maintained by MusicMaker.
- **Website:** https://musicmaker.im/
- **Topics:** suno, ai-music, music-production, songwriting, music-prompts, musicmaker

An account allowed to edit repository settings can apply the description, website and topics with:

```sh
gh repo edit aimusicmaker/awesome-suno-creator-guide \
  --description 'A visual Suno music-making guide with prompts, creator examples, step-by-step workflows, and troubleshooting. Maintained by MusicMaker.' \
  --homepage 'https://musicmaker.im/' \
  --add-topic suno --add-topic ai-music --add-topic music-production \
  --add-topic songwriting --add-topic music-prompts --add-topic musicmaker
```

Verify the saved values with `gh repo view --json description,homepageUrl,repositoryTopics`.

For the share card, open [repository settings](https://github.com/aimusicmaker/awesome-suno-creator-guide/settings), find **Social preview**, and upload [social-preview.jpg](../assets/social-preview.jpg). This 1280 × 640 JPEG is below 1 MB. Changing the README cover does not change this setting.

These are target settings, not evidence that an administrator has applied them. Confirm the repository About panel and public sharing metadata after saving.

## Content maintenance

Keep first-song and troubleshooting links near the top of each language page. Group publishing relationships, check dates, test-status notes and general limitations in the final Notes and sources section. Keep source links, prerequisites that affect the task, and practical instructions alongside the relevant content. The desktop README is the maintained source for its mobile counterpart. Preserve image descriptions, source links and the distinction between official guidance, community examples and tested exercises.

Update dates only when the relevant claims have been rechecked. Use [source notes](sources.md) for evidence and [editorial policy](editorial-policy.md) for responsibility. Run the four checks in [CONTRIBUTING.md](../CONTRIBUTING.md) and inspect visual changes on GitHub.

## Search and sharing

GitHub controls the HTML document head for repository pages. Do not add SEO meta tags, canonical tags or structured-data scripts to README Markdown and expect them to configure GitHub search metadata.

If this guide later gets a separate brand-site edition, decide its URL and update workflow first. That website can manage page titles, language annotations and preferred URLs at the site level. Keep the GitHub desktop/mobile entries for their reader use; their existence alone is not evidence of additional search traffic.

Relevant official guidance:

- [GitHub README contents and relative links](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes)
- [GitHub repository topics](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/classifying-your-repository-with-topics)
- [GitHub social preview dimensions](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/customizing-your-repositorys-social-media-preview)
- [GitHub community profiles](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/about-community-profiles-for-public-repositories)
- [Google helpful content and E-E-A-T](https://developers.google.com/search/docs/fundamentals/creating-helpful-content)
- [Google image guidance](https://developers.google.com/search/docs/appearance/google-images)
- [Google multilingual site guidance](https://developers.google.com/search/docs/specialty/international/managing-multi-regional-sites)
