from selenium.webdriver.common.by import By
from businessView.page_首页 import page_首页
import logging
import allure
from selenium.webdriver.common.by import By
from businessView.page_首页 import page_首页
import logging

from common.loc import *


class page_余票查询(page_首页):
    "!!!!!!!!!!!!!!!!!!!定位器!!!!!!!!!!!!!!!!!!!!!!!"

    "!!!!按钮定位器!!!!"
    # btn_查询 = (By.XPATH, '//*[@text="查询"]')
    #
    # btn_出发地 = (By.XPATH, '//*[@text="出发地"]')
    # # btn_出发地列表 = (By.XPATH, '//*[@bounds="[138,432][276,525]"]')
    #
    # btn_目的地 = (By.XPATH, '//*[@text="目的地"]')
    #
    # btn_切换地点 = (By.XPATH, '//*[@bounds="[480,373][597,490]"]')
    btn_出发地 = loc_text("出发地")

    btn_目的地 = loc_text("目的地")

    btn_查询 = loc_text("查询")
    "!!!!文本定位器!!!!"

    # text_今天 = (By.XPATH, '//*[@text="今天"]')

    btn_选择日期 = loc_text("出发日期")




    "!!!!操作层!!!!"

    @allure.step(title='点击_出发地')
    def click_出发地(self):
        logging.info("点击出发地,进入出发地搜索列表!")
        self.click_点击(self.btn_出发地, "点击出发地")
        # logging.info("进入出发地搜索列表!")

    @allure.step(title='点击_目的地')
    def click_目的地(self):
        logging.info("点击目的地,进入目的地搜索列表!")
        self.click_点击(self.btn_目的地, "点击目的地")
        # logging.info("进入出发地搜索列表!")

    @allure.step(title='点击_余票查询')
    def click_余票查询_查询(self):
        logging.info("点击_余票查询_查询")
        self.click_点击(self.btn_查询, "点击余票查询")

    @allure.step(title='点击_出发日期')
    def click_点击出发日期(self):
        logging.info("点击_余票查询_出发日期")
        self.click_点击(self.btn_选择日期, "点击日期")

    "!!!!!!!!校验层!!!!!!!"
    def check_余票查询页面跳转(self):
        logging.info("检查余票查询页面跳转,检查\"查询按钮\"是否存在!")
        try:
            self.wait_显式等待(3, *self.btn_查询)
        except:
            logging.error("余票查询页面跳转失败!")
            self.fun_截图("余票查询页面!")
            return 0
        else:
            logging.info("余票查询页面跳转成功!")
            return 1



if __name__ == '__main__':
    from appiumDriver.desired_caps import appium_微信车站通

    driver = appium_微信车站通()
    dr = page_余票查询(driver)
    dr.click_余票查询()
    t = dr.check_余票查询页面跳转()
    print(t)



# class page_余票查询(page_首页):
#     "!!!!!!!!!!!!!!!!!!!定位器!!!!!!!!!!!!!!!!!!!!!!!"
#
#     "!!!!按钮定位器!!!!"
#     btn_查询 = (By.XPATH, '//*[@text="查询"]')
#
#     btn_出发地列表 = (By.XPATH, '//*[@text="出发地"]')
#     # btn_出发地列表 = (By.XPATH, '//*[@bounds="[138,432][276,525]"]')
#
#     btn_目的地列表 = (By.XPATH, '//*[@text="目的地"]')
#
#     btn_切换地点 = (By.XPATH, '//*[@bounds="[480,373][597,490]"]')
#
#
#     "!!!!文本定位器!!!!"
#
#     text_今天 = (By.XPATH, '//*[@text="今天"]')
#
#
#
#
#
#
#     "!!!!操作层!!!!"
#
#     @allure.step(title='点击_出发地')
#     def click_出发地(self):
#         logging.info("点击出发地,进入出发地搜索列表!")
#         self.find_元素(*self.btn_出发地列表).click()
#         logging.info("进入出发地搜索列表!")
#
#
#
#
#
#
#
#     "!!!!!!!!校验层!!!!!!!"
#
#     @allure.step(title='"检查余票查询页面跳转,检查\"查询按钮\"是否存在!')
#     def check_余票查询页面跳转(self):
#         logging.info("检查余票查询页面跳转,检查\"查询按钮\"是否存在!")
#         try:
#             self.wait_显式等待(3, *self.btn_查询)
#         except:
#             logging.error("余票查询页面跳转失败!")
#             self.fun_截图("余票查询页面!")
#             return 0
#         else:
#             logging.info("余票查询页面跳转成功!")
#             return 1
#
#
#
# if __name__ == '__main__':
#     from appiumDriver.desired_caps import appium_微信车站通
#
#     driver = appium_微信车站通()
#     dr = page_余票查询(driver)
#     dr.click_余票查询()
#     t = dr.check_余票查询页面跳转()
#     print(t)
#
#
