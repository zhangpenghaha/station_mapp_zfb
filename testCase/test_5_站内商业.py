from businessView.page_站内商业 import page_站内商业
from common.loc import *
from function.tools import *
from businessView.page_切换站点 import page_切换站点
from businessView.page_店铺详情 import page_店铺详情
from myUnit.st_首页 import st_首页
import logging
from time import sleep
from function.function import *


class tc_站内商业(st_首页):


    @classmethod
    def setUpClass( cls ):
        dr = page_站内商业(cls.driver)
        dr.click_首页()

        dr = page_切换站点(cls.driver)
        a = dr.get_toast("浠水站")
        if a != "浠水站":
            dr.click_首页_切换站点按钮()
            dr.bus_切换站点_切换到指定站点("浠水")
        dr.act_上滑(3)

    def setUp( self ):
        dr = page_站内商业(self.driver)
        dr.click_首页_车站商业查看全部()

    def test_301_所有楼层展开(self):
        logging.info("====test_301_所有楼层展开=====")
        dr = page_站内商业(self.driver)
        a1 = dr.click_站内商业_所有楼层()
        a2 = dr.get_toast("F1")
        a3 = dr.get_toast("B1")
        self.myEq(str(a1) + a2 + a3, "TrueF1B1", "test_301_所有楼层展开")

    def test_303_全部分类展开(self):
        logging.info("=====test_303_全部分类展开=====")
        dr = page_站内商业(self.driver)
        a1 = dr.click_站内商业_全部分类()
        a2 = dr.get_站内商业_筛选展开4()
        a3 = dr.get_站内商业_筛选展开5()
        self.myEq(str(a1) + a2 + a3, "True美食娱乐休闲", "test_303_全部分类展开")

    def test_305_全部分类展开(self):
        logging.info("=====test_305_全部分类展开=====")
        dr = page_站内商业(self.driver)
        a1 = dr.click_站内商业_智能排序()
        a2 = dr.get_toast("人均最低")
        a3 = dr.get_toast("评分最高")
        self.myEq(str(a1) + a2 + a3, "True人均最低评分最高", "test_305_全部分类展开")

    def etest_307_进站前后展开(self):
        logging.info("=====test_307_进站前后展开=====")
        dr = page_站内商业(self.driver)
        a1 = dr.click_站内商业_进站前后()
        a2 = dr.get_toast("进站前")
        a3 = dr.get_toast("进站后")
        self.myEq(str(a1) + str(a2) + str(a3), "True进站前进站后", "test_307_进站前后展开")

    def test_309_跳转店铺详情(self):
        logging.info("=====test_309_跳转店铺详情=====")
        dr = page_站内商业(self.driver)
        a1 = dr.click_站内商业_店铺列表_便民超市()
        dr = page_店铺详情(self.driver)
        a2 = dr.get_店铺详情_评论此商家()
        self.myEq(str(a1) + a2, "True评论此商家", "test_309_跳转店铺详情")

    def test_310_单条件筛选_所有楼层_一层(self):
        logging.info("=====test_310_单条件筛选_所有楼层_F1=====")
        dr = page_站内商业(self.driver)
        dr.click_站内商业_所有楼层()
        dr.click_站内商业_筛选展开2()
        a1 = dr.get_站内商业_店铺列表_便民超市()
        a2 = dr.get_站内商业_店铺列表_平价自选商店()
        self.myEq(str(a1) + str(a2), "便民超市平价自选商店", "test_310_单条件筛选_所有楼层_F1")

    def test_311_单条件筛选_所有楼层_负一层_无结果(self):
        logging.info("=====test_311_单条件筛选_所有楼层_负一层_无结果=====")
        dr = page_站内商业(self.driver)
        dr.click_站内商业_所有楼层()
        dr.click_站内商业_筛选展开3()
        a = dr.get_站内商业_无搜索结果提示()
        self.myEq(str(a), "暂无相关商家", "test_311_单条件筛选_所有楼层_负一层_无结果")

    def test_312_单条件筛选_所有分类_美食_无结果(self):
        logging.info("=====test_312_单条件筛选_所有分类_美食_无结果=====")
        dr = page_站内商业(self.driver)
        dr.click_站内商业_全部分类()
        dr.click_站内商业_展开筛选_美食()
        a = dr.get_站内商业_无搜索结果提示()
        self.myEq(str(a), "暂无相关商家", "test_312_单条件筛选_所有分类_美食_无结果")

    def test_313_单条件筛选_所有分类_超市(self):
        logging.info("=====test_313_单条件筛选_所有分类_超市=====")
        dr = page_站内商业(self.driver)
        dr.click_站内商业_全部分类()
        # dr.act_滑动_AtoB(dr.btn_站内商业_筛选展开_美食, dr.btn_站内商业_全部分类, "美食", "全部分类")
        dr.click_站内商业_展开筛选_百货超市()
        a1 = dr.get_站内商业_店铺列表_便民超市()
        a2 = dr.get_站内商业_店铺列表_平价自选商店()
        self.myEq(str(a1) + str(a2), "便民超市平价自选商店", "test_313_单条件筛选_所有分类_超市")

    def etest_314_单条件筛选_进站前后_进站前(self):
        logging.info("=====test_314_单条件筛选_进站前后_进站前=====")
        dr = page_站内商业(self.driver)
        dr.click_站内商业_进站前后()
        dr.click_站内商业_筛选展开2()
        sleep(2)
        a1 = dr.get_站内商业_店铺列表_便民超市()
        a2 = dr.get_站内商业_店铺列表_平价自选商店()
        self.myEq(str(a1) + str(a2), "便民超市0", "test_314_单条件筛选_进站前后_进站前")

    def etest_315_单条件筛选_进站前后_进站后(self):
        logging.info("=====test_315_单条件筛选_进站前后_进站后=====")
        dr = page_站内商业(self.driver)
        dr.click_站内商业_进站前后()
        dr.click_站内商业_筛选展开3()
        sleep(3)
        a2 = dr.get_站内商业_店铺列表_平价自选商店()
        a1 = dr.get_站内商业_店铺列表_便民超市()
        self.myEq(str(a1) + str(a2), "0平价自选商店", "test_315_单条件筛选_进站前后_进站后")

    def test_399_标记归零(self):
        update_flag(0)

    def tearDown(self):
        dr = page_站内商业(self.driver)
        dr.screenshot_as_png()
        dr.tc_后置回首页()


if __name__ == '__main__':
    import unittest

    unittest.main()
