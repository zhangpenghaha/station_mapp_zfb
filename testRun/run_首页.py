from BSTestRunner import BSTestRunner
import unittest
import time
import logging.config
import sys
import os

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
sys.setrecursionlimit(3000)

"引入日志配置文件"
CON_LOG = '../config/log.conf'
logging.config.fileConfig(CON_LOG)
logging = logging.getLogger()

test_dir = '../testCase'
report_dir = '../reports'

discover = unittest.defaultTestLoader.discover(test_dir, pattern='tc.py')

now = time.strftime('%Y-%m-%d %H_%M_%S')
report_name = report_dir+'/'+now+'test_report.html'

with open(report_name,'wb') as f:
    runner = BSTestRunner(stream=f, title="自动化测试报告!", description="微信车站通首页!")
    logging.info("=====开始车站通微信小程序测试=====")
    runner.run(discover)
