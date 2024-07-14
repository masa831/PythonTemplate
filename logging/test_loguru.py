from loguru import logger


def main():
    # logger.add("logtest.log")  # ファイル出力
    logger.trace("トレース")
    logger.debug("デバッグ")
    logger.info("情報")
    logger.success("成功")
    logger.warning("警告")
    logger.error("エラー")
    logger.critical("クリティカル")


if __name__ == '__main__':
    main()
