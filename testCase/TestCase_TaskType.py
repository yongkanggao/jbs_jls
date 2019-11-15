#coding=utf-8
#author_="bruce.gao"
#date:2019/10/29 16:17

import json
import unittest
from common.configHttp import RunMain
import paramunittest
from common import geturlParams, readExcel
from common.Log import logger
from common import getmySql

logger = logger
url = geturlParams.geturlParams().get_Url()
TaskType_xls = readExcel.readExcel().get_xls('case.xlsx','tasktype')
cur = getmySql.getmySql().get_MySql()
cu = cur.cursor()

@paramunittest.parametrized(*TaskType_xls)
class testTaskType(unittest.TestCase):
    """
    自定义任务
    """
    def setParameters(self,case_name,path,query,method,status_code,code,msg,sql,task,task_name,create,create_name,message):
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
        self.status_code = status_code
        self.code = str(code)
        self.msg = str(msg)
        self.sql = str(sql)
        self.task = str(task)
        self.task_name = str(task_name)
        self.create = str(create)
        self.create_name = str(create_name)
        self.message = str(message)

    def setUp(self):
        """

        :return:
        """
        print("\n" + self.case_name + ":\n\n测试开始前准备\n\n" + "接口请求数据：\n")

    def tearDown(self):
        print("测试结束\n输出log\n完结!\n\n")

    def test_checkResult(self):
        """
        check test report
        :return:
        """
        cu.execute(self.sql)
        da = cu.fetchall()

        if self.case_name.startswith("类型不关联任务"):
            task_type = da[0][0]

            get_query = json.dumps(dict(eval(self.query)))
            get_url = url + self.path
            req = RunMain().run_main(self.method, get_url, get_query.encode('utf-8'))
            data = json.loads(req.text)
            res = json.dumps(data, ensure_ascii=False, indent=1)
            print("url:" + get_url + "\n" + "query:\n" + self.query)
            print("\n接口返回数据:\n\n" + res + "\n")

        elif self.case_name.startswith("添加已有"):
            get_url = url + self.path
            req = RunMain().run_main(self.method, get_url,self.query.encode('utf-8'))
            data = json.loads(req.text)
            res = json.dumps(data, ensure_ascii=False, indent=1)
            print("url:" + get_url + "\n" + "query:\n" + self.query)
            print("\n接口返回数据:\n\n" + res + "\n")

        else:
            get_url = url + self.path
            req = RunMain().run_main(self.method, get_url, self.query.encode('utf-8'))
            data = json.loads(req.text)
            res = json.dumps(data,ensure_ascii=False,indent=1)
            print("url:" + get_url + "\n" + "query:\n" + self.query)
            print("\n接口返回数据:\n\n" + res + "\n")
            #
            # self.assertEqual(req.status_code,self.status_code)
            # self.assertEqual(data['code'],self.code)
            # self.assertEqual(data['msg'],self.msg)
            # print("结果数据为：\n" + str(req.status_code) + "," + str(data['code']) + "," + str(data['msg']))
            # print("基线数据为：\n" + str(self.status_code) + "," + str(self.code) + "," + str(self.msg) + "\n")


        logger.info(req)
        logger.info(str(self.case_name))
        logger.info(data)
        return  res

if __name__ == '__main__':
    unittest.main()