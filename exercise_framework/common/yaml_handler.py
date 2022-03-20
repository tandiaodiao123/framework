# @time: 2022/2/13 11:28
# -*- coding:utf-8 -*-
import yaml
def read_data(file):
    with open(file,encoding='utf-8') as f:
        value = yaml.load(f,Loader=yaml.SafeLoader)
        return value
def write_data(file,data):
    with open(file,"a",encoding='utf8') as f:
        yaml.dump(data,f,allow_unicode=True)
