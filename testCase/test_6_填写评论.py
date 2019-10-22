from myUnit.st_首页 import st_首页
from businessView.page_填写评论 import page_填写评论
from function.function import get_flag,update_flag
from businessView.page_切换站点 import page_切换站点
import logging


class tc_填写评论(st_首页):
    @classmethod
    def setUpClass( cls ):
        dr = page_填写评论(cls.driver)
        dr.click_首页()
        dr.click_首页_切换站点按钮()
        dr = page_切换站点(cls.driver)
        dr.bus_切换站点_切换到指定站点("浠水")
        dr.act_上滑(3)
    def setUp(self):
        dr=page_填写评论(self.driver)
        dr.click_首页()
        # if dr.get_首页顶部_当前站点()!="浠水站":
        #     dr.click_首页_切换站点按钮()
        #     dr = page_切换站点(self.driver)
        #     dr.bus_切换站点_切换到指定站点("浠水")
        #     dr=page_填写评论(self.driver)
        # if get_flag()==0:
        #     dr.act_上滑(3)
        dr.click_首页_车站商业进站前1号位()
        dr.click_店铺详情_评论此商家()
        # dr.bus_填写评论_流程(勾选匿名=True, 选择星级=5, 评价内容="好评!", 上传图片="1-1")


    def test_001_全部为空提示(self):
        logging.info("=====test_001_全部为空提示=====")
        update_flag(1)
        dr=page_填写评论(self.driver)
        dr.bus_填写评论_流程()
        # a = dr.get_toast_byid()
        a = dr.get_toast("匿名评论")
        logging.info("toast提示为:"+"描述不能为空")
        self.myEq("匿名评论",a,"test_001_全部为空提示")

    def test_002_评分为空提示(self):
        logging.info("=====test_002_评分为空提示=====")
        dr=page_填写评论(self.driver)
        dr.bus_填写评论_流程(评价内容="好评好评!好好吃!")
        # a = dr.get_toast_byid()
        a = dr.get_toast("匿名评论")
        logging.info("toast提示为:"+"评分不能为空")
        self.myEq("匿名评论",a,"test_002_评分为空提示")

    def test_003_评论为空提示(self):
        logging.info("=====test_003_评论为空提示=====")
        dr=page_填写评论(self.driver)
        dr.bus_填写评论_流程(选择星级=5)
        # a = dr.get_toast_byid()
        a = dr.get_toast("匿名评论")
        logging.info("toast提示为:"+"描述不能为空")
        self.myEq("匿名评论",a,"test_003_评论为空提示")

    def test_004_主流程全部填写(self):
        logging.info("=====test_004_主流程全部填写=====")
        dr=page_填写评论(self.driver)
        dr.bus_填写评论_流程(勾选匿名=True,选择星级=5,评价内容="便民超市,物美价廉,货物丰富!",上传图片="1-0")
        # a = dr.get_toast_byid()
        a = dr.get_toast("评论此商家")
        logging.info("toast提示为:"+"评论提交成功，审核通过后发布")
        self.myEq("评论此商家",a,"test_004_主流程全部填写")

    def test_005_主流程不上传图片(self):
        logging.info("=====test_005_主流程不上传图片=====")
        dr=page_填写评论(self.driver)
        dr.bus_填写评论_流程(勾选匿名=True,选择星级=5,评价内容="便民超市,物美价廉,货物丰富!")
        # a = dr.get_toast_byid()
        a = dr.get_toast("评论此商家")
        logging.info("toast提示为:"+"评论提交成功")
        self.myEq("评论此商家",a,"test_005_主流程不上传图片")

    def test_006_主流程不上传图片不匿名(self):
        logging.info("=====test_006_主流程不上传图片不匿名=====")
        dr=page_填写评论(self.driver)
        dr.bus_填写评论_流程(选择星级=5,评价内容="此超市很赞")
        # a = dr.get_toast_byid()
        a = dr.get_toast("评论此商家")
        logging.info("toast提示为:"+"评论提交成功")
        self.myEq("评论此商家",a,"test_006_主流程不上传图片不匿名")

    def test_007_主流程不匿名(self):
        logging.info("=====test_007_主流程不匿名=====")
        dr=page_填写评论(self.driver)
        dr.bus_填写评论_流程(选择星级=5,评价内容="便民超市,物美价廉,货物丰富!",上传图片="1-0")
        # a = dr.get_toast_byid()
        a = dr.get_toast("评论此商家")
        logging.info("toast提示为:"+"评论提交成功，审核通过后发布")
        self.myEq("评论此商家",a,"test_007_主流程不匿名")

    def test_008_评论少于5个字(self):
        logging.info("=====test_008_评论少于5个字=====")
        dr=page_填写评论(self.driver)
        dr.bus_填写评论_流程(选择星级=5,评价内容="物美价廉",上传图片="1-0")
        a = dr.get_toast("匿名评论")
        logging.info("toast提示为:"+"描述至少五个字")
        self.myEq("匿名评论",a,"test_008_评论少于5个字")

    def tearDown(self):
        dr=page_填写评论(self.driver)
        dr.tc_后置回首页()

if __name__ == '__main__':
    import unittest
    unittest.main()