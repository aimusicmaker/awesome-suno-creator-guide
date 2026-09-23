<div align="center">

# Suno 音楽制作ガイド：プロンプト・実例・入門

**ひとつのアイデアから、いろいろな音楽へ。**

フォーク、ダンス、ジャズ、アニメや短編映画の音楽も。Suno に作りたい曲を伝え、できた曲を聴いて、気に入った部分を磨いていきましょう。

<!-- LANGUAGES:START -->
<p align="center">
<a href="README.md"><img src="assets/ui/lang-en.svg" height="32" alt="English"></a>
<a href="README_ZH.md"><img src="assets/ui/lang-zh.svg" height="32" alt="简体中文"></a>
<a href="README_TW.md"><img src="assets/ui/lang-tw.svg" height="32" alt="繁體中文"></a>
<a href="README_JA.md" aria-current="page"><img src="assets/ui/lang-ja-active.svg" height="32" alt="日本語 — 現在の言語"></a>
<a href="README_KO.md"><img src="assets/ui/lang-ko.svg" height="32" alt="한국어"></a>
<a href="README_ID.md"><img src="assets/ui/lang-id.svg" height="32" alt="Bahasa Indonesia"></a>
<a href="README_IT.md"><img src="assets/ui/lang-it.svg" height="32" alt="Italiano"></a>
<a href="README_PT.md"><img src="assets/ui/lang-pt.svg" height="32" alt="Português"></a>
<a href="README_ES.md"><img src="assets/ui/lang-es.svg" height="32" alt="Español"></a>
<a href="README_DE.md"><img src="assets/ui/lang-de.svg" height="32" alt="Deutsch"></a>
<a href="README_RU.md"><img src="assets/ui/lang-ru.svg" height="32" alt="Русский"></a>
<a href="README_FR.md"><img src="assets/ui/lang-fr.svg" height="32" alt="Français"></a>
<a href="README_TH.md"><img src="assets/ui/lang-th.svg" height="32" alt="ไทย"></a>
<a href="README_VI.md"><img src="assets/ui/lang-vi.svg" height="32" alt="Tiếng Việt"></a>
<a href="README_AR.md"><img src="assets/ui/lang-ar.svg" height="32" alt="العربية"></a>
</p>
<!-- LANGUAGES:END -->

<!-- DEVICE-VIEW:START -->
<p align="center"><a href="mobile/README_JA.md"><img src="assets/ui/mobile-ja.svg" height="40" alt="モバイル版"></a></p>
<!-- DEVICE-VIEW:END -->

<a href="https://help.suno.com/en/articles/13924481"><img src="assets/creator-guide-cover.jpg" width="960" alt="ピアノ、ジャズ、ギター、ダンス、アニメのコラージュ。伝える、作る、磨く。Suno 公式 v6 FAQ を開く。"></a>

<p><a href="#official"><img src="assets/ui/official-ja.svg" height="32" alt="公式情報"></a> <a href="#examples"><img src="assets/ui/cases-ja.svg" height="32" alt="X の実例"></a> <a href="#briefs"><img src="assets/ui/briefs-ja.svg" height="32" alt="制作案を選ぶ"></a></p>
<p align="center"><a href="#start"><strong>▶ 最初の曲を作る</strong></a> · <a href="docs/troubleshooting.md">生成の問題を解決する · 英語</a></p>
</div>

