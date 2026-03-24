# Django Tutorial Project

このプロジェクトはDjangoのチュートリアル用プロジェクトです。Djangoの基本的な機能を学習するためのサンプルアプリケーションです。

## 必要条件

- Python 3.10 以上
- pip

## インストール方法

1. リポジトリをクローンまたはダウンロードします。

2. 仮想環境を作成し、有効化します：
   ```bash
   python -m venv myvenv
   source myvenv/bin/activate  # Windowsの場合: myvenv\Scripts\activate
   ```

3. 依存パッケージをインストールします：
   ```bash
   pip install -r requirements.txt
   ```

4. 設定ファイルをコピーします：
   ※PythonAnywhereを使うために以下の設定は削除しています

   ```bash
   cp mysite/settings.dist.py mysite/settings.py
   ```

   `mysite/settings.py` を編集して、SECRET_KEYを実際の値に変更してください。
   必要に応じてDEBUGやALLOWED_HOSTSも調整してください。

## マイグレーションの実行

データベースの初期化とマイグレーションを実行します：

```bash
python manage.py makemigrations
python manage.py migrate
```

## サーバーの起動

開発サーバーを起動します：

```bash
python manage.py runserver
```

ブラウザで `http://127.0.0.1:8000/` にアクセスしてアプリケーションを確認できます。

## プロジェクト構造

- `mysite/` - Djangoプロジェクトの設定ディレクトリ
- `manage.py` - Django管理スクリプト
- `requirements.txt` - 依存パッケージリスト

## 追加情報

- Djangoの公式ドキュメント: https://docs.djangoproject.com/
- このプロジェクトはDjango 5.1.x を使用しています

## ライセンス

このプロジェクトはMITライセンスの下で公開されています。