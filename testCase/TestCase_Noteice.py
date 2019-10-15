#coding=utf-8
#author_="bruce.gao"
#date:2019/10/15 17:00

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
Notice_xls = readExcel.readExcel().get_xls('case.xlsx','notice')
cur = getmySql.getmySql().get_MySql()
cu = cur.cursor()

@paramunittest.parametrized(*Notice_xls)
class testNotice(unittest.TestCase):
    """
    消息通知！
    """

    def setParameters(self,case_name,path,query,method,status_code,code,msg,commit,sql,content,content_text):
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
        self.commit = str(commit)
        self.content = str(content)
        self.content_text = str(content_text)

    def setUp(self):
        """

        :return:
        """
        print("\n" + self.case_name + ":\n\n测试开始前准备\n")

    def tearDown(self):
        print("测试结束\n输出log\n完结!\n\n")

    def test_checkResult(self):

        if self.case_name == "消息列表":
            get_url = url + self.path
            req = RunMain().run_main(self.method, get_url,self.query)
            data = json.loads(req.text)
            res = json.dumps(data, ensure_ascii=False, indent=1)
            self.assertEqual(req.status_code, self.status_code)
            self.assertEqual(data['code'], self.code)
            self.assertEqual(data['msg'], self.msg)
            self.assertEqual(eval(self.content),self.content_text)

        elif self.case_name.startswith("消息_"):
            cu.execute(self.sql)
            da = cu.fetchall()
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

        else:
            get_url = url + self.path
            req = RunMain().run_main(self.method, get_url, self.query.encode('utf-8'))
            data = json.loads(req.text)
            res = json.dumps(data, ensure_ascii=False, indent=1)
            self.assertEqual(req.status_code, self.status_code)
            self.assertEqual(data['code'], self.code)
            self.assertEqual(data['msg'], self.msg)
            time.sleep(1)

        logger.info(req)
        logger.info(str(self.case_name))
        logger.info(data)
        # print(res)
        return res


if __name__ == '__main__':
    unittest.main()