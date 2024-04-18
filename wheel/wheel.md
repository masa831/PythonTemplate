# wheel

## whl生成方法

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

## whlインストール方法

通常のpipコマンドでインストールが可能

```bash
pip install xxx.whl
```

インストール後はpip listで確認できる。


## その他
