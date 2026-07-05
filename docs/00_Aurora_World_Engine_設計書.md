# Aurora World Engine 設計書 Ver.1.0

---

# 1. プロジェクト概要

Aurora World Engine は、自分だけの世界を作り、その世界で自由に物語を楽しむための AI ストーリーゲームエンジンである。

AIチャットアプリではなく、世界・キャラクター・シナリオ・プレイヤーを管理し、長期間遊び続けられることを目的とする。

---

# 2. コンセプト

Create Your World.
Live Your Story.

プレイヤーは

・世界を作る

・登場人物を作る

・自分自身（ペルソナ）を作る

・物語を開始する

・AIゲームマスターと共に物語を進める

ことができる。

Session（プレイデータ）は保存され、いつでも続きを遊べる。

---

# 3. Aurora World Engine の思想

AuroraはAIチャットではない。

Auroraは

「世界を作る」

「世界を遊ぶ」

「世界を育てる」

ためのエンジンである。

世界はProjectとして保存され、

物語はSessionとして積み重なっていく。

---

# 4. 基本構成

Aurora World Engineは4つの機能で構成される。

・PLAY

・CREATE

・CHARACTER LIBRARY

・SETTINGS

---

# 5. PLAY

PLAYは実際に物語を遊ぶ画面である。

PLAYは

・新しく始める

・続きから

の2つで構成される。

## 新しく始める

Projectを選択

↓

開始準備

↓

Session作成

↓

Play開始

開始準備では

・Project説明

・Scenario選択

・登場Character追加

・Persona選択

を行う。

## 続きから

保存されたSession一覧を表示する。

Sessionを選択するとその続きを開始する。

---

# 6. CREATE

CREATEは世界を作る画面である。

CREATEは

新規作成

編集

に分かれる。

## 新規作成

・Project

・Character

・Persona

## 編集

・Project

・Character

・Persona

編集では

作成済みデータの編集・削除ができる。

削除時は必ず確認画面を表示する。

---

# 7. CHARACTER LIBRARY

Character Libraryには全Characterを保存する。

Characterは

・Project Character

・単独作成Character

をまとめて管理する。

Character Libraryでは

・編集

・削除

・Character Chat

が行える。

Character ChatではProjectを使わずCharacter単体と会話できる。

---

# 8. SETTINGS

設定画面では

・AI設定

・表示設定

・画像設定

・データ管理

を行う。

---

# 9. Project

Projectは一つの世界である。

Projectは以下を持つ。

・世界観

・概要

・Scenario

・Project Character

・背景画像

Projectはゲーム一本に相当する。

---

# 10. Character

CharacterはAIが演じる登場人物である。

Characterは

・名前

・設定

・画像

を持つ。

Characterは複数Projectへ出演可能。

---

# 11. Persona

Personaはプレイヤー自身である。

Personaは

・名前

・設定

を持つ。

Session開始時に選択し、

Play中でも変更できる。

---

# 12. Scenario

Scenarioは物語の開始地点である。

Project内に複数保存できる。

開始時に選択する。

---

# 13. Session

Sessionはプレイデータである。

Sessionは

Project

Scenario

Persona

Chat履歴

を保存する。

続きを遊ぶ場合はSessionを読み込む。

---

# 14. Image System

画像は

Project

Character

のみ設定する。

画像登録時は

・推奨サイズ表示

・切り抜き

・拡大縮小

・位置調整

を行う。

画像が無い場合はAI画像生成も利用できる。

---

# 15. 今後の開発

Version 1.0

設計書完成

Version 1.1

基本実装

Version 1.2

画像システム

Version 1.3

Character Library

Version 1.4

AI画像生成

Version 2.0

スマホ正式版
