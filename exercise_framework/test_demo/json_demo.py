#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/3/13 10:03
# @Author  : datan
# @Site    : 
# @File    : json_demo.py
import json
#json串必须是有双引号包裹起来的
# my_info = {"name":"大喜","sex":"girl"}

#特殊值 null，true
#在python字典里，为空的表示是None,TRUE与FALSE都是大写，而在json串里，true与false都必须是小写,除非None,TRUE,FALSE有双引号包裹起来


# my_mes = '{"food":null}'
# print(type(my_mes))

#json 序列化

#将json转换为python
# my_hooby = '{"name":"daxi","hobby":"majiang"}'
# res = json.loads(my_hooby)
# print(my_hooby)
# print(res)

# my_info = '{"house":null,"age":false,"sex":true}'
# new_my_info = json.loads(my_info)
# print(my_info)
# print(new_my_info)


#将python对象转为json串
# python_01 = {'name':'大喜','age':True,'sex':False,"money":None}
# json_data = json.dumps(python_01,ensure_ascii=False)
# print(type(python_01))
# print(type(json_data))

python_02 = {'name':'大喜','age':True,'sex':False,"money":None}
#默认遍历出key
# for i in python_02:
#     print(i)

# for i in python_02.values():
#     print(i)

# print(type(python_02.items()))
# for k,v in python_02.items():
#     print(k,v)

# python_01 = {'name':'大喜','age':True,'sex':False,"money":None}
# # python_03= {"name": "大喜", "age": "true", "sex": "false", "money": "null"}
# json_data = json.dumps(python_01,ensure_ascii=False)
# print(type(python_01))
# print(json_data)

# print(type(python_03))


# json_data = {"num":float(300)}
# print(json_data)
# json_t = json.loads(json_data)
#
# print(json_t)



json_data = '{"amount":-600}'
json_trans = json.loads(json_data)
print(json_trans)
