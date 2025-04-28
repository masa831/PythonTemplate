# sphinx

## 実行の手順 by chatgpt

1. ディレクトリ構成を整備

```md
sample_project/
  ├── mypackage/
  │     ├── __init__.py
  │     └── calculator.py
  └── docs/
```

※calculator.py の中身を書いておく
sample_project/mypackage/calculator.py に、簡単な関数とdocstringを書きます。

2. Sphinxをセットアップする
次に、sample_project/docs/に移動して、Sphinxの設定をします。
```bash
cd sample_project/docs
sphinx-quickstart
```

起動後の質問には以下のように答える
- Separate source and build directories? → y
- Project name → sample_project
- Author name → 適当に
- その他はデフォルトでOK

3. conf.py を設定する
docs/source/conf.py を少し編集します。
まず、Pythonコードが見つかるようにパスを通します。

```py
import os
import sys
sys.path.insert(0, os.path.abspath('../../mypackage'))
```

次に、必要な拡張を有効にします。

```py
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',  # Google/Numpyスタイルdocstring対応
    'sphinx.ext.viewcode',  # ソースコードへのリンク
]

# テーマの変更
html_theme = 'sphinx_rtd_theme'
```


1. sphinx-apidocでrstファイルを作る
ドキュメントのひな形を自動生成します！

```bash
sphinx-apidoc -o source ../mypackage
# 上書きモード
sphinx-apidoc -f -o source ../mypackage
```
すると、source/mypackage.rst などができあがります。

5. index.rstにモジュールを追加
docs/source/index.rst にこの一行を追加して、モジュールを表示するようにします。

```rst
.. toctree::
   :maxdepth: 2
   :caption: Contents:

   mypackage
```

6. ドキュメントをビルドする

```bash
make html
```
（Windowsなら make.bat html）

→ docs/build/html/index.html ができるので、ブラウザで開くと内容を確認できる。

## 補足
### うまく行かない場合
```bash
# いったん古いビルドを削除
make clean
# 再ビルド
make html
```