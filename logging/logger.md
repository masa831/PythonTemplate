# logger

loggerのラッパーライブラリ

<https://qiita.com/ko-he-8/items/3247e16881cf9ba45c8a>

## loguru

loggerのラッパーライブラリの一つ。  
print代わりにlogを出力させることができる。  

<https://qiita.com/k8uwall/items/07ace17382b454b996a7>

## デコレータを活用したケース
→デコレータテンプレート側に格納


## ロギング設計案

- 基本設計
  - 関数単位で「入った」「出た」をログる　→ 呼び出し順序のトレースができる
  - 引数や戻り値をできる範囲でログる　→ 何が原因でバグったか推測しやすい
    - →上二つは同時にできるかも
  - エラーハンドリングは例外＋ログ　→ logger.exception() を使うとスタックトレースも出るので超便利
  - 本番ではログレベルを変えられる設計　→ logging.basicConfig(level=logging.INFO) とか起動時に変える

- dprintを使うケース
  - verbose は基本ONにはしないこと
  - 例外系のみ、基本はverbose = True