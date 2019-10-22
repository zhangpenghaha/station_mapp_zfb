from myUnit.st_首页 import st_首页
from businessView.page_选择日期 import page_选择日期




class tc_选择日期(st_首页):

    def setUp(self):
        dr=page_选择日期(self.driver)
        dr.click_某月某日()


    def test_001_时刻查询模块正确展示选择60天以后的日期(self):

        dr=page_选择日期(self.driver)
        dr.click_当前日期加60天()
        e="".join(tuple(dr.check_选择日期()))
        a=dr.get_选择后的出发某月某日()+dr.get_选择后的出发星期()
        self.myEq(a,e,"时刻查询模块正确展示选择60天以后的日期")


    def tearDown(self):
        dr=page_选择日期(self.driver)
        dr.tc_后置回首页()


if __name__ == '__main__':
    import unittest
    unittest.main()


