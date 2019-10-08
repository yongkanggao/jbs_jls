import requests
import json
from common.Log import logger

logger = logger
class RunMain():

    def send_post(self, url, data):# 定义一个方法，传入需要的参数url和data
        # 参数必须按照url、data顺序传入
        headers = {'Content-Type':'application/json'}
        result = requests.post(url=url, headers=headers,data=data)# 因为这里要封装post方法，所以这里的url和data值不能写死
        # data = json.loads(result.text)
        # res = json.dumps(data, ensure_ascii=False, sort_keys=True, indent=1)
        return result

    def send_get(self, url, data):
        result = requests.get(url=url, params=data)
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