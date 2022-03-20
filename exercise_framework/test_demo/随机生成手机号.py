#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/3/18 22:35
# @Author  : datan
# @Site    : 
# @File    : 随机生成手机号.py
import random

from common import mysql_handler


def random_phone():
    # 动态生成一个手机号
    while True:
        phone = "1" + random.choice(["3", "5", "7", "9"])
        for i in range(9):
            num = random.randint(0, 9)
            phone = phone + str(num)
        # 将手机号与数据库作对比
        db = mysql_handler.MysqlHandler()
        phone_record = db.query("select * from futureloan.member where mobile_phone={}".format(phone))
        # 如果生成的手机号在数据库不存在，就返回phone
        if not phone_record:
            db.close()
            return phone
        db.close()

phone_res = random_phone()
print(phone_res)

