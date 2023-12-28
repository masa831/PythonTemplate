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

## openpyxlについて

#### 読み込みオプションとセル内の関数について

Excel内のセルに計算式が埋め込まれている場合、基本的にはload_workbook()のオプション"data_only=True"とすることで計算結果を取得できる。
しかし、Excelの仕様上、関数の計算式は開いたときに更新されるため、ツール等で自動処理した際には、値が再評価されていない状態となっている。
そのような計算式が更新されていない状態では、openpyxlでは、値を取得できない。("None"となる。)
よって、上記の状況の対処法として、マージ処理実行前に取得した機能ファイルは保存し直す処理を入れている。

参考URL
<https://buzz-server.com/tech/python-openpyxl-no-value-cause/>
<https://teratail.com/questions/328690>

#### 結合セルのコピーについて

openpyxlは、結合セルに対して、"左上だけが書き換え可能、それ以外は読み取り専用"という振る舞いをする。
よって、例えば、コピー処理をする際に、コピー元ファイルの任意のセルが結合セルではなく、値が入っており、
コピー先ファイルでは、結合セルとなっており、かつ結合の先頭セルではない場合にはエラーが出る。
コピー元、先で結合セルが範囲がずれている＆値が異なっている場合はエラーとなる。

#### セルのコメントのサイズについて

Excelファイルに対して、プログラム実行後は処理にかかわらず、セルのコメントボックスサイズと位置が初期化されてしまう。  
ファイルのデータを読み込む際にもセルのコメントボックスサイズなどのデータは取得することができないため、
コメントを新たに生成する場合のみ、サイズを指定できる状態となっている。
→openpyxl自体がこのあたりの処理に対応してないようで、現状思いつく解決策はVBAとPythonの組み合わせ。できるかは不明

