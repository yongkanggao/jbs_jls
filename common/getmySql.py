#coding=utf-8
#author_="bruce.gao"
#date:2019/10/8 17:02

import pymysql
from common import readConfig

read_conf = readConfig.ReadConfig()
host = read_conf.get_mysql('host')
port = read_conf.get_mysql('port')
user = read_conf.get_mysql('user')
password = read_conf.get_mysql('passwd')
database = read_conf.get_mysql('database')

class getmySql():
    def get_MySql(self):
        conn = pymysql.connect(
            host=host,
            port=int(port),
            user=user,
            password=password,
            database=database,
            charset='utf8')

        # cur = conn.cursor()
        # cur.execute("select uuid from task where title = '家里事任务流程_保存任务';")
        # data = cur.fetchall()

        return conn

        # cur.close()
        # conn.close()

if __name__ =='__main__':
    print(getmySql().get_MySql())