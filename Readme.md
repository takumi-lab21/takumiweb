## 概要
Djangoを試す。

## リンク
- [Django girls](https://tutorial.djangogirls.org/ja/django_installation/)
- [Document](https://docs.djangoproject.com/ja/4.0/)


## インストール
```bash
sudo apt install sqlite3

PIPENV_VENV_IN_PROJECT=true pipenv install

# マイグレーションの実行
pipenv shell
python manage.py migrate

# スーパーユーザーの作成
python manage.py createsuperuser
```

## サーバーの起動
```bash
pipenv run start
```


## 手順

### プロジェクトの作成
```bash
django-admin startproject takumiweb .
```

以下の構成でファイルが作成される。

```
djangogirls
├── manage.py
├── takumiweb
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── myvenv
│   └── ...
└── requirements.txt
```

- manage.py
  - Djangoのプロジェクトに関するコマンドを実行するための実行ファイル。
- takumiweb
  - プロジェクト共通の設定やスクリプトが格納されている。
  - startprojectを実行した時の名前がフォルダ名になる。
  - settings.py
    - 環境変数などの設定
  - urls.py
    - ルーティングにか変わる設定
  - wsgi.py
    - ？？？

### 設定の変更
setting.pyを編集する。


### モデルの生成

