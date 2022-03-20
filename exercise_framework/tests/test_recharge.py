"""充值需要用到登录成功后返回的token值"""


import unittest
import ddt
import json
from common.requests_handler import visit
from middlerware.Handler import Handler
from decimal import Decimal

recharge_data = Handler.excel.read_data("recharge")
logger = Handler.logger
@ddt.ddt()
class TestRecharge(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.token = Handler().token["token"]
        cls.member_id = Handler().token["member_id"]

    def setUp(self) -> None:
        #打开数据库
        self.db= Handler.mysql()
    def tearDown(self) -> None:
        #关闭数据库
        self.db.close()

    @ddt.data(*recharge_data)
    def test_recharge(self,case):

        headers = case["headers"]
        if "#Token#" in headers:

            headers = headers.replace("#Token#",self.token)

        data = case["data"]
        if "#member_id#" in data:
            data = data.replace("#member_id#",str(self.member_id))

        headers = json.loads(headers)
        data = eval(data)

        #查询充值前的金额数据
        sql_code = ("select leave_amount from futureloan.member where id = {}".format(self.member_id))
        before_money = self.db.query(sql_code)["leave_amount"]
        print(type(before_money))


        res = visit(

            url=Handler.yaml_data["host"] + "/member/recharge",
            method = "post",
            json=data,
            headers = headers
        )

        #查询请求之后的金额数据
        if res["code"] == 0:
            after_money = self.db.query(sql_code)["leave_amount"]

            self.assertTrue(before_money + Decimal(str(data["amount"])) == after_money)


        # 断言
        try:
            expected = json.loads(case["expected"])
            for key,value in expected.items():
                self.assertEqual(value,res[key])
            logger.info("测试用例通过")
        except Exception as e:
            logger.error("测试用例不通过{}".format(e))
            raise e






