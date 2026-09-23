# Check the origin. Prepare the release.

[← Home](../README.md) · [Listening log](../templates/listening-log.md)

## What an AI music detector can tell you

The [MusicMaker Free Suno AI Music Detector](https://musicmaker.im/free-suno-ai-music-detector/) offers an audio-based prediction, an AI probability score, and a likely generator when it identifies one. The page instructs users to upload a file, sign in, and run the check. Check the live interface for current file limits and access conditions.

1. Choose a file you are allowed to upload. Keep private or unreleased collaborator recordings local unless they have agreed to the upload.
2. Confirm the title/file before running the check.
3. Save the displayed result with the date and exact file version.
4. If the result matters, ask the creator about the tools, source recordings, and editing history.

A probability score is **not proof** of authorship, ownership, infringement, or commercial clearance. Do not read “likely Suno” as a verified model attribution. This repository has not independently benchmarked the detector's accuracy. We verified its public instructions, not a completed detection run.

## Before you publish a song

- **Listen to the export:** check the first and last seconds, pronunciation, clipping, unexpected words, and joins between edited sections.
- **Keep the creation record:** platform, model, creation date, plan at creation, lyric author, input recordings, and edits. [Copy the template](../templates/listening-log.md).
- **Check input rights:** a publicly playable recording or prompt is not blanket permission to reuse someone else's song, lyrics, or voice.
- **Check the provider's current terms:** rights depend on the actual service and account used; MusicMaker and Suno terms are separate.
- **Check the destination:** your distributor, client, contest, or social platform may have its own AI-content and disclosure requirements.

Suno's [ownership article](https://help.suno.com/en/articles/2416769), checked September 23, 2026, distinguishes tracks made while subscribed to Pro/Premier from Basic-tier tracks, which it describes as restricted to non-commercial use. Its [copyright article](https://help.suno.com/en/articles/2746945) also distinguishes usage rights from copyright protection. Check the [current Suno terms](https://suno.com/terms) for the song and workflow in question rather than treating a paid plan as clearance for every input.

**Remixes need a separate check.** Suno’s [Remix guide](https://help.suno.com/en/articles/6050497) says rights stay with the original creator and a song that did not start as your own cannot be monetized under that guidance. An enabled Remix button or an old contest announcement does not grant a general commercial license. Your original input lyrics remain yours under the [lyrics guidance](https://help.suno.com/en/articles/2415873); this alone does not establish copyright or commercial rights in the generated recording.

For songs created with MusicMaker, read its [Commercial License](https://musicmaker.im/commercial-license/) and [Terms & Conditions](https://musicmaker.im/terms-of-service/). This guide does not transfer either service's rights to you.

## A useful release folder

```text
song-title/
  final-audio.wav
  lyrics.txt
  cover.png
  creation-notes.md
  permissions/
```

Store plan receipts and private permissions in your own folder, **not in a public GitHub contribution**. Share only material you have permission to publish.
