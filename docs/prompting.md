# Write a prompt you can revise

[← Home](../README.md) · [Recipes](../prompts/README.md)

Start with a sound you can describe in one sentence. Add detail only when you can hear what is missing.

For a single creative brief, v6 Simple can handle complex instructions and multiple input types. The table below is specifically for the **Custom** workflow used by our recipes. [Official v6 guidance and editing examples](official-suno-guide.md).

## Choose a creation tool

Use [Suno Create](https://suno.com/create) or [MusicMaker’s song generator](https://musicmaker.im/ai-song-generator/) for these recipes. Both offer a Custom route for separate style and lyric inputs. For an idea without prepared lyrics, Suno uses Simple; MusicMaker uses Basic with a Description field.

| Recipe block | Suno Custom | MusicMaker Custom |
|:--|:--|:--|
| Style | Styles / Style of Music | Music Style |
| Lyrics | Lyrics | Lyrics |
| Song name | Title | Music Title |
| Music without vocals | Instrumental on; Lyrics empty | Instrumental on; Lyrics empty |

MusicMaker’s fields were inspected with Music 6.0 selected on September 23, 2026; other model choices may change the controls. Check the model, credits and sharing settings before generating. Accounts, credits and rights are separate between services. These recipes have not been generation-tested on either service.

## Put each instruction in the right place

| Field | Put here | Avoid |
|:--|:--|:--|
| Style / Style of Music | Genre, instruments, vocal delivery, mood, broad arrangement | Full lyrics or contradictory lists of genres |
| Lyrics | Words to sing, with simple section labels | Paragraphs of production instructions that might get sung |
| Title | A short name to find the take again | Treating a title as an arrangement control |
| Instrumental | On for music without sung words; Lyrics empty | Pasting a vocal song while expecting no voice |

Suno's [Custom-mode guidance](https://help.suno.com/en/articles/2415873) confirms the separate space for your own lyrics. Other platforms may use different labels. Check your chosen interface before pasting.

## A useful starting sentence

```text
[Genre] with [two main instruments], [pace and mood].
[Vocal character, or instrumental].
[One change between the verse and chorus].
```

For example, replace “beautiful emotional song” with this original brief:

```text
Slow acoustic folk with fingerpicked guitar and upright bass.
Close conversational lead vocal. The chorus adds soft harmonies;
the last line returns to voice and guitar.
```

The second brief gives you specific things to listen for. It does not guarantee them.

## Revise in small steps

1. Keep the lyrics and selected model the same within your chosen service (for Suno, keep the same v6 variant).
2. Name the problem: “the vocal is buried,” not “it sounds wrong.”
3. Change one instruction: replace a dense synth layer with sparse piano.
4. Compare similar passages at similar playback volume. A louder take can seem better just because it is louder.
5. Stop when the song serves its purpose, or when your chosen credit budget is reached. Keep a usable take rather than rerolling indefinitely.

If your interface offers exclusions or other advanced controls, use their dedicated fields. Availability and labels depend on the model and plan. Avoid copying somebody else's slider settings as a universal recipe.

## What words cannot guarantee

Exact BPM, key, bar counts, silence, voice identity, and second-by-second timing are not guaranteed by prose. A section tag is not a programming command. For a 15-second clip, generate a usable passage and trim it in an audio/video editor; do not rely on “exactly 15 seconds” in the style field.

Use musical characteristics such as “warm low voice, restrained vibrato” to describe a vocal. Upload reference audio only when you have permission to use it. The [release guide](detector-and-release.md) separates creation settings, rights, and detection.

**Next:** [Lyrics and structure](lyrics-and-structure.md) · [Troubleshooting](troubleshooting.md)
