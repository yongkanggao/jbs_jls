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

    def setUp(self):
        """

        :return:
        """
        print(self.case_name + ":\n测试开始前准备")

    def tearDown(self):
        print("测试结束，输出log完结\n\n")

    def test_checkResult(self):
        """
        check test report
        :return:
        """
        get_url = url + self.path
        req = RunMain().run_main(self.method, get_url, self.query)# 根据Excel中的method调用run_main来进行requests请求，并拿到响应
        data = json.loads(req.text)
        res = json.dumps(data,ensure_ascii=False,indent=1)

#进行中的任务列表的校验
        if self.case_name == "进行中任务列表显示":
            self.assertEqual(req.status_code,200)
            self.assertEqual(data['code'],"Joybos.2112")
            self.assertEqual(data['msg'],'success')
            self.assertLessEqual(data['data']['list'][0]['end_date'],data['data']['list'][1]['end_date'])
        if self.case_name == "进行中任务筛选_标题":
            self.assertEqual(req.status_code, 200)
            self.assertEqual(data['code'], "Joybos.2112")
            self.assertEqual(data['msg'], 'success')
            self.assertLessEqual(data['data']['list'][0]['end_date'], data['data']['list'][1]['end_date'])
        if self.case_name == "进行中任务筛选_角色":
            self.assertEqual(req.status_code, 200)
            self.assertEqual(data['code'], "Joybos.2112")
            self.assertEqual(data['msg'], 'success')
            self.assertLessEqual(data['data']['list'][0]['end_date'], data['data']['list'][1]['end_date'])
        if self.case_name == "进行中任务筛选_进度":
            self.assertEqual(req.status_code, 200)
            self.assertEqual(data['code'], "Joybos.2112")
            self.assertEqual(data['msg'], 'success')
            self.assertLessEqual(data['data']['list'][0]['end_date'], data['data']['list'][1]['end_date'])
        if self.case_name == "进行中任务筛选_时间":
            self.assertEqual(req.status_code,200)
            self.assertEqual(data['code'],"Joybos.2112")
            self.assertEqual(data['msg'],'success')
            self.assertLessEqual(data['data']['list'][0]['end_date'],data['data']['list'][1]['end_date'])

#已完成任务列表的校验
        if self.case_name == "已完成任务列表显示":
            self.assertEqual(req.status_code, 200)
            self.assertEqual(data['code'], "Joybos.2112")
            self.assertEqual(data['msg'], 'success')
            self.assertGreaterEqual(data['data']['list'][0]['end_date'], data['data']['list'][1]['end_date'])
        if self.case_name == "已完成任务筛选_标题":
            self.assertEqual(req.status_code, 200)
            self.assertEqual(data['code'], "Joybos.2112")
            self.assertEqual(data['msg'], 'success')
            self.assertGreaterEqual(data['data']['list'][0]['end_date'], data['data']['list'][1]['end_date'])
        if self.case_name == "已完成任务筛选_角色":
            self.assertEqual(req.status_code, 200)
            self.assertEqual(data['code'], "Joybos.2112")
            self.assertEqual(data['msg'], 'success')
            self.assertGreaterEqual(data['data']['list'][0]['end_date'], data['data']['list'][1]['end_date'])
        if self.case_name == "已完成任务筛选_进度":
            self.assertEqual(req.status_code, 200)
            self.assertEqual(data['code'], "Joybos.2112")
            self.assertEqual(data['msg'], 'success')
            self.assertGreaterEqual(data['data']['list'][0]['end_date'], data['data']['list'][1]['end_date'])
        if self.case_name == "已完成任务筛选_时间":
            self.assertEqual(req.status_code, 200)
            self.assertEqual(data['code'], "Joybos.2112")
            self.assertEqual(data['msg'], 'success')
            self.assertGreaterEqual(data['data']['list'][0]['end_date'], data['data']['list'][1]['end_date'])

        logger.info(req)
        logger.info(str(self.case_name))
        logger.info(data)
        #print(res)
        return  res


if __name__ == "__main__":
    unittest.main()