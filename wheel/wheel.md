# wheel

## whl生成方法

setup.pyを使用するパターンとpyproject.tomlを使用するパターンが存在する。
pyproject.tomlの方が簡潔な記載になっている印象。
共存は推奨されない。どちらもファイルが存在する場合は、setup.pyが優先される様子。(実験的に確かめた。)

### setup.py

対象のディレクトリに移動し、以下のコマンドで圧縮ができる。
圧縮には2パターンある。
いずれの場合もdistフォルダにwhlファイルが生成される。

```bash
# setuptools
python setup.py bdist_wheel

# pip
pip wheel .

```

setupファイルテンプレート
```python
from setuptools import setup

setup(
    name='パッケージ名',
    version='バージョン番号',
    description='パッケージの説明文',
    author='作者名',
    author_email='メールアドレス',
    url='プロジェクトURL',
    packages=['package_name'],  # パッケージ名
    install_requires=[
        # 必要な依存関係
        '依存関係パッケージ名1',
        '依存関係パッケージ名2',
        # ...
    ],
    python_requires='>=3.6',  # 必要なPythonバージョン
)
```

### pyproject.toml

```bash
# buildがインストールされている必要がある。
pip install build

# pip
pip wheel .

```

```bash
[project]
name = "パッケージ名"
version = "バージョン"
description = "パッケージの説明文"
authors = [{name = "Pradyun Gedam", email = "pradyun@example.com"}]

[project.scripts]
# コマンド名 = モジュール:関数
myscript = "mypackage:main"

[dependencies]
# 依存関係モジュール
requests = "^2.27.1"
```

pyproject.tomlのテンプレートあり

<https://packaging.python.org/en/latest/guides/writing-pyproject-toml/>

## whlインストール方法

通常のpipコマンドでインストールが可能

```bash
pip install xxx.whl
```

インストール後はpip listで確認できる。

## フォルダ構成テンプレート

<https://peps.python.org/pep-0636/>

<https://github.com/cookiecutter/cookiecutter>

### PEP636

PEP 636は、Pythonプロジェクトのディレクトリ構造に関する標準的なガイドラインです。以下のディレクトリ構成が推奨されています。

```bash
project_root
├── LICENSE
├── README.md
├── docs
│   └── ...
├── tests
│   └── ...
├── src
│   ├── __init__.py
│   └── packages
│       ├── package1
│       │   ├── __init__.py
│       │   └── modules.py
│       └── package2
│           ├── __init__.py
│           └── modules.py
└── tox.ini
```

各ファルダ、ファイルの説明

project_root: プロジェクトのルートディレクトリ  
LICENSE: ライセンスファイル  
README.md: プロジェクトの説明書  
docs: ドキュメントディレクトリ  
tests: テストコードディレクトリ  
src: ソースコードディレクトリ  
__init__.py: パッケージ初期化ファイル  
packages: パッケージディレクトリ  
package1: パッケージ1ディレクトリ  
__init__.py: パッケージ1初期化ファイル  
modules.py: パッケージ1のモジュールファイル  
package2: パッケージ2ディレクトリ  
__init__.py: パッケージ2初期化ファイル  
modules.py: パッケージ2のモジュールファイル  
tox.ini: テスト実行設定ファイル  


### Cookiecutter

Cookiecutterは、Pythonプロジェクトテンプレートを生成するためのツールです。様々なテンプレートが公開されており、プロジェクトの骨格を簡単に作成することができます。

```bash
# テンプレート確認
cookiecutter --list-templates

# テンプレート選択
cookiecutter <template_name>

```

## その他
