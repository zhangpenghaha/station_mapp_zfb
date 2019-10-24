import time

from businessView.page_始发站选择 import page_选择车次出发和到达
from businessView.page_车次详情 import page_车次详情
from businessView.page_选择城市 import Page_选择城市
from businessView.page_选择日期 import page_选择日期
from businessView.page_选择车次 import page_选择车次

from businessView.page_首页 import page_首页
from myUnit.st_首页 import st_首页
from businessView.page_行程 import page_行程
from businessView.page_添加行程 import page_添加行程


class tc_行程详情与分享(st_首页):
    # @classmethod
    # def setUpClass(cls):
    #     dr = page_行程(cls.driver)
    #     dr.click_点击行程()
    #     dr.bus_行程_删除全部(2)
    #     dr.click_行程_添加行程()
    #     dr.click_行程_手动添加()
    #     dr = page_添加行程(cls.driver)
    #     dr.click_添加行程_查询方式("站站添加")
    #     dr.click_点击出发地()
    #     dr = Page_选择城市(cls.driver)
    #     dr.select_选择城市("乌鲁木齐")
    #     dr.click_点击目的地()
    #     dr.select_选择城市("哈尔滨")
    #     dr = page_添加行程(cls.driver)
    #     dr.click_添加行程_查询()
    #     dr = page_选择车次(cls.driver)
    #     dr.click_点击车次("小时")
    #     dr.click_确认添加()

    def setUp(self):
        dr = page_首页(self.driver)
        dr.click_点击文本("乌鲁木齐")

    def test_01_行程详情页分享( self ):
        dr = page_车次详情(self.driver)
        dr.click_车次详情_分享按钮()
        a = dr.get_toast("推荐给朋友")
        dr.click_关闭()
        self.myEq(a, "推荐给朋友", "行程详情页行程分享按钮")

    def test_02_跨天检查(self):
        dr =  page_车次详情(self.driver)
        a = dr.get_toast("+3天")
        self.myEq(a, "+3天", "行程详情页行程分享按钮")

    def test_03_正点率(self):
        dr =  page_车次详情(self.driver)
        dr.click_点击文本("出发正点率")
        a = dr.get_toast("历史晚点概况")
        self.myEq(a, "历史晚点概况", "正点率页面")

    # def test_04_候车指数(self):
    #     dr = page_车次详情(self.driver)
    #     dr.act_上滑()
    #     a = dr.check_候车指数()
    #     self.myEq(a, ["车站客流负荷","排队进站耗时","今日发送旅客", "今日发送车次","今日晚点车次","今日增开车次"], "候车指数字段检查")

    def test_05_列车信息(self):
        dr = page_车次详情(self.driver)
        dr.act_上滑(2)
        a = dr.check_列车信息()
        self.myEq(a, ["列车型号","定员","编组", "车上WiFi","餐车","最高时速","充电电源"], "列车信息字段检查")

    def test_06_行程天气(self):
        dr = page_车次详情(self.driver)
        dr.act_上滑(4)
        a = dr.check_行程天气()
        self.myEq_in("行程天气", a, "行程详情天气")


    def test_30_首页分享行程(self):
        dr = page_首页(self.driver)
        dr.tc_后置回首页()
        dr.click_分享行程()
        a = dr.get_toast("分享")
        self.myEq(a, "分享", "首页行程分享按钮")
        dr.click_关闭分享()


    def test_40_行程列表页分享(self):
        """手动添加行程_车次查询"""
        dr = page_行程(self.driver)
        dr.tc_后置回行程()
        dr.click_点击分享()
        time.sleep(6)
        a = dr.get_toast("分享 ")
        dr.click_关闭分享行程()
        self.myEq(a, "分享 ", "行程列表页行程分享按钮")

    def tearDown(self):
        dr = page_首页(self.driver)
        dr.screenshot_as_png()
        dr.tc_后置回首页()


    @classmethod
    def tearDownClass(cls):
        dr = page_行程(cls.driver)
        dr.tc_后置回首页()
if __name__ == '__main__':
    import unittest
    unittest.main()