#coding=utf-8
#author_="bruce.gao"
#date:2019/10/12 12:22

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
ProjectNode_xls = readExcel.readExcel().get_xls('case.xlsx','projectnode')
cur = getmySql.getmySql().get_MySql()
cu = cur.cursor()

@paramunittest.parametrized(*ProjectNode_xls)
class testProjectNode(unittest.TestCase):
    """
    项目流程！
    """

    def setParameters(self,case_name,path,query,method,status_code,code,msg,commit,sql,status,reliys,comment,task_node,tasknodenum,category,title):
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
        self.title = str(title)
        self.category = category
        self.status = status
        self.reliys = str(reliys)
        self.comment = str(comment)
        self.task_node = str(task_node)
        self.tasknodenum = tasknodenum
        self.commit = str(commit)

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

        if self.case_name == "项目详情":
            project_id = da[0][0]
            get_url = url + self.path + "?id=" + project_id
            req = RunMain().run_main(self.method, get_url,self.query)
            data = json.loads(req.text)
            res = json.dumps(data, ensure_ascii=False, indent=1)
            self.assertEqual(req.status_code, self.status_code)
            self.assertEqual(data['code'], self.code)
            self.assertEqual(data['msg'], self.msg)
            self.assertEqual(data['data']['taskEntity']['title'],self.title)

        elif self.case_name == "项目子任务详情":
            task_id1 = da[0][0]
            category_id = da[1][0]
            get_url = url + self.path + "/" + task_id1
            req = RunMain().run_main(self.method, get_url, self.query)
            data = json.loads(req.text)
            res = json.dumps(da, ensure_ascii=False, indent=1)
            self.assertEqual(req.status_code, self.status_code)
            self.assertEqual(data['code'], self.code)
            self.assertEqual(data['msg'], self.msg)
            self.assertEqual(float(category_id), self.category)
            self.assertEqual(data['data']['title'],self.title)

        elif self.case_name == "任务详情":
            task_id = da[0][0]
            get_url = url + self.path + "/" + task_id
            req = RunMain().run_main(self.method, get_url, self.query)
            data = json.loads(req.text)
            res = json.dumps(da, ensure_ascii=False, indent=1)
            self.assertEqual(req.status_code, self.status_code)
            self.assertEqual(data['code'], self.code)
            self.assertEqual(data['msg'], self.msg)
            self.assertEqual(data['data']['status'], self.status)
            self.assertEqual(eval(self.reliys), self.comment)
            self.assertEqual(eval(self.task_node), self.tasknodenum)
            time.sleep(1)

        else:
            task_id = da[0][0]
            get_url = url + "/tasks/" + task_id + self.path
            req = RunMain().run_main(self.method, get_url, self.query.encode('utf-8'))
            data = json.loads(req.text)
            res = json.dumps(da, ensure_ascii=False, indent=1)
            self.assertEqual(req.status_code, self.status_code)
            self.assertEqual(data['code'], self.code)
            self.assertEqual(data['msg'], self.msg)
            self.assertEqual(data['data']['commit'], self.commit)
            time.sleep(1)

        logger.info(req)
        logger.info(str(self.case_name))
        logger.info(data)
        # print(res)
        return res


if __name__ == '__main__':
    unittest.main()