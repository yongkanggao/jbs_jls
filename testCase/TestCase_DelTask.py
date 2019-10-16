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
    删除任务！
    """

    def setParameters(self,case_name,path,query,method,sql,status_code,code,msg):
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
        self.status_code = int(status_code)
        self.code = str(code)
        self.msg = str(msg)

    def setUp(self):
        """

        :return:
        """
        print("\n" + self.case_name + ":\n\n测试开始前准备\n\n" + "接口返回数据：\n")

    def tearDown(self):
        print("测试结束\n输出log\n完结!\n\n")

    def test_checkResult(self):
        cu.execute(self.sql)
        da = cu.fetchall()
        # print(len(data[0][0]))
        if len(da[0][0]) != 0:
            task_id = da[0][0]
        else:
            print("没有查到数据")
        # cu.close()

        get_url = url + "/tasks/" + task_id + self.path
        req = RunMain().run_main(self.method,get_url,self.query)
        data = json.loads(req.text)
        res = json.dumps(data,ensure_ascii=False,indent=1)
        print("url:" + get_url + "\n" + "query:\n" + self.query)
        print("\n接口返回数据:\n\n" + res + "\n")

        self.assertEqual(req.status_code,self.status_code)
        self.assertEqual(data['code'],self.code)
        self.assertEqual(data['msg'],self.msg)
        self.assertEqual(data['data'],task_id)

        logger.info(req)
        logger.info(str(self.case_name))
        logger.info(data)
        return res

if __name__ == '__main__':
    unittest.main()