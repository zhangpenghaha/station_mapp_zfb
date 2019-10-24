from businessView.page_添加行程 import page_添加行程
from businessView.page_首页 import page_首页
from function.function import *
from myUnit.st_首页 import st_首页
from businessView.page_车次详情 import page_车次详情
from businessView.page_切换站点 import page_切换站点 
from businessView.page_行程 import page_行程

class tc_车次详情(st_首页):

    def setUp(self):
        dr = page_行程(self.driver)
        dr.click_首页()
        dr = page_车次详情(self.driver)
        if dr.get_toast("浠水站")!= "浠水站":
            dr.click_首页_切换站点按钮()
            dr = page_切换站点(self.driver)
            dr.bus_切换站点_切换到指定站点("浠水")

    def test_500_首页车次号搜索绑定行程(self):
        dr = page_车次详情(self.driver)
        dr.act_下滑(3)
        dr.click_首页_车次查询()
        dr.act_滑动_AtoB(dr.btn_首页_车次查询, dr.btn_车站大屏, "车次查询", "车站大屏")
        sid= dr.bus_首页_车次号搜索("G836")
        dr.click_后一天()
        dr.bus_选择始终站(sid)
        dr.click_车次途经站点_确认添加()
        a = dr.get_toast("行李托运")
        self.myEq(a,"行李托运","test_500_首页车次号搜索绑定行程")
    #

    def test_501_行程车次号搜索绑定行程(self):
        dr = page_行程(self.driver)
        dr.click_点击行程()
        dr.click_行程_添加行程()
        dr.click_行程_手动添加()
        dr = page_添加行程(self.driver)
        dr.click_添加行程_查询方式("车次添加")
        dr.send_输入车次("G835")
        dr.click_添加行程_查询()
        dr = page_车次详情(self.driver)
        dr.bus_选择始终站("G835", 点击确认添加=True)
        dr.click_车次途经站点_确认添加()
        a = dr.get_toast("行李托运")
        self.myEq(a, "行李托运", "test_501_行程车次号搜索绑定行程")

    def test_502_首页删除行程(self):
        dr = page_行程(self.driver)
        dr.click_行程()
        dr.bus_行程_删除全部(3)  # 输入删除个数
        a = dr.click_行程_删除()
        self.myEq(a, None, "test_502_首页删除行程")
        # self.myEq(str(a),"1","test_502_首页删除行程")

    def tearDown(self):
        dr=page_车次详情(self.driver)
        dr.screenshot_as_png()
        dr.tc_后置回首页()

if __name__ == '__main__':
    import unittest
    unittest.main()