# @time: 2022/2/15 16:08
# -*- coding:utf-8 -*-
import unittest


from config import config
from libs.HTMLTestRunnerNew import HTMLTestRunner

#收集用例
loader = unittest.TestLoader()
suites = loader.discover(config.CASE_PATH)

#执行用例
with open(config.REPORET_PATH,"wb") as f:
    runner = HTMLTestRunner(f,title="练习",
                            description="练习自动化框架",
                            tester="daxi")
    runner.run(suites)


