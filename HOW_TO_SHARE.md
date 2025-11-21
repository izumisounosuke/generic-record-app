# 他の人に見せる方法

このプロジェクトを他の人に見せる方法を説明します。

## 方法1: リポジトリのURLを共有する（最も簡単）

### 公開リポジトリ（Public）の場合

リポジトリを**Public**に設定している場合、以下のURLを共有するだけで誰でも見ることができます：

```
https://github.com/izumisounosuke/generic-record-app
```

### 非公開リポジトリ（Private）の場合

**Private**リポジトリの場合は、以下の方法で共有できます：

#### 1. コラボレーターとして追加する

1. GitHubのリポジトリページで「Settings」タブをクリック
2. 左メニューから「Collaborators」を選択
3. 「Add people」ボタンをクリック
4. GitHubのユーザー名またはメールアドレスを入力
5. 招待を送信

招待された人はメールで通知を受け取り、リポジトリにアクセスできるようになります。

#### 2. 一時的に公開リポジトリに変更する

1. リポジトリページで「Settings」タブをクリック
2. 一番下までスクロールして「Danger Zone」セクションを開く
3. 「Change visibility」→「Change to public」を選択

## 方法2: リポジトリをクローンしてもらう

他の人がプロジェクトを使いたい場合、以下のコマンドでクローンできます：

```bash
git clone https://github.com/izumisounosuke/generic-record-app.git
cd generic-record-app
pip install -r requirements.txt
python app.py
```

## 方法3: デプロイして実際に使えるようにする

ローカルでしか動作しないアプリを、インターネット上で誰でも使えるようにするには、以下のサービスにデプロイします：

### 推奨サービス

1. **Render** (無料プランあり)
   - https://render.com
   - Flaskアプリを簡単にデプロイ可能
   - 自動でURLが発行される

2. **Heroku** (有料プランが必要な場合あり)
   - https://www.heroku.com
   - 無料プランは終了しましたが、教育用は無料の場合があります

3. **Railway** (無料プランあり)
   - https://railway.app
   - 簡単にデプロイ可能

4. **PythonAnywhere** (無料プランあり)
   - https://www.pythonanywhere.com
   - Python専用のホスティングサービス

### デプロイ時の注意点

- 環境変数（SECRET_KEYなど）を設定する
- データベースの設定を確認する
- プロダクション用の設定を追加する（`debug=False`など）

## リポジトリの有効性について

### ✅ 基本的にはずっと有効です

- **GitHubアカウントが削除されない限り、リポジトリは存在し続けます**
- **無料アカウントでも、Publicリポジトリは無制限に作成・保持できます**
- **Privateリポジトリも無料で無制限に作成できます**

### ⚠️ リポジトリが削除される可能性がある場合

以下の場合のみ、リポジトリが削除される可能性があります：

1. **手動で削除した場合**
   - Settings → Danger Zone → Delete this repository

2. **GitHubアカウントを削除した場合**
   - アカウント削除時にすべてのリポジトリも削除されます

3. **GitHubの利用規約違反があった場合**
   - 違反が発覚した場合、アカウントやリポジトリが削除される可能性があります

4. **長期未使用の場合**（稀）
   - 通常は削除されませんが、GitHubのポリシー変更で削除される可能性はあります（ほぼありません）

### 🔒 安全に保つ方法

1. **定期的にバックアップを取る**
   ```bash
   git clone https://github.com/izumisounosuke/generic-record-app.git
   ```

2. **他の場所にもバックアップする**
   - 別のGitホスティングサービス（GitLab、Bitbucketなど）にもプッシュ
   - ローカルにコピーを保存

3. **重要データは別途保存**
   - データベースファイルは`.gitignore`で除外されていますが、必要に応じてバックアップ

## リポジトリの状態を確認する方法

1. **GitHubでアクセスできるか確認**
   - https://github.com/izumisounosuke/generic-record-app にアクセス

2. **リポジトリがPublicかPrivateか確認**
   - リポジトリページの上部に表示される
   - 「Public」または「Private」と表示される

3. **最終更新日時を確認**
   - リポジトリページで「Last commit」の日時を確認

## まとめ

- **共有方法**: URLを共有するのが最も簡単
- **有効期限**: 基本的にはずっと有効（GitHubアカウントが存在する限り）
- **おすすめ**: デプロイして実際に使えるアプリとして公開すると、より多くの人に見てもらえます

