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

## 開発環境

注意：flake8,mypyなどはパッケージをインストールする場合と拡張機能を使う場合とで設定が異なる

### 関数ヒント

<https://zenn.dev/yamasakit/articles/dc9ed1acd5ae3b>
<https://zenn.dev/k0kishima/articles/5466aaeb57be7a>

### pep8

以下の設定はflake8をパッケージでインストールした場合の設定となる

pep8 エラーコードチートシート  
<https://qiita.com/KuruwiC/items/8e12704e338e532eb34a>  

詳細設定（settings.json）
VSCodeの settings.json ファイルで、flake8の詳細設定を行うことができます。  
以下の手順で設定ファイルを開きます。

Code メニューを開き、「設定」 を選択します。  
左側のメニューで 「ワークスペース設定」 を選択します。  
右側のエディタに settings.json と入力し、Enterキーを押します。  
settings.json ファイルが開いたら、以下の例のように設定を追加できます。  

```json
{
  // ... 他の設定 ...

  "python.flake8.enabled": true,              // Flake8を有効にする
  "python.flake8.runOnSave": true,           // コード保存時に自動チェックを実行
  "python.flake8.exclude": [                 // チェック対象から除外するファイルパス
    ".git",
    "node_modules",
  ],
  "python.flake8.ignore": [                   // 無視するエラー・警告コード
    "E126",
    "W391",
  ],
  "python.flake8.args": [                    // Flake8に渡す引数
    "--show-source",
    "--statistics",
  ],
  "python.flake8.useStandardConfiguration": false, // 標準設定を使用しない
  "python.flake8.customConfigurationFile": "/path/to/flake8.cfg", // カスタム設定ファイルのパス
}
```

設定項目の説明

python.flake8.enabled: Flake8を有効にするかどうかを設定します。  
python.flake8.runOnSave: コード保存時に自動的にチェックを実行するかどうかを設定します。  
python.flake8.exclude: チェック対象から除外するファイルパスのリストを設定します。  
python.flake8.ignore: 無視するエラー・警告コードのリストを設定します。  
python.flake8.args: Flake8に渡す引数をリスト形式で設定します。  
python.flake8.useStandardConfiguration: 標準設定を使用するかどうかを設定します。false に設定すると、python.flake8.customConfigurationFile で指定したカスタム設定ファイルを使用します。  
python.flake8.customConfigurationFile: カスタム設定ファイルのパスを設定します。  

詳細設定例

特定のディレクトリ以下のファイルをチェック対象から除外する  
```json
"python.flake8.exclude": [
  ".git",
  "node_modules",
  "**/tests/*"
]

特定のエラー・警告コードを無視する

```json
"python.flake8.ignore": [
  "E126",  // 行末に空白がない
  "W391",  // 単一行の`import`ステートメント
]
```

flake8.cfg ファイルでカスタム設定を行う

プロジェクトディレクトリに flake8.cfg ファイルを作成します。  
以下の例のように設定を記述します。  

```ini
Ini, TOML
[flake8]
select = E,W,F
max-line-length = 100
exclude = .git,node_modules
```

settings.json で python.flake8.useStandardConfiguration を false に設定し、python.flake8.customConfigurationFile で flake8.cfg ファイルのパスを設定します。
```json
{
  // ... 他の設定 ...

  "python.flake8.enabled": true,
  "python.flake8.runOnSave": true,
  "python.flake8.useStandardConfiguration": false,
  "python.flake8.customConfigurationFile": "flake8.cfg",
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