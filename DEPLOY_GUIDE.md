# 他の人がアプリを見る方法 - デプロイガイド

現在、アプリはあなたのPC上でしか動いていません（localhost）。他の人に見てもらうには、インターネット上に公開する必要があります。

## おすすめの方法：Render（無料プランあり、簡単）

Renderは無料プランがあり、Flaskアプリを簡単にデプロイできます。

### 手順

#### 1. Renderのアカウント作成

1. [Render](https://render.com) にアクセス
2. 「Get Started for Free」をクリック
3. GitHubアカウントでサインアップ（推奨）またはメールアドレスで登録

#### 2. GitHubに最新のコードをプッシュ

まず、作成したデプロイ用ファイルをGitHubにプッシュします：

```bash
git add .
git commit -m "デプロイ用ファイルを追加"
git push
```

#### 3. RenderでWebサービスを作成

1. Renderのダッシュボードで「New +」→「Web Service」をクリック
2. 「Build and deploy from a Git repository」を選択
3. GitHubアカウントを接続（まだの場合）
4. リポジトリ `generic-record-app` を選択
5. 設定を入力：
   - **Name**: `generic-record-app`（好きな名前でOK）
   - **Region**: `Singapore` または `Frankfurt`（日本に近い地域を選択）
   - **Branch**: `main`
   - **Root Directory**: （空白のまま）
   - **Runtime**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
6. 「Create Web Service」をクリック

#### 4. デプロイの完了を待つ

数分待つと、デプロイが完了します。完了すると、以下のようなURLが発行されます：
```
https://generic-record-app.onrender.com
```

このURLを他の人に共有すれば、誰でもアプリを見ることができます！

### デプロイ後の注意点

- **初回起動が遅い場合があります**（無料プランはスリープモードになります）
- **データベースは自動生成されます**（Renderでは新しいデータベースファイルが作成されます）
- **URLは永続的です**（デプロイを削除しない限り有効です）

---

## その他のデプロイ方法

### Railway（無料プランあり）

1. [Railway](https://railway.app) にアクセス
2. GitHubアカウントでサインアップ
3. 「New Project」→「Deploy from GitHub repo」
4. リポジトリを選択
5. 自動的にデプロイされます

### PythonAnywhere（無料プランあり）

1. [PythonAnywhere](https://www.pythonanywhere.com) にアクセス
2. アカウントを作成
3. 「Web」タブから新しいWebアプリを作成
4. GitHubからコードをクローン
5. 設定を行ってデプロイ

---

## デプロイ前に確認すること

- [ ] `requirements.txt`に`gunicorn`が含まれている
- [ ] `Procfile`が作成されている
- [ ] 最新のコードがGitHubにプッシュされている

---

## デプロイ後のURL共有方法

デプロイが完了したら、以下のように他の人に共有できます：

```
このアプリを使ってみてください！
https://generic-record-app.onrender.com
```

このURLを共有するだけで、誰でもブラウザでアクセスしてアプリを使えます。

---

## トラブルシューティング

### デプロイが失敗する場合

1. **Build Command**が正しいか確認
2. **Start Command**が`gunicorn app:app`になっているか確認
3. Renderのログを確認（「Logs」タブ）

### アプリが起動しない場合

1. `requirements.txt`に`gunicorn`が含まれているか確認
2. `app.py`のポート設定を確認
3. Renderのログでエラーメッセージを確認

---

## まとめ

1. Renderでアカウント作成
2. GitHubリポジトリを接続
3. Webサービスを作成
4. デプロイ完了後にURLを共有

これで他の人もアプリを見られるようになります！

