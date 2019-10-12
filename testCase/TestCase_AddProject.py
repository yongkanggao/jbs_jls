#coding=utf-8
#author_="bruce.gao"
#date:2019/10/11 19:13

import unittest
import json
import paramunittest
from common import geturlParams,readExcel
from common.configHttp import RunMain
from common import getmySql
from common.Log import logger

logger = logger
url = geturlParams.geturlParams().get_Url()
addProject_xls = readExcel.readExcel().get_xls('case.xlsx','addproject')
cur = getmySql.getmySql().get_MySql()
cu = cur.cursor()

@paramunittest.parametrized(*addProject_xls)
class testAddProject(unittest.TestCase):
    """
    新增项目！
    """

    def setParameters(self,case_name,path,query,method,status_code,code,msg,sql):
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
        self.sql = str(sql)

    def setUp(self):
        """

        :return:
        """
        print("\n" + self.case_name + ":\n\n测试开始前准备\n")

    def tearDown(self):
        print("测试结束\n输出log\n完结!\n\n")

    def test_checkResult(self):
        cu.execute(self.sql)
        da = cu.fetchall()

        task_id1 = da[0][0]
        task_id2 = da[1][0]
        get_url = url + self.path
        get_query = json.dumps(dict(eval(self.query)))
        req = RunMain().run_main(self.method, get_url, get_query.encode('utf-8'))
        data = json.loads(req.text)
        res = json.dumps(data, ensure_ascii=False, indent=1)
        self.assertEqual(req.status_code, self.status_code)
        self.assertEqual(data['code'], self.code)
        self.assertEqual(data['msg'], self.msg)

        logger.info(req)
        logger.info(str(self.case_name))
        logger.info(data)
        # print(res)
        return res


if __name__ == '__main__':
    unittest.main()