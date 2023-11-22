# WsAppTemplate

pythonプログラムをGUI化＆Exe化のテンプレートをまとめる
GUI化には"Pyside6","Tkinter"の2つのパターンを用意
Exe化には"Pyinstaller","cx_freeze"のコマンドを用意

必要ライブラリは"./envs"　に情報を格納

## GUI化

個人的所感：簡単なデスクトップアプリ程度なら、Pythonで作成で良いと思うが、
PythonのGUIパッケージを活用して、高度/大規模なアプリは向かないと感じた。

### pyside6 sampleCode

プログレスバー機能とログ機能を追加
ログ機能は対象のスクリプトの標準出力をGUI画面に随時表示する機能となっている。
ただし、以下の懸念点がある。

* ファイルをexe化後にlogファイルを手動で配置する必要がある。
* スレッドを使用している関係で、動作タイミングがずれると表示処理が最後までされないことがある。

参考サイト
<https://rikoubou.hatenablog.com/entry/2022/04/29/115254>

### Tkinter App Template

シンプルなGUI画面

参考サイト
<https://qiita.com/kotai2003/items/fe9b5e59c7164a95ded8>
<https://transcosmos-ecx.jp/blog/shopify/100>

## EXE化

### Pyinstaller

任意のスクリプトを指定して、EXE化を実行
様々オプションがあるため、詳細は別途サイトを参考にすること
基本的なコマンドは以下

```bush
% Normal
pyinstaller testTK.py --clean --onefile --noconsole --icon ./icon/penguin.ico --name TestApp

% specファイル使用パターン
pyinstaller testTK.spec
```

### cx_freeze

setup.pyファイルを別途用意し、それをビルドすることでファイルをEXE化する
基本的なコマンドは以下

```bush
python setup.py build
```

## ローカル環境名(個人用メモ)

環境名："WsApp"
