# Renderデプロイエラーの修正方法

## エラー内容
```
Service Root Directory "/opt/render/project/src/Singapore" is missing.
```

このエラーは、Renderの設定で「Root Directory」が間違って設定されている場合に発生します。

## 修正方法

### 方法1: Renderのダッシュボードで修正（推奨）

1. Renderのダッシュボードで、作成したWebサービスを開く
2. 「Settings」タブをクリック
3. **「Root Directory」のフィールドを空白にする**（これが重要！）
4. 以下の設定を確認：
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
5. 「Save Changes」をクリック
6. 再度デプロイが開始されます

### 方法2: render.yamlを使わない

`render.yaml`ファイルが問題を引き起こしている可能性があるため、削除して、ダッシュボードで直接設定する方が簡単です：

1. GitHubで`render.yaml`を削除
2. Renderのダッシュボードで設定を手動で入力

---

## 正しい設定

Renderのダッシュボードで以下のように設定してください：

- **Name**: `generic-record-app`（任意）
- **Region**: `Singapore` または `Frankfurt`
- **Branch**: `main`
- **Root Directory**: **空白のまま**（重要！）
- **Runtime**: `Python 3`
- **Build Command**: `pip install -r requirements.txt`
- **Start Command**: `gunicorn app:app`

**Root Directoryは絶対に空白にしてください！**

---

## トラブルシューティング

### まだエラーが出る場合

1. Renderでサービスを削除
2. 再度「New Web Service」から作成
3. 今度は**Root Directoryを空白のまま**にしてください

### デプロイが成功するか確認

デプロイが成功すると、「Logs」タブに以下のようなメッセージが表示されます：
```
Listening at: http://0.0.0.0:10000
```

このメッセージが出たら成功です！

