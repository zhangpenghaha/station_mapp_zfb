import allure

from common.loc import *
from common.common import common


class page_个人中心(common):
    "定位器"

    btn_个人中心_我的资料 = loc_start_text("张鹏")

    btn_个人中心_任务中心 = loc_text("任务中心")
    btn_个人中心_优惠价 = loc_text("优惠券")
    btn_个人中心_积分商城 = loc_text("积分商城")

    btn_个人中心_我的12306 = loc_text("我的12306")
    btn_个人中心_我的行程 = loc_text("我的行程")
    btn_个人中心_意见反馈 = loc_text("意见反馈")


    "页面提示文案"

    "功能正在拼命完善中，敬请期待！"
    txt_个人中心_完善中=loc_contains_text("敬请期待")

    "=================操作层===================="

    @allure.step(title='点击_个人中心_我的资料')
    def click_个人中心_会员号(self):
        return self.click_点击(self.btn_个人中心_我的资料, "btn_个人中心_我的资料")

    @allure.step(title='点击_个人中心_任务中心')
    def click_个人中心_任务中心(self):
        return self.click_点击(self.btn_个人中心_任务中心, "btn_个人中心_任务中心")

    @allure.step(title='点击_个人中心_积分商城')
    def click_个人中心_积分商城(self):
        return self.click_点击(self.btn_个人中心_积分商城, "btn_个人中心_积分商城")

    @allure.step(title='点击_个人中心_优惠价')
    def click_个人中心_优惠券(self):
        return self.click_点击(self.btn_个人中心_优惠价, "btn_个人中心_优惠价")


    def wait_个人中心(self):
        return self.wait_显式等待(10, self.btn_个人中心_意见反馈)

    @allure.step(title='点击_个人中心_我的12306')
    def click_个人中心_我的12306(self):
        return self.click_点击(self.btn_个人中心_我的12306, "btn_个人中心_我的12306")

    @allure.step(title='点击_个人中心_我的行程')
    def click_个人中心_我的行程(self):
        return self.click_点击(self.btn_个人中心_我的行程, "btn_个人中心_我的行程")

    @allure.step(title='点击_个人中心_意见反馈')
    def click_个人中心_意见反馈(self):
        return self.click_点击(self.btn_个人中心_意见反馈, "btn_个人中心_意见反馈")

    "提示文案获取"
    def get_个人中心_完善中_提示(self):
        return self.get_元素文本(self.txt_个人中心_完善中,"txt_个人中心_完善中")


if __name__ == '__main__':
    from appiumDriver.desired_caps import appium_微信车站通

    dr = appium_微信车站通()
