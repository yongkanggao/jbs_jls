# jbs_jls
目录结构   
common：存放公共文件
  config.ini：数据库、邮箱、接口等的配置项，用于方便的调用读取
  configEmail.py：配置发送邮件的主题、正文等，将测试报告发送并抄送到相关人邮箱的逻辑
  configHttp.py：通过get、post、put、delete等方法来进行http请求，并拿到请求响应
  getmySql.py：读取数据库，获取数据库数据
  getpathInfo.py:获取项目路径
  geturlParams.py:获取接口的URL、参数、method
  
