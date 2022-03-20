import openpyxl


class ExcelHandler:

    def __init__(self, file_path):
        """初始化"""
        self.file_path = file_path
        # self.open_file()

    def open_file(self):
        """打开文件"""
        workbook = openpyxl.load_workbook(self.file_path)
        self.workbook = workbook
        return workbook

    def get_sheet(self, name):
        """获取表格"""
        workbook = self.open_file()
        # print("获取表格：{}".format(name))
        return workbook[name]

    def read_data(self, name):
        """读取数据. 每一行数据存放到列表或者是字典当中。"""
        sheet = self.get_sheet(name)
        # print("读取读取")
        rows = list(sheet.rows)

        data = []
        # 获取标题
        headers = []
        for title in rows[0]:
            headers.append(title.value)

        # 添加数据
        for row in rows[1:]:
            row_data = {}

            for idx, cell in enumerate(row):
                row_data[headers[idx]] = cell.value

            data.append(row_data)

        self.close()

        return data

    def write(self, sheet_name, row, column, data):
        """写入单元格数据"""
        sheet = self.get_sheet(sheet_name)
        sheet.cell(row, column).value = data
        self.save()
        self.close()

    def save(self):
        self.workbook.save(self.file_path)

    def close(self):
        # print("关闭文件：{}".format(self.file_path))
        self.workbook.close()


if __name__ == '__main__':
    excel = ExcelHandler("cases.xlsx")
    # print(excel.get_sheet('Sheet1'))

    print(excel.read_data('Sheet1'))
