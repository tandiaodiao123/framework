#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/3/19 14:55
# @Author  : datan
# @Site    : 
# @File    : Handler.py
from pymysql.cursors import DictCursor
from jsonpath import jsonpath
from Config import config
from common import looger_handler,excel_handler,yaml_handler
from common.mysql_handler import MysqlHandler
from common.requests_handler import visit


class MiddMysqlHandlerMid(MysqlHandler):

    def __init__(self):
        db = Handler.yaml_data["databases"]
        super().__init__(host=db["host"],port=db["port"],charset=db["charset"],user=db["user"],
                         password=db["password"],cursorclass=DictCursor)

#封装登录
def login():
    url = yaml_handler.read_data(config.YAML_PATH)["host"] + "/member/login"
    data = yaml_handler.read_data(config.YAML_PATH)["user"]
    res = visit(url=url,
                method="post",
                json=data,
                headers = {"X-Lemonban-Media-Type": "lemonban.v2 "}
                )
    token_info = jsonpath(res,"$..token")[0]
    token_type = jsonpath(res,"$..token_type")[0]

    token =  token_type + " " + token_info
    memer_id = jsonpath(res,"$..id")[0]

    return {"token":token,"member_id":memer_id}


class Handler():
    """初始化所有的数据。
      在其他的模块当中重复使用。
      是从 common 当中实例化对象。
      """
    conf = config

    #记录日志
    logger = looger_handler.Logger().get_logger()

    #Excel
    excel_path = conf.DATA_PATH
    excel = excel_handler.ExcelHandler(excel_path)

    #yaml
    yaml_path = conf.YAML_PATH
    yaml_data = yaml_handler.read_data(yaml_path)

    #mysql
    mysql = MiddMysqlHandlerMid

    #获取登录返回的token和member_id
    # login = login()
    @property
    def token(self):
        return login()



if __name__ == "__main__":
    res = Handler().token
    print(res)








