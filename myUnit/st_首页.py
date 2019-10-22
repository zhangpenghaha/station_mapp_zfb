from appiumDriver.desired_caps import appium_微信车站通, appium_支付宝车站通
from time import sleep
import logging
from function.myassert import myassert
import sys
from function.function import update_flag
sys.setrecursionlimit(3000)
import warnings



class st_首页(myassert):
    driver = appium_支付宝车站通()


    @classmethod
    def setUpClass(self):
        warnings.simplefilter("ignore", ResourceWarning)
        logging.info("车站通首页测试前置条件,启动支付宝进入车站通首页!")
        update_flag(0)
        sleep(2)

    @classmethod
    def tearDownClass(self):
        update_flag(0)
