# coding:utf8
import time
import allure
from common.loc import *
import logging
import xlrd

from baseView.baseView import baseView
from appium.webdriver.common.touch_action import TouchAction


class common(baseView):
    "定位器"
    "弹窗"
    btn_确定添加 = loc_text("确定添加")
    btn_确认添加 = loc_text("确认添加")
    btn_确定 = loc_text("确定")
    btn_确认 = loc_text("确认")
    btn_取消 = loc_text("取消")
    btn_后一天 = loc_text("后一天")
    toast_单个按钮弹出提示 = loc_id("com.tencent.mm:id/dcf")

    "退出键盘"
    btn_退出小键盘 = loc_class("android.widget.Image")

    btn_支付宝返回 = loc_desc("退出")

    "title"

    txt_title = loc_id("com.tencent.mm:id/ph")

    "系统摄像头-text:我的二维码"
    # text_二维码提示 = loc_id("com.tencent.mm:id/eb7")   #com.tencent.mm:id/ejr
    text_二维码提示 = loc_text("将二维码放入框内，即可自动扫描")
    "图片选择"
    btn_从相册选择 = loc_text("从相册选择")
    # btn_图片选择返回 = loc_id("com.tencent.mm:id/la")
    btn_图片选择返回 = loc_id("com.alipay.mobile.beephoto: id / bt_back")
    btn_完成 = loc_class_instance("android.widget.Button",0)
    btn_意见个人中心 = loc_id("com.tencent.mm:id/p9")
    # btn_返回 = loc_id("com.alipay.mobile.nebula:id/h5_tv_nav_back")
    btn_返回 = loc_desc("返回")
    btn_首页 = loc_text("首页")
    btn_行程 = loc_text("行程")
    btn_玩转车站 = loc_text("玩转车站")
    btn_我的 = loc_text("我的")

    def screenshot_as_png(self):
        allure.attach("截图", self.driver.get_screenshot_as_png(), allure.attach_type.PNG)

    def click_后一天(self):
        return self.click_点击(self.btn_后一天, "btn_后一天")

    @allure.step(title='获取二维码提示')
    def get_二维码提示(self):
        return self.get_元素文本(self.text_二维码提示, "text_二维码提示")

    def click_点击文本(self, text):
        return self.click_点击(loc_text(text), text)

    @allure.step(title='获取文本提示')
    def get_text(self, toast_tip):
        return self.get_元素文本(loc_text(toast_tip), "获取 " + toast_tip + " 文本")

    @allure.step(title='获取toast提示')
    def get_toast(self,toast_tip):
        return self.get_元素文本(loc_text(toast_tip), "toast_提示:"+toast_tip)

    @allure.step(title='获取toast提示')
    def get_toast_byid(self):
        return self.get_元素文本(loc_id_instance("com.tencent.mm:id/d0",0), "toast_提示")

    @allure.step(title='获取toast提示')
    def get_toast_byclass(self):
        return self.get_元素文本(loc_class_instance("android.widget.TextView",0),"toast_提示")

    @allure.step(title='获取toast提示')
    def get_toast_byIDtoText(self,Text):
        return self.get_元素文本(loc_child_IDtoT("com.tencent.mm:id/pf",Text),"toast_提示")

    @allure.step(title='点击完成')
    def click_完成(self):
        self.click_点击(self.btn_完成, "btn_完成")

    @allure.step(title='选择图片')
    def choose_图片(self, number, startNumber=0):
        for i in range(number):
            self.click_点击(loc_class_instance("android.widget.CheckBox", i + startNumber), "选择第" + str(i + 1) + "张图片!")
        self.click_完成()

    @allure.step(title='获取标题信息')
    def get_title(self):
        return self.get_元素文本(self.txt_title, "txt_title")

    @allure.step(title='点击确定添加')
    def click_确定添加(self):
        return self.click_点击(self.btn_确定添加, "点击确定按钮!")

    @allure.step(title='点击确认')
    def click_确认(self):
        return self.click_点击(self.btn_确认, "点击确认按钮!")

    @allure.step(title='点击确定')
    def click_确定(self):
        return self.click_点击(self.btn_确定, "点击确定按钮")

    @allure.step(title='点击确认添加')
    def click_确认添加(self):
        # allure.attach("截图", self.driver.get_screenshot_as_png(), allure.attach_type.PNG)
        return self.click_点击(self.btn_确认添加, "点击确认添加按钮")

    @allure.step(title='点击取消')
    def click_取消(self):
        return self.click_点击(self.btn_取消, "点击取消按钮!")

    @allure.step(title='点击支付宝返回')
    def click_支付宝返回(self):
        return self.click_点击(self.btn_支付宝返回, "支付宝返回")

    @allure.step(title='点击首页')
    def click_首页(self):
        self.click_点击(self.btn_首页, "btn_首页")

    @allure.step(title='点击行程')
    def click_行程(self):
        self.click_点击(self.btn_行程, "btn_行程")

    @allure.step(title='点击玩转车站')
    def click_玩转车站(self):
        self.click_点击(self.btn_玩转车站, "btn_玩转车站")

    @allure.step(title='点击我的')
    def click_我的按钮(self):
        self.click_点击(self.btn_我的, "btn_我的")

    @allure.step(title='点击我的按钮')
    def jde_我的按钮(self):
        return self.judge_元素(5, self.btn_我的)

    @allure.step(title='点击返回按钮')
    def click_返回按钮(self, 返回页面名称):
        self.click_点击(self.btn_返回, "返回按钮")
        logging.info("返回到" + 返回页面名称 + "!")

    @allure.step(title='获取返回按钮元素')
    def jde_返回按钮(self):
        return self.judge_元素(self.btn_返回)

    @allure.step(title='获取返回按钮元素')
    def jde_首页按钮(self):
        return self.judge_元素(self.btn_返回)

    @allure.step(title='点击退出键盘')
    def click_退出键盘(self):
        a = self.get_screenSize()
        x = a[0]-100
        y = a[1]-100
        return TouchAction(self.driver).tap(x=x, y=y).perform()

    @allure.step(title='点击坐标轴')
    def click_点击坐标轴(self, x, y):
        return TouchAction(self.driver).tap(x=x, y=y).perform()

    # @allure.step(title='关闭分享行程')
    # def click_关闭分享行程(self):
    #     time.sleep(5)
    #     a = self.get_screenSize()
    #     x = a[0] * 0.5
    #     y = a[1] * 0.7812
    #     return TouchAction(self.driver).tap(x=x, y=y).perform()

    @allure.step(title='返回到首页')
    def tc_后置回首页(self):
        time.sleep(3)
        for i in range(10):
            j = self.jde_返回按钮()
            if j == 1:
                self.click_返回按钮("后置返回")
            elif j == 0:
                self.click_首页()
                break
        # for i in range(4):
        #     a = self.get_screenSize()
        #     x = a[0] * 0.0333
        #     y = a[1] * 0.1
        #     TouchAction(self.driver).tap(x=x, y=y).perform()
        #     time.sleep(2)
        # self.click_首页()

    @allure.step(title='返回到我的')
    def tc_后置回我的(self):
        for i in range(10):
            j = self.jde_返回按钮()
            if j == 1:
                self.click_返回按钮("后置返回")
            elif j == 0:
                self.click_我的按钮()
                break
        # time.sleep(10)
        # for i in range(4):
        #     a = self.get_screenSize()
        #     x = a[0] * 0.0333
        #     y = a[1] * 0.1
        #     TouchAction(self.driver).tap(x=x, y=y).perform()
        #     time.sleep(1)
        # self.click_我的按钮()

    @allure.step(title='返回到个人中心')
    def tc_后置回个人中心(self):

        for i in range(10):
            j = self.jde_返回按钮()
            if j == 1:
                self.click_返回按钮("后置返回")
            elif j == 0:
                self.click_我的按钮()
                break
        # time.sleep(10)
        # for i in range(4):
        #     a = self.get_screenSize()
        #     x = a[0] * 0.0333
        #     y = a[1] * 0.1
        #     TouchAction(self.driver).tap(x=x, y=y).perform()
        #     time.sleep(1)
        # self.click_我的按钮()

    @allure.step(title='返回到行程页')
    def tc_后置回行程( self ):
        for i in range(10):
            j = self.jde_返回按钮()
            if j == 1:
                self.click_返回按钮("后置返回")
            elif j == 0:
                self.click_行程()
                break

    def scroll_page_one_time( self, direction="up" ):
        """
        滑动一次屏幕
        :param direction: 方向
            "up"：从下往上
            "down"：从上往下
            "right"：从左往右
            "left"：从右往左
        :return:
        """
        width = self.driver.get_window_size()["width"]
        height = self.driver.get_window_size()["height"]

        center_x = width / 2
        center_y = height / 2

        left_x = width / 4 * 1
        left_y = center_y
        right_x = width / 4 * 3
        right_y = center_y

        top_x = center_x
        top_y = height / 4 * 1
        bottom_x = center_x
        bottom_y = height / 4 * 3

        if direction == "up":
            self.driver.swipe(bottom_x, bottom_y, top_x, top_y, 3000)
        elif direction == "down":
            self.driver.swipe(top_x, top_y, bottom_x, bottom_y, 3000)
        elif direction == "left":
            self.driver.swipe(right_x, right_y, left_x, left_y, 3000)
        elif direction == "right":
            self.driver.swipe(left_x, left_y, right_x, right_y, 3000)
        else:
            raise Exception("请检查参数是否正确，up/down/left/right")

    # @allure.step(title='向上滑动')
    def click_loc_with_scroll(self, text ):
        """向上滑动找元素"""
        nums = 0
        while True:
            btn = self.get_toast(text)
            if btn == 0:
                self.act_上滑()
                nums += 1
                if nums == 5:
                    break
            if btn == text:
                self.click_点击(loc_text(text), "点击" + text)
                break

    def find_loc_with_scroll(self, text ):
        """向上滑动找元素"""
        nums = 0
        while True:
            btn = self.get_toast(text)
            if btn == 0:
                self.act_上滑()
                nums += 1
                if nums == 5:
                    break
            else:
                self.click_点击(loc_text(text), "点击" + text)
                break

    def find_text_with_scroll( self, text ):
        page_source = ""
        while True:
            try:
                return loc_contains_text(text)
            except :

                self.act_上滑()

                if self.driver.page_source == page_source:
                    print("到底了")
                    return False
                page_source = self.driver.page_source

    # 获取屏幕尺寸
    def get_screenSize(self):
        x = self.get_窗口尺寸()['width']
        y = self.get_窗口尺寸()['height']
        return x, y

    def touchTapP(self, percentX, percentY, pressTime):
        logging.info("start touch...")
        l = self.get_screenSize()
        x = l[0] * percentX
        y = l[1] * percentY
        tuple = (x, y)
        list = [tuple]
        self.act_点击(list, pressTime)

    def touchTapN(self, list, pressTime):
        logging.info("start touch...")
        self.act_点击(list, pressTime)

    def act_滑动_AtoB(self, 起点元素, 终点元素, infoS,infoE):
        TouchAction(self.driver).press(self.find_元素(起点元素, infoS)).wait(1000).move_to(self.find_元素(终点元素, infoE)).wait(
            1000).release().perform()

    def act_滑动_AtoP(self, 起点元素, x, y, info):
        TouchAction(self.driver).press(self.find_元素(起点元素, info)).wait(1000).move_to(x=x, y=y).wait(
            1000).release().perform()

    def act_滑动_AtoMiddle(self, 起点元素, info):

        l = self.get_screenSize()
        x = int(l[0] * 0.5)
        y = int(l[1] * 0.5)
        logging.info("按住" + info + "移动到中部位置!")
        TouchAction(self.driver).press(self.find_元素(起点元素, info)).wait(1500).move_to(x=x, y=y).wait(
            1500).release().perform()

    @allure.step(title='act_滑动_byYourSelf')
    def act_滑动_byYourSelf(self, 起点元素, x_percent, y_percent, info):
        l = self.get_screenSize()
        x = int(l[0] * x_percent)
        y = int(l[1] * y_percent)
        logging.info("按住" + info + "移动到自定义位置!")
        TouchAction(self.driver).press(self.find_元素(起点元素, info)).wait(1500).move_to(x=x, y=y).wait(
            1500).release().perform()

    @allure.step(title='键盘输入')
    def act_键盘输入(self, number):
        for i in number:
            info = self.click_点击(loc_text("{}".format(i)), "输入{}".format(i))
            if info == 0:
                logging.error("键盘" + i + "找不到!")
        # self.click_退出键盘()

    # 向左滑动
    @allure.step(title='向左滑动')
    def act_左滑(self):
        logging.info('向左滑动屏幕!')
        l = self.get_screenSize()
        x1 = int(l[0] * 0.2)
        x2 = int(l[0] * 0.8)
        y = int(l[1] * 0.5)
        self.act_滑动(x1, y, x2, y, 1)

    # 向右滑动
    @allure.step(title='向右滑动')
    def act_右滑(self):
        logging.info('向右滑动屏幕')
        l = self.get_screenSize()
        x1 = int(l[0] * 0.2)
        x2 = int(l[0] * 0.8)
        y = int(l[1] * 0.5)
        self.act_滑动(x2, y, x1, y, 1)

    # 向上滑动
    @allure.step(title='向上滑动')
    def act_上滑(self, times=1):
        time.sleep(3)
        self.wait_隐式等待(20)
        for i in range(times):
            logging.info('向上滑动屏幕')
            l = self.get_screenSize()
            x = int(l[0] * 0.5)
            y1 = int(l[1] * 0.3)
            y2 = int(l[1] * 0.7)
            self.act_滑动(x, y2, x, y1, 2)

    # 向上滑动
    @allure.step(title='向下滑动')
    def act_下滑(self, times=1):
        time.sleep(2)
        for i in range(times):
            logging.info('向下滑动屏幕')
            l = self.get_screenSize()
            x = int(l[0] * 0.5)
            y1 = int(l[1] * 0.2)
            y2 = int(l[1] * 0.8)
            self.act_滑动(x, y1, x, y2, 1)
        time.sleep(4)


    # 获取Excel数据方法封装
    def getExcelTestData(self, excel_file_path, module_name, row, col):
        with xlrd.open_workbook(excel_file_path, encoding_override='utf-8-sig') as data:
            table = data.sheet_by_name(u'{}'.format(module_name))
            cell_A = str(table.cell(row - 1, col - 1).value)
            test_data = cell_A.split(',')
            return test_data



if __name__ == '__main__':
    # from appiumDriver.desired_caps import appium_微信车站通
    # from time import sleep
    # driver = appium_微信车站通()
    # dr = common(driver)
    # sleep(5)
    # dr.act_上滑()
    # sleep(3)
    # dr.act_上滑()
    a = "asdasd12312"
    b = str(a).upper()
    print(b)
