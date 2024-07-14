# poetry

色々なコマンドについて説明がある。
<https://zenn.dev/shotakaha/scraps/9416c30cd7745a>

<https://zenn.dev/kkj/articles/d14470babe1930>

<https://qiita.com/ksato9700/items/b893cf1db83605898d8a>


新規でプロジェクトを生成

```bash
# 実行したフォルダの配下に新規でテンプレートフォルダが作られる
poetry new poetrydemo

```

templateフォルダ構成

```bash
├── poetry-demo
│   ├── README.md
│   ├── poetry_demo
│   │   └── __init__.py
│   ├── pyproject.toml
│   └── tests
│       └── __init__.py
```

既存の環境をインストール
```bash
# tomlファイルに記載があるパッケージをインストールする
poetry install
```


パッケージ追加

```bash
# python3.8環境でadd pandasとすると、バージョンの問題でエラーとなった。
# 最新のpython環境ではない場合、バージョン指定は必須かもしれない
# tomlファイルも自動で更新された
poetry add pandas=1.4

```

実行

```bash
# pattern1
poetry run python poetrydemo\main.py

# pattern2
poetry shell
python <python-file>
```
