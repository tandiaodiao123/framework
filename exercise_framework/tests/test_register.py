import unittest
import random

import ddt
import json
from common.requests_handler import visit
from middlerware.Handler import Handler

logger = Handler.logger
test_data = Handler.excel

@ddt.ddt
class TestRegister(unittest.TestCase):
    @ddt.data(*test_data)
    def testregister(self,case_info):
        #手机号需要在接口请求前就完成替换
        # 判断测试用例数据有没有 #phone#, 如果有，就要替换成动态生成的手机号码。
        if "#phone#" in case_info["data"]:
            phone = self.random_phone()  #获取到动态生成的手机号
            case_info["data"] = case_info["data"].replace("#phone#",phone)

        #访问接口
        data = json.loads(case_info["data"])
        resp = visit(
            url=case_info["url"],
            method=case_info["method"],
            json=data,
            headers=json.loads(case_info["headers"])
        )
        #断言
        expected_dict = json.loads(case_info["expected"])
        try:
            for k, v in expected_dict.items():
                    # logger.info("正在断言")
                    self.assertEqual(v, resp[k])
            if resp["code"] == 0:
                    db = Handler.mysql()

                    sql_code = "select * from futureloan.member where mobile_phone={} limit 10".format(data["mobile_phone"])
                    user = db.query(sql_code)
                    self.assertTrue(user)
            logger.info("测试用例通过")
        except Exception as e :
            logger.error("测试用例无法通过{}".format(e))
            raise e

    def random_phone(self):
        #动态生成一个手机号
        phone = "18"
        for i in range(9):
            num = random.randint(0, 9)
            phone = phone + str(num)
        #将手机号与数据库作对比
        db = Handler.mysql()

        phone_record = db.query("select * from futureloan.member where mobile_phone={}".format(phone))
        #如果生成的手机号在数据库不存在，就返回phone
        if not phone_record:
            db.close()
            return phone
        db.close()



