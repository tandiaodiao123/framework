# @time: 2022/2/15 15:37
# -*- coding:utf-8 -*-
import unittest
import ddt
import os
from 接口自动化.exercise_framework.common.excelHandler import ExcelHandler
file_path = "../../data/cases.xlsx"

tester = ExcelHandler(file_path ,"Sheet1").read_data()
print(tester)
def log(name,password):
    if name=="23" and password=="1234":
        return 'success'
    else:
        return 'error'
@ddt.ddt
class TestData(unittest.TestCase):
    @ddt.data(*tester)
    def test_data_01(self,datainfo):
        name = eval(datainfo["data"])
        password = eval(datainfo["data"])
        name=name["username"]
        password=password["password"]
        expect_res = 'success'
        actual_res=log(name,password)
        self.assertTrue(expect_res==actual_res)





