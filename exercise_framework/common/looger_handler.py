# @time: 2022/2/10 14:10
# -*- coding:utf-8 -*-
import logging

from config import config
from common import yaml_handler

data = yaml_handler.read_data(config.YAML_PATH)
class Logger():
    def __init__(self,name = data["log"]["name"],level=data["log"]["level"]):
        self.name = name
        self.level = level
        self.fmt='%(asctime)s--%(filename)s--hanghao:%(lineno)d--%(levelname)s:%(message)s'
    #收集日志
    def get_logger(self):
        logger = logging.getLogger(self.name)
        logger.setLevel(self.level)
        self.logger=logger
        self.log_fmt()
        return logger

    #输出日志到控制台
    def streamHandler(self):
        stram_handler = logging.StreamHandler()
        stram_handler.setLevel(self.level)
        self.logger.addHandler(stram_handler)
        return stram_handler
    #输出日志到文件中
    def fileHandler(self):
        file_handler = logging.FileHandler(config.LOG_PATH)
        file_handler.setLevel(self.level)
        self.logger.addHandler(file_handler)
        self.file_handler = file_handler
        return file_handler
    #输出日志的文件格式
    def log_fmt(self):
        fmt = logging.Formatter(self.fmt)
        stram_handler = self.streamHandler()
        file_handler = self.fileHandler()
        stram_handler.setFormatter(fmt)
        file_handler.setFormatter(fmt)

if __name__ == "__main__":
    # data = yaml_handler.read_data(config.YAML_PATH)
    # name = data["log"]["name"]
    # level = data["log"]["level"]
    logger = Logger().get_logger()
    logger.info("这是信息")
    logger.debug("这是调试")
    logger.error("这是错误")

