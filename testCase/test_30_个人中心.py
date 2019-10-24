from myUnit.st_首页 import st_首页
from businessView.page_个人中心 import page_个人中心
from businessView.page_我的资料 import page_我的资料
from businessView.page_我的积分 import page_我的积分
from businessView.page_登录12306 import page_登录12306
import logging

class tc_个人中心(st_首页):
    def setUp(self):
        logging.info("=====个人中心前置条件=====")
        dr = page_个人中心(self.driver)
        dr.click_我的按钮()


    def test_202_个人中心跳转(self):
        logging.info("=====test_2_个人中心跳转=====")
        dr = page_个人中心(self.driver)
        a = dr.get_toast("个人中心")
        self.myEq("个人中心", a, "test_2_我的资料跳转")


    def test_203_我的资料跳转(self):
        logging.info("=====test_3_我的资料跳转=====")
        dr = page_我的资料(self.driver)
        dr.click_个人中心_会员号()
        a = dr.get_toast("我的资料")
        self.myEq("我的资料", a, "test_3_我的资料跳转")


    def test_204_点击积分商城给提示(self):
        logging.info("=====test_4_点击积分商城给提示=====")
        dr = page_我的积分(self.driver)
        dr.click_个人中心_积分商城()
        a1 = dr.get_个人中心_完善中_提示()
        a2 = dr.click_确认()
        self.myEq(a1 + str(a2), "功能正在拼命完善中，敬请期待！True", "我的积分页面跳转")

    def test_205_点击优惠券给提示(self):
        logging.info("=====test_5_点击优惠券给提示=====")
        dr = page_我的积分(self.driver)
        dr.click_个人中心_优惠券()
        a1 = dr.get_toast("可使用")
        self.myEq(a1, "可使用", "我的积分页面跳转")

    def test_206_我的12306跳转(self):
        logging.info("=====test_6_我的12306跳转=====")
        dr = page_登录12306(self.driver)
        dr.click_个人中心_我的12306()
        a = dr.get_toast("登录12306")
        self.myEq("登录12306", a, "test_6_我的12306跳转")

    def test_207_我的行程跳转(self):
        logging.info("=====test_6_我的12306跳转=====")
        dr=page_个人中心(self.driver)
        dr.click_个人中心_我的行程()
        a=dr.get_toast("智能行程")
        self.myEq(a,"智能行程","test_7_我的行程跳转")

    def test_208_意见反馈跳转(self):
        logging.info("=====test_8_意见反馈跳转=====")
        dr=page_个人中心(self.driver)
        dr.click_个人中心_意见反馈()
        a=dr.get_toast("优化建议")
        self.myEq(a,"优化建议","test_8_意见反馈跳转")


    def tearDown(self):
        dr = page_个人中心(self.driver)
        dr.screenshot_as_png()
        dr.tc_后置回我的()


if __name__ == '__main__':
    import unittest

    unittest.main()
