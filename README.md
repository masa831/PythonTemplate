# PythonTemplate
Pythonの各種テンプレートをまとめた

## pip 基本操作

```bash

% 仮想環境作成 カレントディレクトリに作成される
python -m venv envname

% 仮想環境起動
% windows
envname\Scripts\activate
% linux
source .venv/bin/activate

% 仮想環境終了
(envname)> deactivate

% pythonの場所確認
% windows
where python
% linux
which python

% 環境を外部保存
pip freeze > requirements.txt

% requirementsから環境作成
python -m pip install -r requirements.txt
python -m pip install --proxy http://xxxxxx -r requirements.txt

```

## vscode & ipynb & venv

必要パッケージをインストール
```bash
# 必要パッケージをインストール
pip install ipython ipykernel

# 仮想環境をカーネルに追加
ipython kernel install --user --name=Jupyter-kernel
```


### Vscode & pip 環境設定

仮想環境を複数作った場合は以下のようにjsonを作成する
./.vsocde/settings.json

```bash
{
    "python.defaultInterpreterPath": "D:xxx\\envname\\Scripts\\python.exe"
}
```

「pythonのインタープリター」で使用する仮想環境を切り替える


参考URL
<https://qiita.com/ozaki_physics/items/13466d6d1954a0afeb3b>
<https://helve-blog.com/posts/python/conda-virtual-environment/>


### プロキシ設定

社内NWからパッケージをインストール際にはプロキシの設定を行う必要がある。
参考URL <https://gammasoft.jp/support/pip-install-error/>

```bash

% コマンドメモ
python -m pip install --proxy http://userID:Password@yyyyyy.com xxxx

```

### requirement.txt

pipreqsを使用することで必要最低限のrequirements.txtを作成することができる。

参考URL：<https://jitaku.work/it/language/python/pipreqs/>

```bash
# 一般的な生成方法
pip freeze > requirements.txt

# pipreqs
pipreqs .
# 文字コードでエラーが出たときの対処
pipreqs --encoding=iso-8859-1 .
# フォルダを指定する場合
pipreqs --encoding=iso-8859-1 .\Streamlit

```

## 開発環境

以下のパッケージや拡張機能を用いて、静的解析環境を整備する。  
パッケージ：flake8, flake8-docstring, mypy  
vscode拡張：flake8, MypyTypeChecker  

参考：<https://qiita.com/siruku6/items/6a8412c41616b558df66>

### json設定

以下の設定はflake8をパッケージでインストールした場合の設定となる

pep8 エラーコードチートシート  
<https://qiita.com/KuruwiC/items/8e12704e338e532eb34a>  

```json
{
  　"flake8.args": [
        "--config=.config/flake8"
    ],

    "mypy-type-checker.args": [
        "--config-file=.config/mypy.ini"
    ],
}
```


## docstring (googlestyle)

```python
def func(arg1, arg2):
    """概要

    詳細説明

    Args:
        引数(arg1)の名前 (引数(arg1)の型): 引数(arg1)の説明
        引数(arg2)の名前 (:obj:`引数(arg2)の型`, optional): 引数(arg2)の説明

    Returns:
        戻り値の型: 戻り値の説明

    Raises:
        例外の名前: 例外の説明

    Yields:
        戻り値の型: 戻り値についての説明

    Examples:

        関数の使い方

        >>> func(5, 6)
        11

    Note:
        注意事項や注釈など

    """
   value = arg1 + arg2
   return value
```
