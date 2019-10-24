import allure
from appium.webdriver.common.touch_action import TouchAction
from function.funcdate import *
from common.loc import *
from businessView.page_车次途经站点 import page_车次途经站点
from common.request import *


class page_车次详情(page_车次途经站点):


    btn_车次详情_分享按钮 = loc_id("ATtrip3_1")

    btn_车次详情_行李托运 = loc_text('行李托运')
    btn_车次详情_undefined = loc_contains_text_instance('und',0)
    btn_车次详情_null = loc_contains_text_instance('nu',0)
    btn_展开 = loc_text("展开")
    btn_收起 = loc_text("收起")
    btn_电源位置 = loc_text("电源位置")
    btn_行程天气 = loc_text("行程天气")
    btn_分享给朋友 = loc_text("推荐给朋友")
    btn_关闭 = loc_text("关闭")

    @allure.step(title='点击分享弹框_关闭')
    def click_关闭(self):
        return self.click_点击(self.btn_关闭, "btn_关闭")

    @allure.step(title='点击行程详情_展开')
    def click_行程详情_展开(self):
        return self.find_loc_with_scroll("展开")

    @allure.step(title='点击行程详情_电源位置')
    def click_行程详情_电源位置(self):
        return self.find_loc_with_scroll("电源位置")

    def click_行程详情_收起(self):
        return self.find_loc_with_scroll("收起")

    def click_行程详情_天气(self):
        return self.find_loc_with_scroll("行程天气")

    @allure.step(title='获取候车指数文本')
    def check_候车指数(self):
        a0 = []
        a1 = ["车站客流负荷","排队进站耗时","今日发送旅客", "今日发送车次","今日晚点车次","今日增开车次"]
        for i in a1:
            text = self.get_text(i)
            a0.append(text)
        return a0

    @allure.step(title='获取列车信息文本')
    def check_列车信息(self):
        a0 = []
        a1 = ["列车型号","定员","编组", "车上WiFi","餐车","最高时速","充电电源"]
        for i in a1:
            text = self.get_text(i)
            a0.append(text)
        return a0

    @allure.step(title='获取行程天气文本')
    def check_行程天气( self ):
        a = loc_text("行程天气")
        return self.get_元素文本(a, "获取行程天气文本")

    @allure.step(title='点击车次详情_分享')
    def click_车次详情_分享按钮(self):
        # return self.click_点击(self.btn_车次详情_分享按钮,"btn_行程详情分享")
        logging.info("点击分享按钮" )
        time.sleep(5)
        a = self.get_screenSize()
        x = a[0] * 0.88
        y = a[1] * 0.755
        return TouchAction(self.driver).tap(x=x, y=y).perform()

    def get_车次详情_行李托运(self):
        return self.get_元素文本(self.btn_车次详情_行李托运,'btn_车次详情_行李托运')

    def check_车次详情_undefined(self):
        """
        :return: 返回结果正常为11
        """
        a1=self.judge_元素(self.btn_车次详情_undefined)
        a2=self.judge_元素(self.btn_车次详情_null)
        return str(a1)+str(a2)

    def bus_车次详情_行程绑定成功(self):
        """
        :return: 返回结果正常为111
        """
        a1=self.get_车次详情_行李托运()
        a2 =self.check_车次详情_undefined()
        return str(a1)+str(a2)