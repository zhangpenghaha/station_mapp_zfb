import time

import allure

from myUnit.st_首页 import st_首页
from businessView.page_切换站点 import page_切换站点
from businessView.page_首页 import page_首页
from businessView.page_公告详情 import page_公告详情
from businessView.page_车站天气 import page_车站天气
from businessView.page_玩转车站 import page_玩转车站

from common.common import common
from time import sleep
import logging
from businessView.page_车站头条 import page_车站头条
from businessView.page_选择日期 import page_选择日期
from businessView.page_选择车次 import page_选择车次
from businessView.page_车站流量 import page_车站流量
from businessView.page_车站大屏 import page_车站大屏
from businessView.page_站内商业 import page_站内商业
from businessView.page_首页底部服务页面 import page_首页底部服务页面
from function.funcdate import *


class tc_首页(st_首页):
    def setUp(self):
        logging.info("=====前置条件=====")
        dr = common(self.driver)
        dr.act_下滑(3)
        time.sleep(3)

    "站点切换页面跳转"

    def test_002_点击切换站点toast切换站点_武昌站(self):
        logging.info("=====test_002_点击切换站点toast切换站点_武昌站=====")
        dr = page_首页(self.driver)
        # 返回预期为:定位显示您在“武昌站”附近
        # a1 = dr.get_首页_切换站点提示()
        # # 返回预期为:1
        # a2 = dr.click_首页_切换站点提示按钮()
        # # 返回预期为:武昌站
        # a3 = dr.get_首页顶部_当前站点()
        # a = a1 + str(a2) + a3
        # self.myEq(a, '定位显示您在“武昌站”附近True武昌站', "点击切换站点toast切换站点_武昌站")
        dr.click_首页_切换站点按钮()
        dr = page_切换站点(self.driver)
        dr.bus_切换站点_切换到指定站点("武昌")
        a = dr.get_toast("武昌站")
        self.myEq(a, "武昌站", "点击切换站点")

    def test_005_站点切换页面调转(self):
        logging.info("=====test_005_站点切换页面调转=====")
        dr = page_首页(self.driver)
        dr.click_首页_切换站点按钮()
        a = dr.get_toast("切换站点")
        self.myEq(a, "切换站点", "首页站点切换页面调转")

    def test_007_首页天气页面跳转(self):
        logging.info("=====test_007_首页天气页面跳转=====")
        dr = page_首页(self.driver)
        dr.click_首页_天气页面()
        dr = page_车站天气(self.driver)
        a = dr.get_toast("车站天气")
        self.myEq(a, "车站天气", "test_007_首页天气页面跳转")

    # def rtest_010_banner车站流量跳转(self):
    #     logging.info("=====test_010_banner车站流量跳转=====")
    #     dr = page_首页(self.driver)
    #     dr.click_首页_banner_1()
    #     dr = page_车站流量(self.driver)
    #     a = dr.get_车站流量_旅客流量()
    #     self.myEq(a, "旅客流量", "banner车站流量跳转")
    #
    # def rtest_011_车站流量旅客流量字段检查(self):
    #     logging.info("=====test_011_车站流量旅客流量字段检查=====")
    #     dr = page_车站流量(self.driver)
    #     dr.click_首页_banner_1()
    #     dr.check_车站流量_车次流量or旅客流量("旅客流量")
    #     # self.myEq(a, ["今日发送旅客", "今日接收旅客", "车站客流负荷", "排队进站耗时", "步行到检票口"], "test_011_车站流量旅客流量字段检查")
    #     a = dr.get_toast("今日接收旅客")
    #     self.myEq(a, "今日接收旅客", "test_011_车站流量旅客流量字段检查")
    #
    #
    # def rtest_012_车站流量车次流量字段检查(self):
    #     logging.info("=====test_012_车站流量车次流量字段检查=====")
    #     dr = page_车站流量(self.driver)
    #     dr.click_首页_banner_1()
    #     dr.click_车站流量_旅客流量()
    #     dr.check_车站流量_车次流量or旅客流量("车次流量")
    #     # self.myEq(a, ["今日发送车次", "今日接收车次", "今日增开车次", "今日晚点车次", "今日停运车次", "未来1小时发送"], "test_012_车站流量车次流量字段检查")
    #     a = dr.get_toast("今日接收车次")
    #     self.myEq(a, "今日接收车次",  "test_012_车站流量车次流量字段检查")
    #
    # def rtest_013_车站流量到达大屏字段检查(self):
    #     logging.info("=====test_013_车站流量到达大屏字段检查=====")
    #     dr = page_车站流量(self.driver)
    #     dr.click_首页_banner_1()
    #     dr.check_车站流量_候车大屏or到达大屏("到达大屏")
    #     # self.myEq(a, ["车次", "始发站", "到本站", "出站口", "状态"], "test_013_车站流量到达大屏字段检查")
    #     a = dr.get_toast("到本站")
    #     self.myEq(a, "到本站", "test_013_车站流量到达大屏字段检查")
    #
    # def rtest_014_车站流量候车大屏字段检查(self):
    #     logging.info("=====test_014_车站流量候车大屏字段检查=====")
    #     dr = page_车站流量(self.driver)
    #     dr.click_首页_banner_1()
    #     dr.click_车站流量_到达大屏()
    #     # a = dr.check_车站流量_候车大屏or到达大屏("候车大屏")
    #     # self.myEq(a, ["车次", "终到站", "发车", "检票口", "状态"], "test_014_车站流量候车大屏字段检查")
    #     a = dr.get_toast("检票口")
    #     self.myEq(a, "检票口", "test_014_车站流量候车大屏字段检查")
    #
    #
    # def rtest_015_车站流量车站大屏跳转(self):
    #     logging.info("=====test_015_车站流量车站大屏跳转=====")
    #     dr = page_车站流量(self.driver)
    #     dr.click_首页_banner_1()
    #     dr.act_上滑(3)
    #     dr.click_车站流量_查看全部车次()
    #     dr = page_车站大屏(self.driver)
    #     a = dr.get_点击车次查看详情文案()
    #     self.myEq(a, "点击车次 查看详情", "test_015_车站流量车站大屏跳转")


    # def test_017_车站流量正晚点查询跳转(self):
    #     logging.info("=====test_017_车站流量正晚点查询跳转=====")
    #     dr = page_车站流量(self.driver)
    #     dr.click_首页_banner_1()
    #     dr.click_车站流量_时刻查询()
    #     a = dr.get_toast_byIDtoText("正晚点查询")
    #     self.myEq(a, "正晚点查询", "test_017_车站流量正晚点查询跳转")

    # def rtest_018_车站流量行李托运跳转(self):
    #     logging.info("=====test_018_车站流量行李托运跳转=====")
    #     dr = page_车站流量(self.driver)
    #     dr.click_首页_banner_1()
    #     dr.act_上滑(3)
    #     dr.click_车站流量_行李托运()
    #     a = dr.get_toast_byIDtoText("行李托运")
    #     self.myEq(a, "行李托运", "test_018_车站流量行李托运跳转")
    #
    # def rtest_019_车站流量车站地图跳转(self):
    #     logging.info("=====test_019_车站流量车站地图跳转=====")
    #     dr = page_车站流量(self.driver)
    #     dr.click_首页_banner_1()
    #     dr.act_上滑(2)
    #     dr.click_车站流量_车站地图()
    #     dr = page_玩转车站(self.driver)
    #     a = dr.get_玩转车站_实时共享()
    #     self.myEq(a, "实时共享", "test_019_车站流量车站地图跳转")

    "切换到浠水站"

    def test_020_切换到测试站点_浠水站(self):
        logging.info("=====test_012_切换到测试站点_浠水站=====")
        dr = page_切换站点(self.driver)
        dr.click_首页_切换站点按钮()
        dr.bus_切换站点_切换到指定站点("浠水")
        a = dr.get_toast('浠水站')
        self.myEq(a, "浠水站", "切换到测试站点_浠水站")

    def test_026_余票查询跳转(self):
        logging.info("=====test_026_余票查询跳转=====")
        dr = page_首页(self.driver)
        dr.click_余票查询()
        a = dr.get_toast("查询")
        self.myEq(a, "查询", '切换到余票查询页面')


    def test_027_更多服务屏幕跳转(self):
        logging.info("=====test_015_更多服务屏幕跳转=====")
        dr = page_首页(self.driver)
        dr.click_更多服务_菜单()
        a = dr.get_更多服务模块标题()
        self.myEq(a, "更多服务", "更多服务屏幕跳转")

    def test_028_公告详情页面跳转(self):
        logging.info("=====test_020_公告详情页面跳转=====")
        dr = page_首页(self.driver)
        dr.click_滚动公告()
        a = dr.get_toast("车站公告")
        self.myEq(a, "车站公告", "公告详情页面跳转")

    def test_029_更多资讯页面跳转(self):
        logging.info("=====test_025_更多资讯页面跳转=====")
        dr = page_首页(self.driver)
        dr.click_更多资讯()
        dr = page_车站头条(self.driver)
        a = dr.get_车站头条_车站资讯()
        self.myEq(a, "车站资讯", "更多资讯页面跳转")

    "时刻查询"
    "车次查询"

    def test_030_车次号为空toast提示(self):
        logging.info("=====test_030_车次号为空toast提示=====")
        dr = page_首页(self.driver)
        time.sleep(3)
        dr.act_上滑(1)
        dr.click_首页_时刻查询_查询()
        a = dr.get_toast("时刻查询")
        self.myEq(a, "时刻查询", "请输入正确的车次号_toast")

    def test_031_车次查询摄像头调用(self):
        logging.info("=====test_031_车次查询摄像头调用=====")
        dr = page_首页(self.driver)
        dr.click_首页_车次查询()
        dr.click_首页_摄像头()
        a = dr.get_二维码提示()
        dr.click_支付宝返回()
        self.myEq(a, "将二维码放入框内，即可自动扫描", "车次查询摄像头调用")

    def test_032_站站查询标签页切换(self):
        logging.info("=====test_032_站站查询标签页切换=====")
        dr = page_首页(self.driver)
        time.sleep(3)

        dr.click_首页_站站查询()
        a = dr.get_站站查询_目的地_北京()
        self.myEq(a, "北京", "站站查询标签页切换")

    def test_033_车次查询标签页切换(self):
        logging.info("=====test_033_车次查询标签页切换=====")
        dr = page_首页(self.driver)
        dr.click_首页_车次查询()
        a = dr.get_车次号输入框示例()
        self.myEq(a, "例如: G520", "车次查询标签页切换")

    def test_034_时刻查询选择日期页面跳转(self):
        logging.info("=====test_034_时刻查询选择日期页面跳转=====")
        dr = page_首页(self.driver)
        # dr.act_上滑(1)
        dr.act_滑动_AtoB(dr.btn_首页_车次查询, dr.btn_车站大屏, "车次查询", "车站大屏")
        dr.click_出发时间_今天()
        dr = page_选择日期(self.driver)
        a = dr.get_toast("选择日期")
        self.myEq(a, "选择日期", "时刻查询选择日期页面跳转")

    # def test_035_时刻查询车次号校验_toast提示(self):
    #     logging.info("=====test_035_时刻查询车次号校验_toast提示=====")
    #     dr = page_首页(self.driver)
    #     dr.click_车次号输入()
    #     dr.act_键盘输入("G")
    #     dr.click_首页_时刻查询_查询()
    #     a = dr.get_请输入正确的车次号_toast()
    #     dr.click_确定()
    #     dr.click_首页_站站查询()
    #     self.myEq(a, "请输入正确的车次号", "时刻查询车次号校验_toast提示")

    # def test_036_查询正确的车次号跳转(self):
    #     dr=page_首页(self.driver)
    #     dr.click_车次查询()
    #     dr.click_车次号输入()
    #     dr.act_键盘输入("Z366")
    #     dr.click_时刻查询_查询()
    #     dr.click_确认()
    #     a=dr.get_title()
    #     self.myEq(a,"Z366","查询正确的车次号跳转")

    def test_037_时刻查询_站站查询结果跳转(self):
        logging.info("=====test_037_时刻查询_站站查询结果跳转=====")
        dr = page_首页(self.driver)
        time.sleep(3)
        dr.click_首页_站站查询()
        dr.act_上滑()
        dr.click_首页_时刻查询_查询()
        dr = page_选择车次(self.driver)
        a = dr.get_toast("武汉-北京")
        self.myEq(a, "武汉-北京", "时刻查询_站站查询结果跳转")

    def test_038_站站查询_切换起始站点按钮(self):
        logging.info("=====test_038_站站查询_切换起始站点按钮=====")
        dr = page_首页(self.driver)
        dr.click_首页_切换起始站点()
        dr.act_上滑()
        dr.click_首页_时刻查询_查询()
        dr = page_选择车次(self.driver)
        a = dr.get_toast("北京-武汉")
        self.myEq(a, "北京-武汉", "站站查询_切换起始站点按钮")

    "封腰"

    "车站大屏"

    def test_045_首页_到达切换(self):
        logging.info("=====test_045_首页_到达切换=====")
        dr = page_首页(self.driver)
        dr.act_滑动_byYourSelf(dr.txt_首页_时刻查询模块名, 0.5, 0.15, "txt_时刻查询模块_标题移动到0.15位置")
        dr.act_滑动_byYourSelf(dr.btn_首页车站大屏_候车按钮, 0.5, 0.3, "btn_首页车站大屏_候车按钮移动到0.3位置")
        dr.click_首页车站大屏_到达()
        a = dr.get_首页车站大屏_始发站()
        self.myEq(a, "始发站", "首页_到达切换")

    def test_048_首页_候车切换(self):
        logging.info("=====test_048_首页_候车切换=====")
        dr = page_首页(self.driver)
        dr.act_滑动_byYourSelf(dr.txt_首页_时刻查询模块名, 0.5, 0.15, "txt_时刻查询模块_标题移动到0.15位置")
        dr.act_滑动_byYourSelf(dr.btn_首页车站大屏_候车按钮, 0.5, 0.3, "btn_首页车站大屏_候车按钮移动到0.3位置")
        dr.click_首页车站大屏_候车()
        a = dr.get_首页车站大屏_终到站()
        self.myEq(a, "终到站", "首页_候车切换")

    def test_050_车站大屏页面跳转(self):
        logging.info("=====test_050_车站大屏页面跳转=====")
        dr = page_首页(self.driver)
        dr.act_滑动_byYourSelf(dr.txt_首页_时刻查询模块名, 0.5, 0.15, "txt_首页_时刻查询模块名移动到0.15位置")
        dr.act_滑动_byYourSelf(dr.btn_首页车站大屏_候车按钮, 0.5, 0.3, "btn_首页车站大屏_候车按钮移动到0.3位置")
        dr.click_查看全部车次()
        dr = page_车站大屏(self.driver)
        a = dr.get_点击车次查看详情文案()
        self.myEq(a, "点击车次 查看详情", "车站大屏页面跳转")

    "车站商业"

    def test_060_查看全部跳转站内商业(self):
        logging.info("=====test_060_查看全部跳转站内商业=====")
        dr = page_首页(self.driver)
        dr.act_滑动_byYourSelf(dr.txt_首页_时刻查询模块名, 0.5, 0.15, "txt_首页_时刻查询模块名移动到0.15位置")
        dr.act_滑动_byYourSelf(dr.btn_首页车站大屏_候车按钮, 0.5, 0.3, "btn_首页车站大屏_候车按钮移动到0.3位置")
        dr.act_滑动_byYourSelf(dr.txt_首页_车站商业模块名, 0.5, 0.3, "txt_首页_车站商业模块名移动到0.3位置")
        dr.click_首页_车站商业查看全部()
        dr = page_站内商业(self.driver)
        a = dr.get_站内商业_智能排序()
        self.myEq(a, "智能排序", "查看全部跳转站内商业")

    def test_065_进站后按钮切换(self):
        logging.info("=====test_065_进站后按钮切换=====")
        dr = page_首页(self.driver)
        dr.act_滑动_byYourSelf(dr.txt_首页_时刻查询模块名, 0.5, 0.15, "txt_首页_时刻查询模块名移动到0.15位置")
        dr.act_滑动_byYourSelf(dr.btn_首页车站大屏_候车按钮, 0.5, 0.3, "btn_首页车站大屏_候车按钮移动到0.3位置")
        dr.act_滑动_byYourSelf(dr.txt_首页_车站商业模块名, 0.5, 0.3, "txt_首页_车站商业模块名移动到0.3位置")
        dr.click_首页_车站商业进站后()
        a = dr.get_首页_车站商业进站后1号位()
        self.myEq(a, "平价自选商店", "进站后按钮切换,定位平价自选商店")

    def test_068_进站前按钮切换(self):
        logging.info("=====test_068_进站前按钮切换=====")
        dr = page_首页(self.driver)
        dr.act_滑动_byYourSelf(dr.txt_首页_时刻查询模块名, 0.5, 0.15, "txt_首页_时刻查询模块名移动到0.15位置")
        dr.act_滑动_byYourSelf(dr.btn_首页车站大屏_候车按钮, 0.5, 0.3, "btn_首页车站大屏_候车按钮移动到0.3位置")
        dr.act_滑动_byYourSelf(dr.txt_首页_车站商业模块名, 0.5, 0.3, "txt_首页_车站商业模块名移动到0.3位置")
        dr.click_首页_车站商业进站前()
        a = dr.get_首页_车站商业进站前1号位()
        self.myEq(a, "便民超市", "进站后按钮切换,定位便民超市")


    "=====更多服务====="


    def test_075_功能待完善提示(self):
        logging.info("=====test_075_功能待完善提示=====")
        dr = page_首页(self.driver)
        dr.act_上滑(3)
        dr.click_首页更多服务_服务项("饮水处")
        a = dr.get_toast("注意事项")
        self.myEq(a, "注意事项", "功能待完善提示")


    "首页底部服务页面"


    def test_100_首页军人优先跳转(self):
        logging.info("=====test_100_首页军人优先跳转=====")
        dr = page_首页(self.driver)
        dr.act_上滑(4)
        dr.click_首页军人优先()
        dr = page_首页底部服务页面(self.driver)
        a = dr.get_军人优先_文章标题()
        self.myEq(a, "【军人优先】风里雨里你在前，铁路出行你优先", "test_100_首页军人优先跳转")


    def test_105_首页常见问题跳转(self):
        logging.info("=====test_105_首页常见问题跳转=====")
        dr = page_首页(self.driver)
        dr.act_上滑(4)
        dr.click_首页常见问题()
        dr = page_首页底部服务页面(self.driver)
        a = dr.get_常见问题_文章标题()
        self.myEq(a, "出行常见问题之火车票相关", "test_105_首页常见问题跳转")


    def test_110_首页服务评价跳转(self):
        logging.info("=====test_110_首页服务评价跳转=====")
        dr = page_首页(self.driver)
        dr.act_上滑(4)
        dr.click_首页服务评价()
        dr = page_首页底部服务页面(self.driver)
        a = dr.get_服务评价_文章标题()
        self.myEq(a, "【服务评价】欢迎您对铁路出行服务进行评价！", "test_105_首页常见问题跳转")


    def test_115_首页关于我们跳转(self):
        logging.info("=====test_115_首页关于我们跳转=====")
        dr = page_首页(self.driver)
        dr.act_上滑(4)
        dr.click_首页关于我们()
        dr = page_首页底部服务页面(self.driver)
        a = dr.get_关于我们_文章标题()
        self.myEq(a, "威泰科技", "test_105_首页常见问题跳转")


    def tearDown(self):
        dr = page_选择车次(self.driver)
        dr.screenshot_as_png()
        dr.tc_后置回首页()



if __name__ == '__main__':
    import unittest
    unittest.main()
