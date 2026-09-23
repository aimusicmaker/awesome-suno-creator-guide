<div align="center">

# Suno 音乐创作指南

**做一首自己还想再听的歌。**

可直接复制的提示词、原创歌词、真实试听参考，以及常见问题的修改办法。

[English](README.md) · 简体中文

![Suno 创作指南封面：米白底色与橙色黑胶唱片，主题是创作下一首自己喜欢的歌。](assets/creator-guide-cover.png)

**[挑选提示词](prompts/README.md) · [开始第一首歌](#开始第一首歌) · [解决问题](#生成结果不对怎么办) · [去品牌曲库试听](https://musicmaker.im/discover/)**

</div>

适合第一次写歌的人、需要视频配乐的创作者，以及“脑中有声音，却总生成不出来”的音乐爱好者。这里有 **12 份原创方案**，分别写清风格填在哪里、歌词怎么填、下一次改什么、生成后听什么。

本仓库由 **[AI Music Maker](https://musicmaker.im/)** 维护，是独立创作指南，并非 Suno 官方文档。提示词尚未逐条生成验证；下面的品牌歌曲是独立试听参考，不是这些提示词的生成结果。详细教程和大部分方案目前为英文，本页提供中文入门说明和中文歌曲示例。

## 先选你要做的内容

| 你想做什么 | 从哪里开始 |
|:--|:--|
| 做第一首有主歌和副歌的歌曲 | [独立流行：Last Train Home](prompts/01-last-train-home.md) |
| 给学习、播客或旅行视频配乐 | [4 份纯音乐方案](prompts/README.md#instrumentals) |
| 写一首中文歌 | [站台的雨](prompts/08-rain-at-the-station.md) |
| 给朋友做生日礼物 | [生日歌曲](prompts/07-birthday-table.md) |
| 处理唱字太赶、声音太挤等问题 | [本页问题速查](#生成结果不对怎么办) |
| 把歌曲做成社媒短片 | [公开案例与创作练习（英文）](docs/community-playbook.md) |
| 了解一段音乐是否可能由 AI 生成 | [本页检测说明](#分享前先检查) |

## 先听，再写

以下三首歌曲来自 [MusicMaker Discover](https://musicmaker.im/discover/)。点击封面打开单曲页，再按播放按钮。这是一组跨模型的品牌作品：Island Sunshine 页面标注 Mureka V9.5，Morning with Healing Hands 标注 V6.0；这是页面信息，不是本仓库对模型的独立认证。

<table>
<tr><td width="30%"><a href="https://musicmaker.im/detail/discover-v2-94/"><img src="https://cdn.musicmaker.im/musicmaker/discover_v2/neon_pulse.webp" alt="Neon Pulse" width="150"></a></td><td><b>Neon Pulse</b><br>02:53 · 品牌作品<br><a href="https://musicmaker.im/detail/discover-v2-94/">▶ 打开单曲</a> · <a href="https://cdn.musicmaker.im/musicmaker/discover_v2/neon_pulse.mp3">直接听音频</a></td></tr>
<tr><td width="30%"><a href="https://musicmaker.im/detail/discover-v2-106/"><img src="https://cdn.musicmaker.im/musicmaker/discover_v2/morning_with_healing_hands.webp" alt="Morning with Healing Hands" width="150"></a></td><td><b>Morning with Healing Hands</b><br>03:33 · 木吉他风格<br><a href="https://musicmaker.im/detail/discover-v2-106/">▶ 打开单曲</a> · <a href="https://cdn.musicmaker.im/musicmaker/discover_v2/morning_with_healing_hands.mp3">直接听音频</a></td></tr>
<tr><td width="30%"><a href="https://musicmaker.im/detail/discover-v2-101/"><img src="https://cdn.musicmaker.im/musicmaker/discover_v2/island_sunshine.webp" alt="Island Sunshine" width="150"></a></td><td><b>Island Sunshine</b><br>03:51 · Mureka V9.5<br><a href="https://musicmaker.im/detail/discover-v2-101/">▶ 打开单曲</a> · <a href="https://cdn.musicmaker.im/musicmaker/discover_v2/island_sunshine.mp3">直接听音频</a></td></tr>
</table>

**一个小练习：**选一首，记下最先留下印象的声音、情绪发生变化的位置，以及是谁在带动旋律。借鉴这些声音特点，重新写自己的故事、旋律和歌词。[素材来源说明（英文）→](docs/sources.md)

## 开始第一首歌

不用下载仓库，也不用安装软件。

1. 打开 [Suno Create](https://suno.com/create)，选择 **Custom（自定义）**。也可在 [MusicMaker 歌曲生成器](https://musicmaker.im/ai-song-generator/)尝试同一份创作想法；两者的模型和控件可能不同。
2. 将第一段填入 **Style / Style of Music（音乐风格）**，第二段填入 **Lyrics（歌词）**。有歌词的歌曲需关闭 **Instrumental（纯音乐）**。
3. 在自己的可用额度内生成，先听完备选结果，再决定改什么。
4. 保留较好的版本；下一次只改一个因素，例如主乐器、演唱方式或歌词长度。

**歌名：站台的雨。音乐风格栏：**

```text
Mandarin acoustic pop ballad, gentle piano and warm fingerpicked guitar.
Clear natural Mandarin lead vocal, short syllabic phrases, restrained emotion.
Sparse verse, chorus adds soft bass and brushed drums.
Small instrumental outro.
```

这段要求的是：中文抒情流行，钢琴和指弹吉他，咬字清晰，主歌简单，副歌再加入贝斯和轻鼓。

**歌词栏：**以下为本仓库新写的短歌词。

```text
[Verse]
你把伞靠在窗边
说雨停了就再见
站台亮起一排灯
我还留着那张票

[Chorus]
雨慢慢落 车慢慢走
没说的话 留在路口
下一站若 天气晴朗
记得把伞 带在身旁

[Outro]
记得把伞 带在身旁
```

`[Verse]` 是主歌，`[Chorus]` 是副歌，`[Outro]` 是结尾。这些标签用于提示歌曲结构，不保证模型严格照做。

**生成后先听：**“站台”“那张票”是否唱清楚？副歌是否比主歌更饱满？如果唱得赶，先减字或改断句。[查看完整方案 →](prompts/08-rain-at-the-station.md)

## 12 份方案，按用途挑

| 用途 | 方案 |
|:--|:--|
| 怀旧流行 | [Last Train Home](prompts/01-last-train-home.md) |
| 温暖民谣 | [Kitchen Light](prompts/02-kitchen-light.md) |
| 深夜倾诉 | [Blue Receipt](prompts/03-blue-receipt.md) |
| 轻快舞曲 | [Weekend Platform](prompts/04-weekend-platform.md) |
| 有冲劲的流行朋克 | [Paper Crown](prompts/05-paper-crown.md) |
| 公路乡村歌曲 | [Mile Marker](prompts/06-mile-marker.md) |
| 生日礼物 | [Birthday Table](prompts/07-birthday-table.md) |
| 中文抒情 | [站台的雨](prompts/08-rain-at-the-station.md) |
| 学习背景音乐 | [Window Seat](prompts/09-window-seat.md) |
| 夜间行车配乐 | [After Hours](prompts/10-after-hours.md) |
| 播客和旁白底乐 | [Small Victories](prompts/11-small-victories.md) |
| 旅行风景配乐 | [Open Horizon](prompts/12-open-horizon.md) |

纯音乐方案需打开 Instrumental，并清空歌词栏。英文方案内的提示词可直接复制；不要把解释文字一起粘进去。

## 生成结果不对，怎么办？

| 问题 | 先试这一项 |
|:--|:--|
| 把要求也唱出来了 | 将说明移到风格栏，歌词栏只留歌词和简单分段 |
| 唱字太赶 | 缩短最长的一行，先别添加更多指令 |
| 副歌没有变化 | 让主歌少一件乐器，副歌再加回来 |
| 声音太挤 | 删掉互相冲突的曲风，只留两件主要乐器 |
| 纯音乐出现人声 | 确认纯音乐已开启、歌词已清空，再重新生成 |
| 开头太长 | 为短视频直接剪取副歌；提示词不能精确控制秒数 |
| 结尾突然截断 | 尝试明确要求自然收尾，或在编辑器中选合适位置淡出 |
| 配乐盖住旁白 | 先调低配乐音量，再考虑减少配器 |

每次只改一项，并记录原提示词、模型和结果。不需要为了一个不明显的问题无限重新生成。[详细排查（英文）→](docs/troubleshooting.md)

## 看看创作者怎样使用这些工具

| 创作者 | 作品与访谈 | 可以借鉴的做法 |
|:--|:--|:--|
| Dream Relic | [试听 Seven-Eleven Halo](https://suno.com/embed/2e6b6eb7-9421-4c10-bdab-ba70252ae152) · [访谈](https://suno.com/blog/dream-relic) | 先确定画面的情绪，再寻找匹配的声音 |
| Matt Steffanina | [试听 The Sound](https://suno.com/embed/336c6b25-0b32-438c-8857-0a46679ffc13) · [访谈](https://suno.com/blog/matt-steffanina) | 围绕舞蹈和动作创作音乐 |
| sad alex | [访谈与内嵌作品](https://suno.com/blog/sad-alex) | 用不同编曲发展已有歌曲想法，自己决定保留什么 |

[Dream Relic《Seven Eleven Halo》YouTube 发布页](https://www.youtube.com/watch?v=A0jr0cN3vKw) · [看 Reddit 混音活动原帖](https://www.reddit.com/r/SunoAI/comments/1txu83c/dream_relic_x_suno_remix_contest/)（2026 年 6 月历史活动，非当前征集）。

以上为 Suno 发布的创作者访谈，作品不是本仓库提示词的生成结果。借鉴的是创作方法，不是照搬他们的歌词或声音。[案例拆解与练习（英文）→](docs/community-playbook.md)

## 分享前，先检查

听一遍最终导出的文件，确认开头、结尾、咬字和剪接没有明显问题。核对歌词、上传录音和人声的使用权限，再查看实际生成平台及套餐的现行条款。公开可听不等于可以直接拿来商用。

想了解歌曲可能的来源，可使用 MusicMaker 的 **[Free Suno AI Music Detector](https://musicmaker.im/free-suno-ai-music-detector/)**。它提供预测、AI 概率分数，以及识别到的可能生成工具；页面说明运行检测需要登录。**检测分数不是作者身份、版权或商用许可的证明。** 本仓库没有独立测评其准确率。[检测与发布说明（英文）→](docs/detector-and-release.md)

## 和 MusicMaker 一起继续创作

去 [Discover](https://musicmaker.im/discover/)寻找声音灵感，在[歌曲生成器](https://musicmaker.im/ai-song-generator/)尝试自己的版本，再用这里的指南逐步修改。

欢迎[提交实用提示词、失败例子或纠错](CONTRIBUTING.md)，请写明模型、设置和实际测试情况，并只分享有权公开的素材。

[素材和来源（英文）](docs/sources.md) · [MIT 许可证](LICENSE) · [媒体素材权利说明（英文）](assets/README.md)
