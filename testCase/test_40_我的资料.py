
import logging
from myUnit.st_首页 import st_首页
from businessView.page_我的资料 import page_我的资料

class tc_我的资料(st_首页):

    def setUp(self):
        logging.info("=====我的资料前置条件=====")
        dr=page_我的资料(self.driver)
        dr.click_我的按钮()
        dr.click_个人中心_会员号()


    def test_102_是否有城市选择控件弹出(self):
        logging.info("=====test_102_是否有城市选择控件弹出=====")
        dr = page_我的资料(self.driver)
        dr.click_所在城市()
        a=dr.click_取消()
        self.myEq(1,a,"是否有城市选择控件弹出!")

    def test_103_是否有日期选择控件弹出(self):
        logging.info("=====test_103_是否有日期选择控件弹出=====")
        dr = page_我的资料(self.driver)
        dr.click_出生日期()
        a=dr.click_取消()
        self.myEq(1,a,"是否有日期选择控件弹出")

    def test_104_确认修改出生日期(self):
        logging.info("=====test_104_确认修改出生日期=====")
        dr=page_我的资料(self.driver)
        a=dr.bus_修改日期("确定")
        self.myEq(1,a,"确认修改出生日期")

    def test_105_取消修改出生日期(self):
        logging.info("=====test_105_取消修改出生日期=====")
        dr=page_我的资料(self.driver)
        a=dr.bus_修改日期("取消")
        self.myEq(1,a,"取消修改出生日期")

    def tearDown(self):
        dr=page_我的资料(self.driver)
        dr.screenshot_as_png()
        dr.click_点击首页()
        dr.tc_后置回我的()


if __name__ == '__main__':
    import unittest
    unittest.main()