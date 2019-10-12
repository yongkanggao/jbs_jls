import requests
import json
from common.Log import logger

logger = logger
webtoken = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqVXNlciI6eyJuaWNrIjoi546L5p6rIiwib3BlbmlkIjpudWxsLCJ1bmlvbmlkIjoidVJOYkc3ZVhDUmVVVVlZMjN4MHlxUWlFaUUiLCJ1c2VyaWQiOiIxNTUxMDU0ODU4MDgwMTY2NSIsInVzZXJJbWciOiJodHRwczovL3N0YXRpYy1sZWdhY3kuZGluZ3RhbGsuY29tL21lZGlhL2xBRFBEZ1E5cWdwU3FmYk5DUkROQ1F3XzIzMTZfMjMyMC5qcGciLCJ3ZWJUb2tlbiI6bnVsbCwidXNlcmluZm8iOm51bGwsInVzZXJNZW51IjpudWxsfSwiaXNzIjoiZHdhcGl1c2VyIiwiZXhwIjoxNTcwODgwODczLCJuYmYiOjE1NzA3OTQ0NzN9.jB2loxIht4rzs-7x_RsUAKXfT9EpoN6Abgy_R433tV8'
class RunMain():

    def send_post(self, url, data):# 定义一个方法，传入需要的参数url和data
        # 参数必须按照url、data顺序传入
        headers = {'Content-Type':'application/json','webtoken': webtoken}
        result = requests.post(url=url, headers=headers,data=data)# 因为这里要封装post方法，所以这里的url和data值不能写死
        # data = json.loads(result.text)
        # res = json.dumps(data, ensure_ascii=False, sort_keys=True, indent=1)
        return result

    def send_get(self, url, data):
        headers = {'webtoken': webtoken}
        result = requests.get(url=url,headers=headers,params=data)
        # data = json.loads(result.text)
        # res = json.dumps(data, ensure_ascii=False, sort_keys=True, indent=1)
        return result

    def run_main(self, method, url=None, data=None):#定义一个run_main函数，通过传过来的method来进行不同的get或post请求
        result = None
        if method == 'post':
            result = self.send_post(url, data)
            # logger.info(str(result))
        elif method == 'get':
            result = self.send_get(url, data)
            #data = json.loads(result.text)
            # logger.info(str(result))
        else:
            print("method值错误！！！")
            logger.info("method值错误！！！")
        return result
if __name__ == '__main__':#通过写死参数，来验证我们写的请求是否正确
    result = RunMain().run_main('get', 'http://192.168.1.198:10007/task/tasks', 'login_user=1342&page_num=1&page_size=10&status=0')
    print(result)