#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/3/6 18:49
# @Author  : datan
# @Site    : 
# @File    : config.py

import os
import time
#目录路径
DIR_PATH = os.path.dirname(os.path.abspath(__file__))

#根目录路径
ROOT_PATH = os.path.dirname(DIR_PATH)

#用例路径

CASE_PATH =os.path.join(ROOT_PATH,"tests")

#报告路径
date_time = time.strftime("%Y-%m-%d-%H-%M-%S")
file_path = "{}Reports.html".format(date_time)
REPORET_PATH = os.path.join(os.path.join(ROOT_PATH,"reports"),file_path)

#测试数据路径
DATA_PATH = os.path.join(ROOT_PATH,"data\\cases.xlsx")

#yaml文件的配置路径
YAML_PATH = os.path.join(ROOT_PATH,"data\log_config.yaml")

#logs的收集路径
log_time = time.strftime("%Y-%m-%d %H-%M-%S")
log_path = "{} logs.txt".format(log_time)
LOG_PATH = os.path.join(os.path.join(ROOT_PATH,"logs"),log_path)



