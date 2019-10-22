import time
import allure
from businessView.page_添加行程 import page_添加行程
from common.loc import *
from selenium.webdriver.common.by import By
import logging

class Page_选择城市(page_添加行程):

    # btn_城市搜索 = loc_text("中文  /  英文  /  首字母")
    btn_城市搜索 = loc_class("android.widget.EditText")
    @allure.step(title='点击_城市搜索框')
    def click_点击城市搜索框(self):
        self.click_点击(self.btn_城市搜索, "点击城市搜索输入框")

    @allure.step(title='输入_城市信息')
    def send_城市搜索框(self, text):
        self.send_输入(self.btn_城市搜索, "选择城市", text)

    @allure.step(title='选择城市')
    def select_选择城市(self, text):
        self.click_点击(self.btn_城市搜索, "点击城市搜索输入框")
        time.sleep(10)
        self.send_输入(self.btn_城市搜索, "选择城市", text)
        btn_站点 = loc_text("城市")
        self.click_点击(btn_站点, "点击站点")