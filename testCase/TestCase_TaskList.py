#coding=utf-8
#author_="bruce.gao"
#date:2019/9/27 14:59

import json
import unittest
from common.configHttp import RunMain
import paramunittest
from common import geturlParams, readExcel


url = geturlParams.geturlParams().get_Url()# 调用我们的geturlParams获取我们拼接的URL
taskList_xls = readExcel.readExcel().get_xls('case.xlsx','task')

@paramunittest.parametrized(*taskList_xls)
class testTaskList(unittest.TestCase):
    def setParameters(self, case_name, path, query, method):
        """
        set params
        :param case_name:
        :param path
        :param query
        :param method
        :return:
        """
        self.case_name = str(case_name)
        self.path = str(path)
        self.query = str(query)
        self.method = str(method)

    def description(self):
        """
        test report description
        :return:
        """
        self.case_name

    def setUp(self):
        """

        :return:
        """
        print(self.case_name+"测试开始前准备")

    def taskList(self):
        self.test_checkResult()

    def tearDown(self):
        print("测试结束，输出log完结\n\n")

    def test_checkResult(self):# 断言
        """
        check test report
        :return:
        """
        get_url = url +self.path
        info = RunMain().run_main(self.method, get_url, self.query)# 根据Excel中的method调用run_main来进行requests请求，并拿到响应
        data = json.loads(info.text)
        res = json.dumps(data,ensure_ascii=False,indent=1)
        self.assertEqual(info.status_code,200)
        self.assertEqual(data['code'],"Joybos.2112")
        # print(data)
        return  res


if __name__ == "__main__":
    unittest.main()