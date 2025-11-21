# 汎用記録アプリ

ユーザーが記録したい項目を自由に定義できる汎用記録Webアプリケーションです。

## 機能

- **ユーザー認証**: ログイン・サインアップ機能
- **汎用的な記録機能**: 
  - 任意の項目（項目名・単位）を追加・管理
  - 各項目に対して日付と数値を記録
  - 同じ日付に複数回記録すると、自動的に加算されます
  - 5個以上の項目を管理可能
- **グラフ化**: Chart.jsを使用したデータの可視化
  - 折れ線グラフ、棒グラフ、エリアチャート、円グラフから選択可能

## 技術スタック

- **バックエンド**: Python Flask
- **データベース**: SQLite (SQLAlchemy)
- **フロントエンド**: 
  - Bootstrap 5（レスポンシブ対応）
  - Chart.js（グラフ表示）
  - Bootstrap Icons

## セットアップ

### 1. リポジトリのクローン

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git
cd YOUR_REPOSITORY_NAME
```

### 2. 必要なパッケージのインストール

```bash
pip install -r requirements.txt
```

### 3. アプリケーションの起動

```bash
python app.py
```

### 4. ブラウザでアクセス

```
http://localhost:5000
```

初回実行時に`records.db`（SQLiteデータベース）が自動生成されます。

## 使用方法

1. **ユーザー登録・ログイン**
   - 新規登録またはログインを行います

2. **項目の作成**
   - ダッシュボードで「項目名」と「単位」を入力して項目を作成
   - 例: 項目名「体重」、単位「kg」

3. **記録の追加**
   - 項目をクリックして詳細ページを開く
   - 日付と値を入力して記録を追加
   - **同じ日付に複数回記録すると、値が自動的に加算されます**

4. **データの確認**
   - グラフでデータの推移を確認
   - グラフタイプは折れ線、棒グラフ、エリア、円グラフから選択可能
   - 履歴一覧で過去の記録を確認

## ファイル構成

```
.
├── app.py                 # メインアプリケーション
├── models.py             # データベースモデル
├── requirements.txt      # 依存パッケージ
├── .gitignore           # Git除外ファイル
├── README.md            # このファイル
├── records.db           # SQLiteデータベース（自動生成、Git管理外）
└── templates/           # HTMLテンプレート
    ├── layout.html      # ベースレイアウト
    ├── login.html       # ログイン画面
    ├── register.html    # 登録画面
    ├── index.html       # ダッシュボード
    └── item_detail.html # 項目詳細ページ
```

## データベース設計

- **User**: ユーザー情報
  - id, username, password_hash, created_at

- **Item**: 記録項目
  - id, user_id, name, unit, created_at

- **Record**: 記録データ
  - id, item_id, date, value, created_at

## 特徴

- 同じ日付の記録は自動的に加算されるため、1日に複数回記録しても1つの記録として管理されます
- グラフの表示形式を選択可能（折れ線、棒、エリア、円）
- レスポンシブ対応でモバイルでも使いやすい

## ライセンス

このプロジェクトは大学の課題として作成されました。
