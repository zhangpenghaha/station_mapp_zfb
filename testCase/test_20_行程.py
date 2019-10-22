from myUnit.st_首页 import st_首页
from businessView.page_行程 import page_行程
from businessView.page_添加行程 import page_添加行程

class tc_行程(st_首页):
    def setUp(self):
        dr = page_行程(self.driver)
        dr.click_行程()

    def test_1_添加行程弹出选择框(self):
        dr = page_行程(self.driver)
        dr.click_行程_添加行程()
        a=dr.get_行程_手动添加()
        self.myEq(a,"手动添加","test_1_添加行程弹出选择框")
        dr.click_取消()

    def test_2_手动添加行程跳转到关注行程页(self):
        dr = page_行程(self.driver)
        dr.click_行程_添加行程()
        dr.click_行程_手动添加()
        dr = page_添加行程(self.driver)
        a=dr.get_toast("扫火车票")
        self.myEq(a,"扫火车票","test_2_手动添加行程跳转到关注行程页")




    def tearDown(self):
        dr = page_行程(self.driver)
        dr.tc_后置回首页()

if __name__ == '__main__':
    import unittest
    unittest.main()