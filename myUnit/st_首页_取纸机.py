import unittest
from businessView.page_取纸机 import page_取纸机
from appiumDriver.desired_caps import appium_微信车站通
import logging
import warnings

class st_首页_取纸机(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        warnings.simplefilter("ignore", ResourceWarning)
        self.driver = appium_微信车站通()
        self.dr = page_取纸机(self.driver)
        self.dr.act_上滑(2)
        self.dr.click_取纸机()
        self.dr.wait_取纸机()

    @classmethod
    def tearDownClass(self):
        self.dr.sys_关闭app()