import logging
from logging import getLogger, StreamHandler, Formatter
from datetime import datetime

class CstmLogger:

    def __init__(self, output_file_flg=False,log_file=""):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)
        self.output_file_flg = output_file_flg
        self.formatter = logging.Formatter('%(asctime)s - %(message)s')
        if log_file=="":
            self.log_file = datetime.now().strftime("%Y%m%d%H%M%S") + "log.log"
        else:
            self.log_file = log_file


    def set_handler(self):
        self.handler_stream = logging.StreamHandler()
        self.handler_stream.setLevel(logging.DEBUG)
        self.handler_stream.setFormatter(self.formatter)
        self.logger.addHandler(self.handler_stream)

        if self.output_file_flg==1:
            self.handler_file = logging.FileHandler(filename=self.log_file, mode="a", encoding="utf-8")
            self.handler_file.setLevel(logging.DEBUG)
            self.handler_file.setFormatter(self.formatter)
            self.logger.addHandler(self.handler_file)

    def debug(self, message):
        self.logger.debug(message)

    def release_handler(self):
        if self.handler_stream in self.logger.handlers:
            self.logger.removeHandler(self.handler_stream)
            self.handler_stream.close()
        if self.output_file_flg==1 and self.handler_file in self.logger.handlers:
            self.logger.removeHandler(self.handler_file)
            self.handler_file.close()