このガイドは [MusicMaker](https://github.com/aimusicmaker) が公開・管理しています。紹介している MusicMaker のツールも同ブランドが運営しています。詳しい解説と練習ページは英語です。 [運営と編集方針 · 英語](docs/editorial-policy.md)。

<a id="official"></a>
## Suno v6 でできること

言葉、写真、動画、ハミングを音楽の出発点にできます。Simple はアイデアから、Custom は歌詞と曲調を分けて指定する場合に使います。

[![Suno v6 でできること](assets/suno-workflow.svg)](https://help.suno.com/en/articles/13924481)

v6-mini は全プラン、v6 と v6-wild は Pro / Premier 向けです。指定した秒数や旋律が毎回そのまま再現される保証はありません。生成後に聴いて確認しましょう。

[公式情報 ↗](https://help.suno.com/en/articles/13924481) · [Suno v6 ↗](https://help.suno.com/en/articles/13924801)

<sub>モデル情報の確認日 2026-09-23。</sub>

<a id="examples"></a>
## X の公式プロンプト例

画像をクリックすると Suno の元投稿が開きます。カードでは要点を簡潔に紹介します。

<table>
<tr>
<td width="50%" valign="top"><a href="https://x.com/suno/status/2098504030204973500"><img src="assets/x-cases/rooftop.svg" width="440" alt="情景から始める — Suno / X"></a><br><a href="https://x.com/suno/status/2098504030204973500"><b>情景から始める ↗</b></a></td>
<td width="50%" valign="top"><a href="https://x.com/suno/status/2098504032079814672"><img src="assets/x-cases/input.svg" width="440" alt="写真やハミングを使う — Suno / X"></a><br><a href="https://x.com/suno/status/2098504032079814672"><b>写真やハミングを使う ↗</b></a></td>
</tr>
<tr>
<td width="50%" valign="top"><a href="https://x.com/suno/status/2098504033698812198"><img src="assets/x-cases/edit.svg" width="440" alt="一か所だけ変える — Suno / X"></a><br><a href="https://x.com/suno/status/2098504033698812198"><b>一か所だけ変える ↗</b></a></td>
<td width="50%" valign="top"><a href="https://x.com/suno/status/2098504035292618787"><img src="assets/x-cases/arc.svg" width="440" alt="感情の変化を伝える — Suno / X"></a><br><a href="https://x.com/suno/status/2098504035292618787"><b>感情の変化を伝える ↗</b></a></td>
</tr>
</table>

<a id="briefs"></a>
## 作品を聴いて制作の方向を選ぶ

<!-- COMMUNITY-CASES:START -->
X コミュニティの9つの事例から方向性を選べます。画像をクリックすると元投稿が開き、解説では公開プロンプトと制作方法を紹介します。

<table width="100%">
<tr>
<td width="33%" align="center" valign="top"><a href="https://x.com/maxescu/status/2049444543360336167"><img src="https://pbs.twimg.com/amplify_video_thumb/2049444325596286976/img/lqCxWmk86QgVYb-a.jpg" width="1200" alt="Tech house：短いプロンプトとカスタムモデル — @maxescu — 元投稿の関連画像。クリックして X の投稿を開く"></a><br><b>Tech house：短いプロンプトとカスタムモデル</b><br><sub><a href="https://x.com/maxescu/status/2049444543360336167">@maxescu</a> · 2026-04-29</sub><br><sub>公開音楽プロンプト</sub><br><a href="https://x.com/maxescu/status/2049444543360336167">▶ X の元投稿</a> · <a href="docs/x-community-examples.md#case-2049444543360336167">解説 · 英語 →</a></td>
<td width="33%" align="center" valign="top"><a href="https://x.com/KiwiJazzTutor/status/2069599574000586959"><img src="https://pbs.twimg.com/amplify_video_thumb/2069594596422672384/img/F5ujZhXCu71zlQcd.jpg" width="1200" alt="ピアノとラテンジャズ — @KiwiJazzTutor — 元投稿の関連画像。クリックして X の投稿を開く"></a><br><b>ピアノとラテンジャズ</b><br><sub><a href="https://x.com/KiwiJazzTutor/status/2069599574000586959">@KiwiJazzTutor</a> · 2026-06-24</sub><br><sub>制作過程 / 完成作品</sub><br><a href="https://x.com/KiwiJazzTutor/status/2069599574000586959">▶ X の元投稿</a> · <a href="docs/x-community-examples.md#case-2069599574000586959">解説 · 英語 →</a></td>
<td width="33%" align="center" valign="top"><a href="https://x.com/Framer_X/status/2093001366922744183"><img src="https://pbs.twimg.com/amplify_video_thumb/2092980107551858688/img/anFYID4N5V4X_n1y.jpg" width="1200" alt="曲にアニメ映像を付ける — @Framer_X — 元投稿の関連画像。クリックして X の投稿を開く"></a><br><b>曲にアニメ映像を付ける</b><br><sub><a href="https://x.com/Framer_X/status/2093001366922744183">@Framer_X</a> · 2026-08-27</sub><br><sub>制作過程 / 完成作品</sub><br><a href="https://x.com/Framer_X/status/2093001366922744183">▶ X の元投稿</a> · <a href="docs/x-community-examples.md#case-2093001366922744183">解説 · 英語 →</a></td>
</tr>
<tr>
<td width="33%" align="center" valign="top"><a href="https://x.com/juliewdesign_/status/1928099450884333867"><img src="https://pbs.twimg.com/amplify_video_thumb/1928098998537076736/img/lz34BDEJjqLEvQy_.jpg" width="1200" alt="日常の映像に曲を合わせる — @juliewdesign_ — 元投稿の関連画像。クリックして X の投稿を開く"></a><br><b>日常の映像に曲を合わせる</b><br><sub><a href="https://x.com/juliewdesign_/status/1928099450884333867">@juliewdesign_</a> · 2025-05-29</sub><br><sub>制作過程 / 完成作品</sub><br><a href="https://x.com/juliewdesign_/status/1928099450884333867">▶ X の元投稿</a> · <a href="docs/x-community-examples.md#case-1928099450884333867">解説 · 英語 →</a></td>
<td width="33%" align="center" valign="top"><a href="https://x.com/HashemGhaili/status/1929615615133966391"><img src="https://pbs.twimg.com/amplify_video_thumb/1929614716961247232/img/mfhSRJTv-wh7OvDx.jpg" width="1200" alt="SF短編の音楽を作る — @HashemGhaili — 元投稿の関連画像。クリックして X の投稿を開く"></a><br><b>SF短編の音楽を作る</b><br><sub><a href="https://x.com/HashemGhaili/status/1929615615133966391">@HashemGhaili</a> · 2025-06-02</sub><br><sub>制作過程 / 完成作品</sub><br><a href="https://x.com/HashemGhaili/status/1929615615133966391">▶ X の元投稿</a> · <a href="docs/x-community-examples.md#case-1929615615133966391">解説 · 英語 →</a></td>
<td width="33%" align="center" valign="top"><a href="https://x.com/demon_ai_/status/1797764913198154072"><img src="https://pbs.twimg.com/ext_tw_video_thumb/1797763815158784001/pu/img/lcMHsbRBHK8hmv0J.jpg" width="1200" alt="ミュージックビデオを仕上げる — @demon_ai_ — 元投稿の関連画像。クリックして X の投稿を開く"></a><br><b>ミュージックビデオを仕上げる</b><br><sub><a href="https://x.com/demon_ai_/status/1797764913198154072">@demon_ai_</a> · 2024-06-03</sub><br><sub>制作過程 / 完成作品</sub><br><a href="https://x.com/demon_ai_/status/1797764913198154072">▶ X の元投稿</a> · <a href="docs/x-community-examples.md#case-1797764913198154072">解説 · 英語 →</a></td>
</tr>
<tr>
<td width="33%" align="center" valign="top"><a href="https://x.com/Attack/status/1797664905568412055"><img src="https://pbs.twimg.com/ext_tw_video_thumb/1797663888697090048/pu/img/nPOfswNRcqjBjTWV.jpg" width="1200" alt="未完成のメロディーを育てる — @Attack — 元投稿の関連画像。クリックして X の投稿を開く"></a><br><b>未完成のメロディーを育てる</b><br><sub><a href="https://x.com/Attack/status/1797664905568412055">@Attack</a> · 2024-06-03</sub><br><sub>制作過程 / 完成作品</sub><br><a href="https://x.com/Attack/status/1797664905568412055">▶ X の元投稿</a> · <a href="docs/x-community-examples.md#case-1797664905568412055">解説 · 英語 →</a></td>
<td width="33%" align="center" valign="top"><a href="https://x.com/Hermion28758241/status/1802200978969559447"><img src="https://pbs.twimg.com/ext_tw_video_thumb/1802200843904532480/pu/img/Syu6hS_9jGHJvVo7.jpg" width="1200" alt="猫をテーマにした曲 — @Hermion28758241 — 元投稿の関連画像。クリックして X の投稿を開く"></a><br><b>猫をテーマにした曲</b><br><sub><a href="https://x.com/Hermion28758241/status/1802200978969559447">@Hermion28758241</a> · 2024-06-16</sub><br><sub>制作過程 / 完成作品</sub><br><a href="https://x.com/Hermion28758241/status/1802200978969559447">▶ X の元投稿</a> · <a href="docs/x-community-examples.md#case-1802200978969559447">解説 · 英語 →</a></td>
<td width="33%" align="center" valign="top"><a href="https://x.com/DJKNEK/status/2001536418393543105"><img src="https://cdn2.suno.ai/2607b0c3-4c55-4cad-98f8-e8e0217a184e.jpeg" width="1200" alt="段階的にファンクをリミックス — @DJKNEK — 元投稿の関連画像。クリックして X の投稿を開く"></a><br><b>段階的にファンクをリミックス</b><br><sub><a href="https://x.com/DJKNEK/status/2001536418393543105">@DJKNEK</a> · 2025-12-18</sub><br><sub>公開音楽プロンプト</sub><br><a href="https://x.com/DJKNEK/status/2001536418393543105">▶ X の元投稿</a> · <a href="docs/x-community-examples.md#case-2001536418393543105">解説 · 英語 →</a></td>
</tr>
</table>
<!-- COMMUNITY-CASES:END -->

<a id="start"></a>
## まず一曲作ってみる

**[Suno · 曲を作る ↗](https://suno.com/create)** · **[MusicMaker · 曲を作る ↗](https://musicmaker.im/ai-song-generator/)**

1. 下のどちらかを開き、Custom を選びます。
2. 曲調は Suno の Styles、または MusicMaker の Music Style に入力します。歌詞は Lyrics に入れます。
3. 下の練習は純音楽です。Instrumental をオンにして歌詞欄を空にし、モデル、クレジット、公開設定を確認して生成します。

Morning with Healing Hands の楽器構成を参考に、歌声のない曲へアレンジする練習です。

**試聴待ち**

```text
An instrumental acoustic piece for a quiet everyday scene.
Fingerpicked guitar leads, with upright bass and light strings.
Keep the mood warm and hopeful. No singing or spoken voice.
```

アカウント、クレジット、利用条件はサービスごとに別です。同じプロンプトでも同じ結果になるとは限りません。

[詳しいガイド・英語 →](docs/official-suno-guide.md)

### MusicMaker · 試聴 · 12

さらに **12 種類のサウンド**を探しましょう。上の制作案とは別の曲です。ジャケットと曲名は公開スタイルへ、試聴リンクは元の曲へ進みます。

[MusicMaker · 148 · 中文 / English →](docs/musicmaker-catalog.md)

<!-- BRAND-STYLES:START -->
<table width="100%">
<tr>
<td width="33%" align="center" valign="top"><a href="docs/musicmaker-catalog.md#discover-v2-26"><img src="https://cdn.musicmaker.im/musicmaker/discover_v2/plastic_midnight.webp" width="1200" alt="シティポップ · Plastic Midnight — 公開スタイルと素材情報を開く"></a><br><b>シティポップ</b><br><a href="docs/musicmaker-catalog.md#discover-v2-26">Plastic Midnight</a><br><a href="https://musicmaker.im/detail/discover-v2-26/">▶ 試聴</a></td>
<td width="33%" align="center" valign="top"><a href="docs/musicmaker-catalog.md#discover-v2-11"><img src="https://cdn.musicmaker.im/musicmaker/discover_ai_music/v2/cover/cypress_moon_rising.webp" width="1200" alt="スワンプブルース · Cypress Moon Rising — 公開スタイルと素材情報を開く"></a><br><b>スワンプブルース</b><br><a href="docs/musicmaker-catalog.md#discover-v2-11">Cypress Moon Rising</a><br><a href="https://musicmaker.im/detail/discover-v2-11/">▶ 試聴</a></td>
<td width="33%" align="center" valign="top"><a href="docs/musicmaker-catalog.md#discover-v2-43"><img src="https://cdn.musicmaker.im/musicmaker/discover_v2/midnight_rearview.webp" width="1200" alt="ディープハウス · Midnight Rearview — 公開スタイルと素材情報を開く"></a><br><b>ディープハウス</b><br><a href="docs/musicmaker-catalog.md#discover-v2-43">Midnight Rearview</a><br><a href="https://musicmaker.im/detail/discover-v2-43/">▶ 試聴</a></td>
</tr>
<tr>
<td width="33%" align="center" valign="top"><a href="docs/musicmaker-catalog.md#discover-v2-78"><img src="https://cdn.musicmaker.im/musicmaker/discover_v2/sunrise_on_vinyl.webp" width="1200" alt="ローファイソウル · Sunrise On Vinyl — 公開スタイルと素材情報を開く"></a><br><b>ローファイソウル</b><br><a href="docs/musicmaker-catalog.md#discover-v2-78">Sunrise On Vinyl</a><br><a href="https://musicmaker.im/detail/discover-v2-78/">▶ 試聴</a></td>
<td width="33%" align="center" valign="top"><a href="docs/musicmaker-catalog.md#discover-v2-28"><img src="https://cdn.musicmaker.im/musicmaker/discover_v2/glass_dolls.webp" width="1200" alt="ダークポップ · Glass Dolls — 公開スタイルと素材情報を開く"></a><br><b>ダークポップ</b><br><a href="docs/musicmaker-catalog.md#discover-v2-28">Glass Dolls</a><br><a href="https://musicmaker.im/detail/discover-v2-28/">▶ 試聴</a></td>
<td width="33%" align="center" valign="top"><a href="docs/musicmaker-catalog.md#discover-v2-46"><img src="https://cdn.musicmaker.im/musicmaker/discover_v2/bonfire_kinda_night.webp" width="1200" alt="モダンカントリー · Bonfire Kinda Night — 公開スタイルと素材情報を開く"></a><br><b>モダンカントリー</b><br><a href="docs/musicmaker-catalog.md#discover-v2-46">Bonfire Kinda Night</a><br><a href="https://musicmaker.im/detail/discover-v2-46/">▶ 試聴</a></td>
</tr>
<tr>
<td width="33%" align="center" valign="top"><a href="docs/musicmaker-catalog.md#discover-v2-86"><img src="https://cdn.musicmaker.im/musicmaker/discover_v2/rua_em_chamas.webp" width="1200" alt="ブラジリアンPhonk · Rua Em Chamas — 公開スタイルと素材情報を開く"></a><br><b>ブラジリアンPhonk</b><br><a href="docs/musicmaker-catalog.md#discover-v2-86">Rua Em Chamas</a><br><a href="https://musicmaker.im/detail/discover-v2-86/">▶ 試聴</a></td>
<td width="33%" align="center" valign="top"><a href="docs/musicmaker-catalog.md#discover-v2-29"><img src="https://cdn.musicmaker.im/musicmaker/discover_v2/first_look_forever.webp" width="1200" alt="ドリームポップ · First Look, Forever — 公開スタイルと素材情報を開く"></a><br><b>ドリームポップ</b><br><a href="docs/musicmaker-catalog.md#discover-v2-29">First Look, Forever</a><br><a href="https://musicmaker.im/detail/discover-v2-29/">▶ 試聴</a></td>
<td width="33%" align="center" valign="top"><a href="docs/musicmaker-catalog.md#discover-10"><img src="https://cdn.musicmaker.im/musicmaker/discover_ai_music/example/Awakening_echoes.webp" width="1200" alt="Hyper-afrobeat · Awakening echoes — 公開スタイルと素材情報を開く"></a><br><b>Hyper-afrobeat</b><br><a href="docs/musicmaker-catalog.md#discover-10">Awakening echoes</a><br><a href="https://musicmaker.im/detail/discover-10/">▶ 試聴</a></td>
</tr>
<tr>
<td width="33%" align="center" valign="top"><a href="docs/musicmaker-catalog.md#discover-v2-22"><img src="https://cdn.musicmaker.im/musicmaker/discover_v2/midnight_garden_circuits.webp" width="1200" alt="アンビエント電子音楽 · Midnight Garden Circuits — 公開スタイルと素材情報を開く"></a><br><b>アンビエント電子音楽</b><br><a href="docs/musicmaker-catalog.md#discover-v2-22">Midnight Garden Circuits</a><br><a href="https://musicmaker.im/detail/discover-v2-22/">▶ 試聴</a></td>
<td width="33%" align="center" valign="top"><a href="docs/musicmaker-catalog.md#discover-v2-19"><img src="https://cdn.musicmaker.im/musicmaker/discover_v2/salt_on_my_skin.webp" width="1200" alt="トロピカルハウス · Salt on My Skin — 公開スタイルと素材情報を開く"></a><br><b>トロピカルハウス</b><br><a href="docs/musicmaker-catalog.md#discover-v2-19">Salt on My Skin</a><br><a href="https://musicmaker.im/detail/discover-v2-19/">▶ 試聴</a></td>
<td width="33%" align="center" valign="top"><a href="docs/musicmaker-catalog.md#discover-37"><img src="https://cdn.musicmaker.im/musicmaker/discover_ai_music/example/City_pulse.webp" width="1200" alt="シンセウェイヴ · City pulse — 公開スタイルと素材情報を開く"></a><br><b>シンセウェイヴ</b><br><a href="docs/musicmaker-catalog.md#discover-37">City pulse</a><br><a href="https://musicmaker.im/detail/discover-37/">▶ 試聴</a></td>
</tr>
</table>
<!-- BRAND-STYLES:END -->

<!-- MUSICMAKER-DETECTOR:START -->
<a id="musicmaker-detector"></a>

## MusicMaker｜この曲も AI で作られたの？

自分の曲を作るだけでなく、いろいろな作品を聴くこともヒントになります。気に入った曲に出会うと、Suno などの AI ツールが使われているのか気になることもあるでしょう。

そんなときは **MusicMaker の Free Suno AI Music Detector** を試してみてください。音声をアップロードすると、AI 生成の可能性を示す推定スコアと、識別できた場合は生成ツールの候補を確認できます。

<p align="center"><a href="https://musicmaker.im/"><img src="https://musicmaker.im/images/logo.svg" width="64" alt="MusicMaker — musicmaker.im"></a><br><strong>AI Music Maker</strong></p>

<a href="https://musicmaker.im/free-suno-ai-music-detector/"><img src="assets/screenshots/musicmaker-suno-detector.jpg" width="100%" alt="MusicMaker の検出ツールの画面：音声アップロード、Check ボタン、結果欄。クリックして試す"></a>

<sub>英語の画面です。</sub>

音声をアップロード → ログインして **Check** をクリック → 判定と AI 生成の可能性を確認。

**[MusicMaker の音楽検出ツールを試す →](https://musicmaker.im/free-suno-ai-music-detector/)** · [結果の読み方・英語](docs/detector-and-release.md)

<sub>検出結果は参考情報です。作品の利用許可は作者に確認してください。</sub>
<!-- MUSICMAKER-DETECTOR:END -->

[Sources · English](docs/sources.md) · [Contributing · English](CONTRIBUTING.md)

<!-- BRAND-AFFILIATE:START -->
### MusicMaker のアフィリエイトパートナー募集

MusicMaker では、クリエイター、レビュー執筆者、教育者、コミュニティとのアフィリエイト提携を受け付けています。読者や視聴者に MusicMaker を紹介し、条件を満たす紹介注文に応じて報酬を受け取れます。

**[プログラムの詳細と参加方法を見る →](https://musicmaker.im/affiliate-program/)**
<!-- BRAND-AFFILIATE:END -->
