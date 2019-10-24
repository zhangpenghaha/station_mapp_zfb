from baseView.base_excel import read_excel
from businessView.page_始发站选择 import page_选择车次出发和到达
from businessView.page_选择城市 import Page_选择城市
from businessView.page_选择日期 import page_选择日期
from businessView.page_选择车次 import page_选择车次
from myUnit.st_首页 import st_首页
from businessView.page_行程 import page_行程
from businessView.page_添加行程 import page_添加行程
from parameterized import parameterized


class tc_行程(st_首页):
    def setUp(self):
        dr = page_行程(self.driver)
        dr.click_点击行程()


    @parameterized.expand(read_excel("test_data.xlsx", "kuatian"))
    def test_3_手动添加行程_站站查询_跨天行程检查( self, test_出发地, test_目的地 , test_toast):
        """站站查询"""
        dr = page_行程(self.driver)
        dr.click_点击行程()
        dr.click_行程_添加行程()
        dr.click_行程_手动添加()
        dr = page_添加行程(self.driver)
        dr.click_添加行程_查询方式("站站添加")
        dr.click_点击出发地()
        dr = Page_选择城市(self.driver)
        dr.select_选择城市(test_出发地)
        dr.click_点击目的地()
        dr.select_选择城市(test_目的地)
        dr.click_添加行程_查询()
        dr.click_loc_with_scroll(test_toast)
        a = dr.get_toast(test_toast)
        self.myEq(test_toast, a, "test站站查询查看跨天行程")



    def tearDown(self):
        dr = page_行程(self.driver)
        dr.screenshot_as_png()
        dr.tc_后置回行程()

    @classmethod
    def tearDownClass(cls):
        dr = page_行程(cls.driver)
        dr.tc_后置回首页()


if __name__ == '__main__':
    import unittest
    unittest.main()