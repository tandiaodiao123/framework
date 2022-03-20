#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/3/13 21:40
# @Author  : datan
# @Site    : 
# @File    : mysql_handler.py
import pymysql
from pymysql.cursors import DictCursor

class MysqlHandler():
    def __init__(self,
                 host="8.129.91.152",
                 port=3306,charset='utf8',
                 user="future",password="123456",
                 cursorclass=DictCursor):
        #连接数据库
        self.con = pymysql.connect(host=host,port=port,charset=charset,user=user,password=password,cursorclass=cursorclass)
        #创建游标
        self.cursor = self.con.cursor()
    def query(self,sql,one=True):
        self.con.commit() #查询数据之前先更新一下数据
        #查询数据
        self.cursor.execute(sql)
        if one is True:
            return self.cursor.fetchone()
        return self.cursor.fetchall()
    def close(self):
        self.cursor.close()
        self.con.close()

if __name__ == "__main__":
    db = MysqlHandler()
    res = db.query("select * from futureloan.member limit 10",one=False)
    res_2 = db.query("select * from futureloan.member limit 10")
    print(res)
    print(res_2)

