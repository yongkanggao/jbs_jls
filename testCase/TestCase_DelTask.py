#coding=utf-8
#author_="bruce.gao"
#date:2019/10/8 17:20

import unittest
import json
from common import geturlParams
from common.configHttp import RunMain
from common import getmySql
from common.Log import logger

logger = logger
url = geturlParams.geturlParams().get_Url()
cur = getmySql.getmySql().get_MySql()
cu = cur.cursor()

class testDelTask(unittest.TestCase):
    def test_del_saved(self):
        "删除保存的任务"
        cu.execute("select uuid from task where title = '家里事任务流程_保存任务';")
        data = cu.fetchall()
        # print(len(data[0][0]))
        if len(data[0][0]) != 0:
            dat = data[0][0]
        else:
            print("没有查到数据")
        cu.close()

        get_url = url + "/tasks/" + dat + "/delete"
        # print(get_url)
        data1 = {"user_id":"130751354"}
        req = RunMain().run_main('post',get_url,data1)
        da = json.loads(req.text)
        res = json.dumps(da,ensure_ascii=False,indent=1)
        self.assertEqual(req.status_code,200)
        self.assertEqual(da['code'],'Joybos.2112')
        self.assertEqual(da['msg'],'success')

        logger.info(req)
        logger.info(da)
        # print(res)
        return res

if __name__ == '__main__':
    unittest.main()