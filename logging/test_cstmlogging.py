import cstm_logging

# cstm_loggingクラスのテストコード

if __name__ == "__main__":
    # 標準出力のみ
    log = cstm_logging.CstmLogger() # 標準出力のみ
    # 標準出力 & ファイル出力　ファイル名はデフォルト定義
    # log = cstm_logging.CstmLogger(output_file_flg=True)
    # 標準出力 & ファイル出力　ファイル名を指定
    # log = cstm_logging.CstmLogger(output_file_flg=True, log_file="test.log")

    log.set_handler()
    log.debug("hello")
    log.debug("日本語文字化けの確認用：[林檎, 檸檬, 葡萄]")
    log.debug("world")
    log.release_handler()
