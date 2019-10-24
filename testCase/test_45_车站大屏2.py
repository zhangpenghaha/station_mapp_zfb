import time

from businessView.page_切换站点 import page_切换站点
from businessView.page_首页 import page_首页
from myUnit.st_首页 import st_首页
from businessView.page_车站大屏 import page_车站大屏
import unittest
from function.function import get_flag,update_flag
class tc_车站大屏详情(st_首页):
    def setUp(self):
        dr =page_首页(self.driver)
        dr.click_首页()
        dr.act_下滑()
        time.sleep(3)
        if dr.get_toast("浠水站")!="浠水站":
            dr.click_首页_切换站点按钮()
            dr = page_切换站点(self.driver)
            dr.bus_切换站点_切换到指定站点("浠水")
        if get_flag()==0:
            dr.click_车站大屏()
        # dr.act_下滑(3)
        # dr.act_滑动_byYourSelf(dr.txt_首页_时刻查询模块名, 0.5, 0.15, "txt_首页_时刻查询模块名移动到0.15位置")
        # dr.act_滑动_byYourSelf(dr.btn_首页车站大屏_候车按钮, 0.5, 0.3, "btn_首页车站大屏_候车按钮移动到0.3位置")
        # dr.click_查看全部车次()

    def test_001_车站大屏候车字段检查(self):
        dr=page_车站大屏(self.driver)
        a=dr.bus_车站大屏_候车信息检查("候车")
        self.myEq(a,["车次","终到站","发车","检票口","状态"],"test_001_车站大屏候车字段检查")

    def test_002_车站大屏到达字段检查(self):
        dr=page_车站大屏(self.driver)
        a=dr.bus_车站大屏_候车信息检查("到达")
        self.myEq(a,["车次","始发站","到本站","出站口","状态"],"test_001_车站大屏候车字段检查")


    def test_003_点击车次查看详情文案(self):
        dr = page_车站大屏(self.driver)
        a = dr.get_点击车次查看详情文案()
        self.myEq("点击车次 查看详情", a, "判断文案是否存在")

    def test_004_车站大屏_输入框文案(self):
        dr = page_车站大屏(self.driver)
        a = dr.get_输入框文案()
        self.myEq("请输入要查询的车次号", a, "判断文案是否存在")

    #
    # def test_005_勾选高铁动车(self):
    #     dr=page_车站大屏(self.driver)
    #     a=dr.click_勾选高铁动车()
    #     self.myEq("暂无相关数据",a,"检查勾选结果")
    #
    def test_006_检查以上信息仅供参考文案(self):
        dr = page_车站大屏(self.driver)
        a = dr.get_以上信息仅供参考文案()
        self.myEq("以上信息仅供参考，实际情况以车站公告为准", a, "检查以上信息仅供参考文案")

    def test_007_点击搜索输入框(self):
        dr = page_车站大屏(self.driver)
        a = dr.get_键盘元素()
        self.myEq('C', a, "检查键盘是否弹出")

    def test_008_搜索存在的车次(self):
        dr = page_车站大屏(self.driver)
        a = dr.input_输入车次号("K446","-我也是有底线的-")
        self.myEq('-我也是有底线的-', a, "检查搜索结果")

    def test_009_搜索不存在的车次(self):
        dr = page_车站大屏(self.driver)
        a = dr.input_输入车次号("GY", "暂无相关数据")
        self.myEq('暂无相关数据', a, "检查搜索结果")

    def test_010_模糊查询车次(self):
        dr = page_车站大屏(self.driver)
        a = dr.input_输入车次号("446", "西安")
        self.myEq('西安', a, "检查搜索结果")

    def test_011_精准查询车次(self):
        dr = page_车站大屏(self.driver)
        a = dr.input_输入车次号("K823", "深圳东")
        self.myEq('深圳东', a, "检查搜索结果")

    def test_012_勾选高铁动车(self):
        dr=page_车站大屏(self.driver)
        a=dr.click_勾选高铁动车()
        self.myEq("暂无相关数据",a,"检查勾选结果")

    def test_013_清空搜索框(self):
        dr = page_车站大屏(self.driver)
        a=dr.click_清空("GY362")
        self.myEq(0,a,"检查清空按钮")

    def test_014_车站大屏_点击车次进入结果页(self):
        dr = page_车站大屏(self.driver)
        a=dr.click_车次号("K823")
        self.myEq("请选择出发站和到达站",a,"检查点击车次进入结果页")

    def test_015_检查勾选起始站(self):
        dr = page_车站大屏(self.driver)
        a = dr.check_起始站("K823")
        self.myEq("浠水", a, "检查默认选择起始站")

    def test_016_检查到达站文案(self):
        dr = page_车站大屏(self.driver)
        a = dr.check_结果页文案("K823","到达站")
        self.myEq("到达站", a, "检查到达站文案站")

    def test_017_检查结果页底部文案(self):
        dr = page_车站大屏(self.driver)
        a = dr.check_结果页文案("K823", "添加行程，列车动态实时提醒")
        self.myEq("添加行程，列车动态实时提醒", a, "检查结果页底部文案")

    def test_018_检查加一天标识(self):
        dr = page_车站大屏(self.driver)
        a = dr.check_结果页文案("K823", "+1天")
        self.myEq("+1天", a, "检查跨天标识")

    def test_019_检查车次变更标识(self):
        dr = page_车站大屏(self.driver)
        a = dr.check_结果页文案("K823", "车次变更：K823")
        self.myEq("车次变更：K823", a, "检查车次变更标识")

    def test_019_检查车次变更标识_01( self ):
        dr = page_车站大屏(self.driver)
        a = dr.check_结果页文案("K823", "车次号：K822")
        self.myEq("车次号：K822", a, "检查车次变更标识")

    def test_020_检查车次变更标识_02( self ):
        dr = page_车站大屏(self.driver)
        a = dr.check_结果页文案("K823", "车次变更：K823")
        self.myEq("车次变更：K823", a, "检查车次变更标识")


    def tearDown(self):
        dr=page_车站大屏(self.driver)
        dr.screenshot_as_png()
        dr.tc_后置回首页()



if __name__ == '__main__':

    unittest.main()
