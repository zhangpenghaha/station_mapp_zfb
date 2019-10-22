from common.common import Common
from selenium.webdriver.common.by import By
import allure
import logging




class page_我的(Common):


    "文案"
    info_登录状态操作提示 = "点击登录~"


    "定位器!!!"


    "头像按钮"
    btn_头像 = (By.ID, 'com.whwfsf.wisdomstation:id/iv_user_icon_default')

    "每日签到按钮"
    btn_每日签到 = (By.ID, 'com.whwfsf.wisdomstation:id/tv_sign_in')


    "登录状态信息"
    text_登录状态操作提示 = (By.ID, 'com.whwfsf.wisdomstation:id/tv_user_tips_lv')

    @allure.step(title='获取登录状态信息')
    def get_登录状态信息(self):
        logging.info("获取登录状态信息!")
        try:
            mes_登录状态信息 = self.find_element(*self.text_登录状态操作提示).text
        except:
            logging.info("已登录状态!")
            return False
        else:
            logging.info("登录状态信息为:"+"\""+mes_登录状态信息+"\"")
            return mes_登录状态信息

    @allure.step(title='点击头像')
    def click_头像(self):
        messge = self.get_登录状态信息()
        if messge == self.info_登录状态操作提示:
            logging.info("未登录状态,点击头像进入登录注册页面!")
            self.find_element(*self.btn_头像).click()
            logging.info("进入登录注册页面!")
        else:
            logging.info("已登录状态,点击头像进入个人中心页面!")
            self.find_element(*self.btn_头像).click()
            logging.info("进入个人中心页面!")

