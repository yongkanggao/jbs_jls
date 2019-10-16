#coding=utf-8
#author_="bruce.gao"
#date:2019/9/27 14:59

import json
import unittest
from common.configHttp import RunMain
import paramunittest
from common import geturlParams, readExcel
from common.Log import logger

logger = logger
url = geturlParams.geturlParams().get_Url()
taskList_xls = readExcel.readExcel().get_xls('case.xlsx','tasklist')

@paramunittest.parametrized(*taskList_xls)
class testTaskList(unittest.TestCase):
    """
    任务列表！
    """
    def setParameters(self,case_name,path,query,method,status_code,code,msg,data1,data2):
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
        self.status_code = int(status_code)
        self.code = str(code)
        self.msg = str(msg)
        self.data1 = str(data1)
        self.data2 = str(data2)

    def setUp(self):
        """

        :return:
        """
        print("\n" + self.case_name + ":\n\n测试开始前准备\n\n" + "接口返回数据：\n")

    def tearDown(self):
        print("测试结束\n输出log\n完结!\n\n")

    def test_checkResult(self):
        """
        check test report
        :return:
        """
        get_url = url + self.path
        req = RunMain().run_main(self.method, get_url, self.query)# 根据Excel中的method调用run_main来进行requests请求，并拿到响应
        data = json.loads(req.text)
        res = json.dumps(data,ensure_ascii=False,indent=1)
        print("url:" + get_url + "\n" + "query:\n" + self.query)
        print("\n接口返回数据:\n\n" + res + "\n")

        self.assertEqual(req.status_code,self.status_code)
        self.assertEqual(data['code'], self.code)
        self.assertEqual(data['msg'],self.msg)
        self.assertLessEqual(eval(self.data1),eval(self.data2))  #去除字符的双引号，断言


        logger.info(req)
        logger.info(str(self.case_name))
        logger.info(data)
        return  res


if __name__ == "__main__":
    unittest.main()