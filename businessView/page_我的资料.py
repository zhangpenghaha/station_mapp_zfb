from businessView.page_个人中心 import page_个人中心
from common.loc import *
from time import sleep
import logging
import allure

class page_我的资料(page_个人中心):
    "定位器"

    btn_我的资料_男 = loc_text("男")  # 无效定位
    btn_我的资料_女 = loc_text("女")  # 无效定位
    text_我的资料_年 = loc_id_instance("android:id/numberpicker_input", 0)
    text_我的资料_月 = loc_id_instance("android:id/numberpicker_input", 1)
    text_我的资料_日 = loc_id_instance("android:id/numberpicker_input", 2)

    # btn_我的资料_上年 = loc_child_CtoC_Number("com.tencent.mm.ui.widget.picker.YADatePicker", "android.widget.Button", 0)
    # btn_我的资料_下年 = loc_child_CtoC_Number("com.tencent.mm.ui.widget.picker.YADatePicker", "android.widget.Button", 1)
    # btn_我的资料_上月 = loc_child_CtoC_Number("com.tencent.mm.ui.widget.picker.YADatePicker", "android.widget.Button", 2)
    # btn_我的资料_下月 = loc_child_CtoC_Number("com.tencent.mm.ui.widget.picker.YADatePicker", "android.widget.Button", 3)
    # btn_我的资料_上日 = loc_child_CtoC_Number("com.tencent.mm.ui.widget.picker.YADatePicker", "android.widget.Button", 4)
    # btn_我的资料_下日 = loc_child_CtoC_Number("com.tencent.mm.ui.widget.picker.YADatePicker", "android.widget.Button", 5)
    btn_我的资料_上年 = loc_child_CtoC_Number("android.widget.DatePicker", "android.widget.Button", 0)
    btn_我的资料_下年 = loc_child_CtoC_Number("android.widget.DatePicker", "android.widget.Button", 1)
    btn_我的资料_上月 = loc_child_CtoC_Number("android.widget.DatePicker", "android.widget.Button", 2)
    btn_我的资料_下月 = loc_child_CtoC_Number("android.widget.DatePicker", "android.widget.Button", 3)
    btn_我的资料_上日 = loc_child_CtoC_Number("android.widget.DatePicker", "android.widget.Button", 4)
    btn_我的资料_下日 = loc_child_CtoC_Number("android.widget.DatePicker", "android.widget.Button", 5)

    text_我的资料_出生日期 = loc_contains_text("-")

    btn_我的资料_您的手机号 = loc_text("您的手机号")
    btn_我的资料_所在城市 = loc_text("所在城市")
    btn_我的资料_出生日期 = loc_text("出生日期")
    btn_首页 = loc_text("首页")

    "操作层"

    @allure.step(title='点击首页')
    def click_点击首页(self):
        self.click_点击(self.btn_首页, "点击首页")

    @allure.step(title='获取手机号文本')
    def get_text_您的手机号(self):
        return self.get_元素文本(self.btn_我的资料_您的手机号, "btn_您的手机号")

    @allure.step(title='点击我的资料_所在城市')
    def click_所在城市(self):
        self.click_点击(self.btn_我的资料_所在城市, "btn_所在城市")

    @allure.step(title='点击_我的资料_出生日期')
    def click_出生日期(self):
        self.click_点击(self.btn_我的资料_出生日期, "btn_出生日期")

    @allure.step(title='获取出生日期文本')
    def get_出生日期(self):
        return self.get_元素文本(self.text_我的资料_出生日期, "text_出生日期")

    @allure.step(title='点击我的资料_男')
    def click_男(self):
        self.click_点击(self.btn_我的资料_男, "btn_男")

    @allure.step(title='点击我的资料_女')
    def click_女(self):
        self.click_点击(self.btn_我的资料_女, "btn_女")

    "日期选择控件"

    @allure.step(title='获取选择后_向上点年份')
    def swipe_年向上(self):
        self.act_滑动_AtoB(self.btn_我的资料_下年, self.text_我的资料_年, "下年","年")
        sleep(1)
        return self.get_元素文本(self.text_我的资料_年, "获取选择后点年份")

    @allure.step(title='获取选择后_向下点年份')
    def swipe_年向下(self):
        self.act_滑动_AtoB(self.btn_我的资料_上年, self.text_我的资料_年, "上年","年")
        sleep(1)
        return self.get_元素文本(self.text_我的资料_年, "获取选择后点年份")

    @allure.step(title='向上选择月份')
    def swipe_月向上(self):
        self.act_滑动_AtoB(self.btn_我的资料_下月, self.text_我的资料_月, "下月","月")
        sleep(1)
        return self.get_元素文本(self.text_我的资料_月, "获取选择后点月份")

    @allure.step(title='向下选择月份')
    def swipe_月向下(self):
        self.act_滑动_AtoB(self.btn_我的资料_上月, self.text_我的资料_月, "上月","月")
        sleep(1)
        return self.get_元素文本(self.text_我的资料_月, "获取选择后点月份")

    @allure.step(title='向上选择日期')
    def swipe_日向上(self):
        self.act_滑动_AtoB(self.btn_我的资料_下日, self.text_我的资料_日, "下日","日")
        sleep(1)
        return self.get_元素文本(self.text_我的资料_日, "获取选择后点月份")

    @allure.step(title='向下选择日期')
    def swipe_日向下(self):
        self.act_滑动_AtoB(self.btn_我的资料_上日, self.text_我的资料_日,"上日","日")
        sleep(1)
        return self.get_元素文本(self.text_我的资料_日, "获取选择后点月份")

    "业务层"

    @allure.step(title='修改日期')
    def bus_修改日期(self, 确定or取消):
        logging.info("=====开始修改出生日期业务====")
        tmpA = self.get_出生日期()
        logging.info("选择前的出生年月日为:" + str(tmpA))
        self.click_出生日期()
        year = self.swipe_年向上()
        logging.info("选择的出生年为:" + str(year))
        month = self.swipe_月向上()
        if int(month) < 10:
            month = "0" + str(month)
        logging.info("选择的出生月为:" + str(month))
        day = self.swipe_日向上()
        logging.info("选择的出生日为:" + str(day))
        tmpC = year + "-" + month + "-" + day
        logging.info("选择后的出生年月日为:" + str(tmpC))
        if 确定or取消 == "确定":
            self.click_确定()
            tmpB = self.get_出生日期()
            logging.info("修改后的出生年月日为:" + str(tmpB))
            return judgement(tmpB, tmpC)
        elif 确定or取消 == "取消":
            self.click_取消()
            tmpD = self.get_出生日期()
            logging.info("取消修改后的出生年月日为:" + str(tmpD))
            return judgement(tmpA, tmpD)
        else:
            logging.error("参数输入错误!!!")


if __name__ == '__main__':
    from appiumDriver.desired_caps import appium_微信车站通

    driver = appium_微信车站通()
    dr = page_我的资料(driver)
    dr.click_我的按钮()
    dr.click_个人中心_会员号()
    dr.bus_修改日期("确认")
