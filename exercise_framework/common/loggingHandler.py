# @time: 2022/2/13 11:52
# -*- coding:utf-8 -*-
import logging
import os
import time
from 接口自动化.exercise_framework.common.yamlHandler import read_yaml
dir_path = "../logs/"
nowtime = time.strftime("%Y_%m_%d %H_%M_%S")
file_path = dir_path + nowtime + "用例日志.txt"
# file_path = os.path.join(os.path.dirname(os.getcwd()),"logs/用例收集日志.txt")
data = read_yaml()
log_name = data["log"]["log_name"]
log_levl = data["log"]["level"]
print(data)
# print(file_path)

class LoggingHandler():
    def __init__(self,file_path,log_name=log_name,level=log_levl):
        self.logname = log_name
        self.level = level
        self.file_path = file_path
        self.fmt = '%(asctime)s--%(filename)s--hanghao:%(lineno)d--%(levelname)s:%(message)s'
    #获取日志收集器
    def get_logger(self):
        logger = logging.getLogger(self.logname)
        logger.setLevel(self.level)
        self.logger = logger
        self.set_fmt()
        return logger
    def get_streamhandler(self):
        streamHanler = logging.StreamHandler()
        streamHanler.setLevel(self.level)
        self.logger.addHandler(streamHanler)
        return streamHanler
    def get_fileHandler(self):
        fileHandler = logging.FileHandler(self.file_path)
        fileHandler.setLevel(self.level)
        self.logger.addHandler(fileHandler)
        return fileHandler
    def set_fmt(self):
        fmt = logging.Formatter(self.fmt)
        self.get_streamhandler().setFormatter(fmt)
        self.get_fileHandler().setFormatter(fmt)
if __name__ == "__main__":
    logger = LoggingHandler(file_path).get_logger()
    logger.info("this is info")
    logger.debug("this is debug")
    logger.error("this is error")
