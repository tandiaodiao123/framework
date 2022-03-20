#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/3/13 11:21
# @Author  : datan
# @Site    : 
# @File    : mysql.py

#安装pymysql
import pymysql
from  pymysql.cursors import DictCursor
#连接数据数据库
con = pymysql.connect(host="8.129.91.152",port=3306,user="future",charset='utf8',password="123456",cursorclass=DictCursor)

#建立游标
cursor = con.cursor()
cursor_2 = con.cursor()
print(cursor)

#执行SQL语句

cursor.execute("select * from futureloan.member limit 10")
cursor_2.execute("select * from futureloan.member limit 10")



#得到查询数据
# res = cursor.fetchall()
# res_2= cursor_2.fetchone()
# print(res)
# print(res_2)

#关闭游标
cursor.close()
#关闭连接
con.close()


