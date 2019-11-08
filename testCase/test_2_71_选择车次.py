from businessView.page_首页 import page_首页
from function.function import *
from myUnit.st_首页 import st_首页
from businessView.page_选择车次 import page_选择车次
from businessView.page_切换站点 import page_切换站点
from businessView.page_行程 import page_行程
import warnings
warnings.simplefilter("ignore", ResourceWarning)

import unittest

class tc_车次详情(st_首页):

    @classmethod
    def setUpClass(cls):
        dr = page_首页(cls.driver)
        # dr.click_首页()
        # dr = page_选择车次(self.driver)
        if dr.get_toast("浠水站")!= "浠水站":
            dr.click_首页_切换站点按钮()
            dr = page_切换站点(cls.driver)
            dr.bus_切换站点_切换到指定站点("浠水")
        dr.act_下滑(3)
        dr.act_滑动_byYourSelf(dr.txt_首页_时刻查询模块名, 0.5, 0.15, "txt_首页_时刻查询模块名移动到0.15位置")
        dr.click_首页_站站查询()
        dr.click_首页_时刻查询_查询()

    # def test_711_检查出发站与终点站(self):
    #     dr = page_选择车次(self.driver)
    #     a=dr.check_文案检查("武汉-北京")
    #     self.myEq("武汉-北京",a,"检查出发站与终点站")

    def test_712_勾选高铁(self):
        dr = page_选择车次(self.driver)
        a=dr.click_勾选高铁动车("K968")
        self.myEq(0,a,"检查车次数量")

    # def test_713_点击车次(self):
    #     dr = page_选择车次(self.driver)
    #     a=dr.click_点击车次("K600")
    #     self.myEq("到达正点率",a,"检查是否进入结果页")

    # def test_714_前序站(self):
    #     dr = page_选择车次(self.driver)
    #     dr.click_点击车次("K600","到达正点率")
    #     a=dr.get_前序站()
    #     self.myEq("7个前序站",a,"检查前序站点")
    #
    # def test_715_后序站(self):
    #     dr = page_选择车次(self.driver)
    #     dr.click_点击车次("K600","到达正点率")
    #     a=dr.get_后序站()
    #     self.myEq("7个后序站",a,"检查后序站点")
    def test_716_文案检查(self):
        dr = page_选择车次(self.driver)
        dr.click_点击车次("小时")
        a = dr.check_选择车次结果页文案()
        self.myEq(["到达正点率","站名","到站","停留","出发","状态","到站","添加行程，列车动态实时提醒"], a, "文案检查")

    def test_717_点击展开(self):
        dr = page_选择车次(self.driver)
        dr.click_点击车次("小时")
        a=dr.click_展开()
        self.myEq("收起",a,"点击展开按钮")

    def test_718_点击确定添加(self):
        dr = page_选择车次(self.driver)
        dr.click_点击车次("小时")
        a=dr.click_确定添加()
        self.myEq("行李托运",a,"点击确定添加")

    # @classmethod
    # def tearDownClass(cls):
    #     dr = page_行程(cls.driver)
    #     dr.tc_后置回行程()
    #     dr.bus_行程_删除首个行程()

    @classmethod
    def tearDownClass(cls):

        dr = page_行程(cls.driver)
        dr.screenshot_as_png()
        dr.tc_后置回行程()
        dr.bus_行程_删除首个行程()
        dr.tc_后置回首页()




if __name__ == '__main__':
    unittest.main()



    # def test_711_