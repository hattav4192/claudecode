---
name: start
description: 作業開始フロー。ブランチ作成とTODO設定を行う。「始めて」「start」「ブランチ作って」の時に使用。
user-invocable: true
allowed-tools: Bash, Write, Read, TodoWrite
argument-hint: <機能名または修正内容>
---

新しい作業を開始するためのブランチを作成し、TODOを設定する。

## 引数
$ARGUMENTS に機能名または修正内容が入る（例: `ゲームオブライフの速度調整機能`）

## ステップ

### 1. ブランチ名の決定
$ARGUMENTS から英語のブランチ名を生成する：
- 新機能: `feat-<機能名>`（例: `feat-speed-control`）
- バグ修正: `fix-<修正内容>`（例: `fix-cell-render`）
- ドキュメント: `docs-<内容>`
- リファクタ: `refactor-<内容>`

### 2. mainブランチの最新化
```
git checkout main
git pull origin main
```

### 3. ブランチ作成
```
git checkout -b <ブランチ名>
```

### 4. TODOの設定
TodoWriteツールで以下のTODOを作成する：
- [ ] $ARGUMENTS の実装
- [ ] テストの作成・実行
- [ ] lint・typecheckの実行
- [ ] コミット・push・PR作成（/done で実行）

### 5. 完了報告
作成したブランチ名とTODOリストを表示して「作業を開始できます！実装が終わったら /done を実行してください。」と伝える。
