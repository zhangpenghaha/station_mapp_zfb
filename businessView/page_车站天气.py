from selenium.webdriver.common.by import By
from businessView.page_首页 import page_首页
import logging
from common.loc import *
from selenium.common.exceptions import NoSuchElementException
import allure

class page_车站天气(page_首页):
    "定位器!!!!!!!!!!!!!!!!!!!!!!!"

    "车站天气title"

    @allure.step(title='获取车站天气标题文本')
    def get_车站天气_标题(self):
        return self.get_元素文本(self.txt_title, "get_车站天气_标题")

    "文本定位器!"
    text_今天 = (By.XPATH, '//*[@text="今天"]')

    @allure.step(title='检查天气页面跳转')
    def check_天气页面跳转(self):
        logging.info("检查天气页面跳转,检查\"今天\"这问文本信息!是否存在")
        try:
            self.wait_显式等待(3, *self.text_今天)
        except NoSuchElementException:
            logging.error("天气页面跳转失败!")
            self.fun_截图("天气页面!")
            return 0
        else:
            logging.info("天气页面跳转成功!")
            return 1


if __name__ == '__main__':
    from appiumDriver.desired_caps import appium_微信车站通

    driver = appium_微信车站通()
    dr = page_车站天气(driver)
    dr.click_天气图标()
    t = dr.check_天气页面跳转()
    print(t)
