---
name: done
description: 作業完了フロー。lint・typecheck・テスト実行後、コミット・push・PR作成を行う。「完了」「done」「仕上げて」の時に使用。
user-invocable: true
allowed-tools: Bash, Read, Edit, Glob, Grep
---

現在のブランチで作業完了フローを実行する。

## ステップ

### 1. 現状確認
- `git branch --show-current` で現在のブランチを確認
- mainブランチの場合は「mainブランチでは実行できません」と伝えて停止する

### 2. lint・typecheck（該当する場合）
プロジェクトの設定ファイルを確認して適切なコマンドを実行する：
- `package.json` があれば `npm run lint`、`npm run typecheck`（または `npm run type-check`）を実行
- Pythonプロジェクトなら `flake8` や `mypy` を実行
- エラーがある場合は修正してから次へ進む

### 3. テスト実行
プロジェクトの設定に応じてテストを実行：
- `package.json` があれば `npm test` を実行
- Pythonなら `pytest` を実行
- テストが失敗した場合は修正してから次へ進む

### 4. コミット
- `git status` と `git diff` で変更内容を確認
- 変更内容に基づいてConventional Commits形式でコミットメッセージを作成
  - 形式: `feat:`, `fix:`, `docs:`, `refactor:`, `test:`, `chore:`
  - 本文は日本語で記述
- `git add -A` でステージング（.envや機密ファイルは除外）
- コミットを実行

### 5. push
- `git push origin <現在のブランチ名>` でpush
- 初回は `-u` オプションを付ける

### 6. PR作成
- `gh pr list` で既存のPRを確認
- PRがまだなければ `gh pr create` で作成：
  - タイトル: コミットメッセージの要約（70文字以内）
  - 本文: 変更内容の要約・テスト計画をmarkdownで記述
  - ベースブランチ: main
- 既にPRがある場合はPRのURLを表示して完了

## 完了時
PRのURLを表示して「作業完了しました！」と報告する。
