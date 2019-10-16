#coding=utf-8
#author_="bruce.gao"
#date:2019/10/10 16:11


import unittest
import json
import paramunittest
from common import geturlParams,readExcel
from common.configHttp import RunMain
from common import getmySql
from common.Log import logger
import time

logger = logger
url = geturlParams.geturlParams().get_Url()
TaskNode_xls = readExcel.readExcel().get_xls('case.xlsx','tasknode')
cur = getmySql.getmySql().get_MySql()
cu = cur.cursor()

@paramunittest.parametrized(*TaskNode_xls)
class testTaskNode(unittest.TestCase):
    """
    任务流程！
    """

    def setParameters(self,case_name,path,query,method,status_code,code,msg,commit,sql,status,reliys,comment,task_node,tasknodenum):
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
        self.commit = str(commit)
        self.sql = str(sql)
        self.status = status
        self.reliys = str(reliys)
        self.comment = str(comment)
        self.task_node = str(task_node)
        self.tasknodenum = tasknodenum

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

        if self.case_name == "任务详情":
            get_url = url + self.path + "/" + task_id
            req = RunMain().run_main(self.method, get_url, self.query)
            data = json.loads(req.text)
            res = json.dumps(data, ensure_ascii=False, indent=1)
            print("url:" + get_url + "\n" + "query:\n" + self.query)
            print("\n接口返回数据:\n\n" + res + "\n")

            self.assertEqual(req.status_code, self.status_code)
            self.assertEqual(data['code'], self.code)
            self.assertEqual(data['msg'], self.msg)
            self.assertEqual(data['data']['status'], self.status)
            self.assertEqual(eval(self.reliys), self.comment)
            self.assertEqual(eval(self.task_node), self.tasknodenum)
            time.sleep(1)

        else:
            get_url = url + "/tasks/" + task_id + self.path
            req = RunMain().run_main(self.method, get_url, self.query.encode('utf-8'))
            data = json.loads(req.text)
            res = json.dumps(data, ensure_ascii=False, indent=1)
            print("url:" + get_url + "\n" + "query:\n" + self.query)
            print("\n接口返回数据:\n\n" + res + "\n")

            self.assertEqual(req.status_code, self.status_code)
            self.assertEqual(data['code'], self.code)
            self.assertEqual(data['msg'], self.msg)
            self.assertEqual(data['data']['commit'], self.commit)
            time.sleep(1)

        logger.info(req)
        logger.info(str(self.case_name))
        logger.info(data)
        return res

if __name__ == '__main__':
    unittest.main()