
import unittest
import ddt

from common.requests_handler import visit
from middlerware.Handler import Handler
import json

env = Handler()
logger = Handler.logger
login_data = env.excel.read_data("login")

@ddt.ddt
class TestLogin(unittest.TestCase):

    @ddt.data(*login_data)

    def test_login(self,case):
        data =json.loads(case["data"])
        res = visit(
            url = case["url"],
            method=case["method"],
            json=data,
            headers = json.loads(case["headers"])
        )
        expected = json.loads(case["expected"])
        for key,value in expected.items():
            self.assertEqual(value,res[key])
        logger.info("测试用例通过")

