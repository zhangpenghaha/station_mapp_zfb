import time
from parameterized import parameterized
from baseView.base_excel import read_excel
from businessView.page_余票查询 import page_余票查询
from businessView.page_选择城市 import Page_选择城市
from businessView.page_首页 import page_首页
from myUnit.st_首页 import st_首页
from common.common import common
from time import sleep
import logging
from businessView.page_选择日期 import page_选择日期
from businessView.page_选择车次 import page_选择车次


class tc_首页(st_首页):
    def setUp(self):
        logging.info("=====前置条件=====")
        dr = common(self.driver)
        dr.act_下滑(3)
        dr = page_首页(self.driver)
        dr.click_余票查询()


    @parameterized.expand(read_excel("test_data.xlsx", "yupiaochaxun"))
    def test_3_手动添加行程_站站查询( self, test_出发地, test_目的地 , test_days, test_toast):
        dr = page_余票查询(self.driver)
        dr.click_出发地()

        dr = Page_选择城市(self.driver)
        dr.select_选择城市(test_出发地)

        dr = page_余票查询(self.driver)
        dr.click_目的地()

        dr = Page_选择城市(self.driver)
        dr.select_选择城市(test_目的地)

        dr = page_余票查询(self.driver)
        dr.click_点击出发日期()

        dr = page_选择日期(self.driver)
        dr.click_选择几天后日期(test_days)

        dr = page_余票查询(self.driver)
        dr.click_余票查询_查询()
        a = dr.get_toast(test_toast)
        self.myEq(test_toast, a, "test余票查询")


    def tearDown(self):
        dr = page_首页(self.driver)
        dr.screenshot_as_png()
        dr.tc_后置回首页()

if __name__ == '__main__':
    import unittest
    unittest.main()