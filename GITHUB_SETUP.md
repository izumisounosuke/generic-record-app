# GitHubに公開する手順

このプロジェクトをGitHubに公開するための手順を説明します。

## 前提条件

- GitHubアカウントを持っていること
- Gitがインストールされていること（既に確認済み）

## 手順

### 1. GitHubでリポジトリを作成

1. [GitHub](https://github.com)にログインします
2. 右上の「+」ボタンをクリック → 「New repository」を選択
3. リポジトリ名を入力（例：`generic-record-app`）
4. 説明を入力（例：「汎用記録アプリ - Flaskで作られた記録管理Webアプリケーション」）
5. Public（公開）またはPrivate（非公開）を選択
6. **「Add a README file」のチェックは外す**（既にREADME.mdがあるため）
7. 「Create repository」をクリック

### 2. ローカルでGitリポジトリを初期化

プロジェクトのフォルダで、以下のコマンドを実行してください：

```bash
# Gitリポジトリを初期化
git init

# すべてのファイルをステージング
git add .

# 初回コミット
git commit -m "Initial commit: 汎用記録アプリ"
```

### 3. GitHubリポジトリと接続

GitHubで作成したリポジトリのページに表示されているURLをコピーしてください。
例：`https://github.com/YOUR_USERNAME/generic-record-app.git`

その後、以下のコマンドを実行：

```bash
# リモートリポジトリを追加（YOUR_USERNAMEとリポジトリ名を実際のものに置き換えてください）
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git

# メインブランチを設定
git branch -M main

# GitHubにプッシュ
git push -u origin main
```

### 4. 認証について

GitHubにプッシュする際、認証が必要になります。以下のいずれかの方法を使用してください：

#### 方法A: Personal Access Token (推奨)

1. GitHub → Settings → Developer settings → Personal access tokens → Tokens (classic)
2. 「Generate new token」をクリック
3. 必要な権限にチェック（`repo`権限が必要）
4. トークンを生成してコピー
5. パスワードの代わりにトークンを使用

#### 方法B: GitHub CLI

```bash
# GitHub CLIをインストールしてログイン
gh auth login
```

### 5. プッシュ後の確認

GitHubのリポジトリページを開いて、ファイルがアップロードされていることを確認してください。

## トラブルシューティング

### 「remote origin already exists」エラー

既にリモートが設定されている場合は、以下のコマンドで削除してから再設定：

```bash
git remote remove origin
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git
```

### 「authentication failed」エラー

認証情報を確認してください。Personal Access Tokenを使用している場合は、パスワードではなくトークンを使用してください。

### ファイルがアップロードされない

`.gitignore`ファイルで除外されているファイルはアップロードされません。これは正常な動作です（`records.db`などは自動生成されるため除外されています）。

## 今後の更新方法

コードを変更した後は、以下のコマンドでGitHubに更新を反映できます：

```bash
# 変更をステージング
git add .

# コミット（メッセージを変更してください）
git commit -m "更新内容の説明"

# GitHubにプッシュ
git push
```

## 参考リンク

- [GitHub Docs](https://docs.github.com/)
- [Git 公式ドキュメント](https://git-scm.com/doc)

