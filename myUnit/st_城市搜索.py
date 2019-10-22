from functiontool.myassert import myassert
from appiumDriver.desired_caps import appium_微信车站通
from businessView.page_站点搜索 import page_城市搜索
import logging
import warnings

class st_城市搜索(myassert):

    @classmethod
    def setUpClass(self):
        warnings.simplefilter("ignore", ResourceWarning)
        logging.info("测试城市搜索页面前置条件,进入首页,点击余票查询!")
        self.driver = appium_微信车站通()
        self.dr = page_城市搜索(self.driver)
        self.dr.click_余票查询()
        self.dr.click_出发地()

    @classmethod
    def tearDownClass(self):
        self.dr.sys_关闭app()