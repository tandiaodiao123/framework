# @time: 2022/2/13 11:52
# -*- coding:utf-8 -*-
import os
from pprint import pprint

from openpyxl import load_workbook
cwd_path = os.path.join(os.path.dirname(os.getcwd()),"data")
excel_path = os.path.join(cwd_path,"cases.xlsx")

class ExcelHandler():
    def __init__(self,file_path,sheetname):
        self.file_path=file_path
        self.sheetname = sheetname
    def open_file(self):
        wb = load_workbook(self.file_path)
        return wb
    def locate_sheet(self):
        sheet = self.open_file()[self.sheetname]
        return sheet
    def read_data(self):
        rows = list(self.locate_sheet().rows)
        # print(rows)
        # 取出title
        title = []
        excel_data = []
        for row in rows[:1]:
            for title_value in row:
                title.append(title_value.value)
        # print(title)
        # 读取数据
        for values in rows[1:]:
            my_dict = {}
            for num, data_value in enumerate(values):
                my_dict[title[num]] = data_value.value
            excel_data.append(my_dict)
        return excel_data
if __name__ == "__main__":
    tester = ExcelHandler(excel_path,"Sheet1")
    print(tester.read_data())
    pprint(tester.read_data())

