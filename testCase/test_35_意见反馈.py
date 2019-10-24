import pytest
from baseView.base_excel import read_excel
from myUnit.st_首页 import st_首页
from businessView.page_意见反馈 import page_意见反馈
import logging
from parameterized import parameterized



class tc_意见反馈(st_首页):

    def setUp(self):
        dr = page_意见反馈(self.driver)
        dr.click_我的按钮()
        dr.click_个人中心_意见反馈()

    @parameterized.expand(read_excel("test_data.xlsx", "login"))
    def test_意见反馈(self, logging_info, test_意见类型, test_详细描述, test_联系方式, test_toast, test_描述):
        logging.info(logging_info)
        dr = page_意见反馈(self.driver)
        dr.bus_提交意见反馈(意见类型=test_意见类型, 详细描述=test_详细描述, 联系方式=test_联系方式)
        a = dr.get_toast(test_toast)
        self.myEq(test_toast, a, test_描述)

    def tearDown(self):
        dr = page_意见反馈(self.driver)
        dr.screenshot_as_png()
        dr.tc_后置回我的()

if __name__ == '__main__':
    import unittest
    unittest.main()

# from myUnit.st_首页 import st_首页
# from businessView.page_意见反馈 import page_意见反馈
# import logging
#
#
# class tc_意见反馈(st_首页):
#
#     def setUp(self):
#         dr = page_意见反馈(self.driver)
#         dr.click_我的按钮()
#         dr.click_个人中心_意见反馈()
#
#     def test_202_详细描述和联系方式都为空给出提示(self):
#         logging.info("=====test_202_详细描述和联系方式都为空给出提示=====")
#         dr = page_意见反馈(self.driver)
#         dr.bus_提交意见反馈()
#         a=dr.get_toast("请输入详细描述")
#         self.myEq("请输入详细描述",a,"test_202_详细描述和联系方式都为空给出提示")
#
#     def test_203_仅详细描述为空给出提示(self):
#         logging.info("=====test_203_仅详细描述为空给出提示=====")
#         dr = page_意见反馈(self.driver)
#         dr.bus_提交意见反馈(联系方式="17702731522")
#         a=dr.get_toast("请输入详细描述")
#         self.myEq("请输入详细描述",a,"test_203_仅详细描述为空给出提示")
#
#     def test_204_联系方式都为空给出提示(self):
#         logging.info("=====test_204_联系方式都为空给出提示=====")
#         dr = page_意见反馈(self.driver)
#         dr.bus_提交意见反馈(详细描述="需要测试环境")
#         a=dr.get_toast("请输入手机号")
#         self.myEq("请输入手机号",a,"test_204_联系方式都为空给出提示")
#
#     def test_205_意见反馈主流程全部填写(self):
#         logging.info("=====test_205_意见反馈主流程全部填写=====")
#         dr = page_意见反馈(self.driver)
#         dr.bus_提交意见反馈(意见类型="服务体验",详细描述="需要测试环境",联系方式="17702731522")
#         a=dr.get_toast("提交成功!")
#         self.myEq("提交成功!",a,"test_205_意见反馈主流程全部填写")
#
#     def tearDown(self):
#         dr = page_意见反馈(self.driver)
#         dr.tc_后置回我的()
#
# if __name__ == '__main__':
#     import unittest
#     unittest.main()