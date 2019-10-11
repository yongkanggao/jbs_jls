# jbs_jls
#目录结构   
##common：存放公共文件   
  ###config.ini：数据库、邮箱、接口等的配置项，用于方便的调用读取   
  configEmail.py：配置发送邮件的主题、正文等，将测试报告发送并抄送到相关人邮箱的逻辑   
  configHttp.py：通过get、post、put、delete等方法来进行http请求，并拿到请求响应   
  getmySql.py：读取数据库，获取数据库数据   
  getpathInfo.py:获取项目路径   
  geturlParams.py:获取接口的URL、参数、method   
  Log.py：打印生成日志   
  readConfig.py：读取配置文件的方法，并返回文件中内容   
  readExcel.py：读取Excel文件   
  
  
log：   
  logs.txt:存放日志文件   
  
  
main_run:   
  runAll.py:执行接口自动化，项目工程部署完毕后直接运行该文件即可   
  
  
report:   
  report.html:测试报告文件   
  
  
testCase：
  测试用例
  
 
testFile/case:
  case.xlsx:存放测试数据
  
  
 caselist.txt：配置将要执行testCase目录下的哪些用例文件，前加#代表不进行执行，当项目过于庞大，用例足够多的时候，我们可以通过这个开关，来确定本次执行哪些接口的哪些用例。

  
  
