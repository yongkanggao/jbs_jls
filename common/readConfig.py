import os
import configparser
from common import getpathInfo

path = getpathInfo.get_Path()#调用实例化，
config_path = os.path.join(path, 'config/config.ini')#这句话是在path路径下再加一级
config = configparser.ConfigParser()#调用外部的读取配置文件的方法
config.read(config_path, encoding='utf-8')

class ReadConfig():

    def get_http(self, name):
        value = config.get('HTTP', name)
        return value
    def get_email(self, name):
        value = config.get('EMAIL', name)
        return value
    def get_mysql(self, name):
        value = config.get('DATABASE', name)
        return value
    def get_header(self,name):
        value = config.get('HEADER',name)
        return value


if __name__ == '__main__':#测试一下，我们读取配置文件的方法是否可用
    print('HTTP中的baseurl值为：', ReadConfig().get_http('baseurl'))
    print('EMAIL中的开关on_off值为：', ReadConfig().get_email('on_off'))


