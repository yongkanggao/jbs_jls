#coding=utf-8
#author_="bruce.gao"
#date:2019/10/8 17:20

import unittest
import json
import paramunittest
from common import geturlParams,readExcel
from common.configHttp import RunMain
from common import getmySql
from common.Log import logger

logger = logger
url = geturlParams.geturlParams().get_Url()
Deltask_xls = readExcel.readExcel().get_xls('case.xlsx','deletetask')
cur = getmySql.getmySql().get_MySql()
cu = cur.cursor()

@paramunittest.parametrized(*Deltask_xls)
class testDelTask(unittest.TestCase):
    """
    删除任务
    """

    def setParameters(self, case_name, path, query, method, sql):
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
        self.sql = str(sql)

    def setUp(self):
        """

        :return:
        """
        print("\n" + self.case_name + ":\n\n测试开始前准备")

    def tearDown(self):
        print("测试结束，输出log完结\n\n")

    def test_checkResult(self):
        cu.execute(self.sql)
        data = cu.fetchall()
        # print(len(data[0][0]))
        if len(data[0][0]) != 0:
            task_id = data[0][0]
        else:
            print("没有查到数据")
        # cu.close()

        get_url = url + "/tasks/" + task_id + self.path
        req = RunMain().run_main(self.method,get_url,self.query)
        da = json.loads(req.text)
        res = json.dumps(da,ensure_ascii=False,indent=1)
        self.assertEqual(req.status_code,200)
        self.assertEqual(da['code'],'Joybos.2112')
        self.assertEqual(da['msg'],'success')

        logger.info(req)
        logger.info(str(self.case_name))
        logger.info(da)
        # print(res)
        return res

if __name__ == '__main__':
    unittest.main()