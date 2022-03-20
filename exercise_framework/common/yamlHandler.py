# @time: 2022/2/15 15:15
# -*- coding:utf-8 -*-
import os
import yaml
yaml_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),"config/config.yaml")

def read_yaml():
    with open(yaml_path,encoding="utf8") as f:
        read_data = yaml.load(f,Loader=yaml.SafeLoader)
        return read_data
if __name__=="__main__":
    print(read_yaml())
