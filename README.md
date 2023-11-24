# PythonTemplate
Pythonの各種テンプレートをまとめた

## 概要

## 環境設定

環境名：enviroment

### pip 基本操作

```bash

% 仮想環境作成 カレントディレクトリに作成される
python -m venv envname

% 仮想環境起動
envname\Scripts\activate

% 仮想環境終了
(envname)> deactivate

% pythonの場所確認
where python

% 環境を外部保存
pip freeze > requirements.txt

% requirementsから環境作成
python -m pip install -r requirements.txt
python -m pip install --proxy http://userID:Password@hg-vm-prx-sdc.t.rd.honda.com:8080 -r requirements.txt

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

