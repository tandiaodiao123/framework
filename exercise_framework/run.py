# @time: 2022/2/15 16:08
# -*- coding:utf-8 -*-

import unittest
import os
import time
from HTMLTestRunnerNew import HTMLTestRunner
loader = unittest.TestLoader()
file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),"tests/testcases")
suite = loader.discover(file_path)
dir_path = "reports/"
nowtime = time.strftime("%Y_%m_%d %H_%M_%S")
file_name = dir_path + nowtime + "Report.html"
with open(file_name,"wb") as f:
    runner = HTMLTestRunner(f,title="大喜测试",description="测试测试测试",tester="大喜")
    runner.run(suite)

