from common.loc import *
from businessView.page_余票查询 import page_余票查询
from selenium.webdriver.common.by import By
import logging
import allure

class page_城市搜索(page_余票查询):

    "!!!!定位器!!!"

    "所在城市站点"
    atCity=loc_text("所在城市站点")
    ListView=loc_text("可上下滚动")
    classView=loc_text("八大家站")
    son2=loc_child_ele(ListView,classView)

    btn_八大家站=(By.XPATH,'//*[@bounds=""]')

    @allure.step(title='点击所在城市站点')
    def click_所在城市站点(self):
        self.click_点击(self.btn_八大家站,"btn_八大家站")



    "操作层!"

    def wait_text_所在城市站点(self):
        self.wait_显式等待(20,self.atCity)

    @allure.step(title='获取热门城市名称')
    def get_热门城市1_1(self):
        logging.info("获取热门城市1_1名称!")
        t = self.find_元素(*self.btn_热门城市1_1).text
        print(t)
        logging.info(t)
        return t

    @allure.step(title='点击城市输入框')
    def click_城市输入框(self):
        logging.info("点击搜索输入框!")
        self.find_元素(*self.btn_搜索输入框).click()

    @allure.step(title='输入城市信息')
    def send_keys_城市输入框(self,城市检索信息):
        logging.info("在城市搜索输入框输入{}".format(城市检索信息))
        self.find_元素(*self.ipb_搜索输入框).send_keys(城市检索信息)

    @allure.step(title='点击城市输入框_输入城市信息')
    def bus_城市搜索输入框(self, 城市检索信息):
        self.click_城市输入框()
        self.send_keys_城市输入框(城市检索信息)
        logging.info("搜索城市信息:{}!".format(城市检索信息))

    @allure.step(title='获取第一个按钮文本')
    def get_第一个按钮文本(self):
        logging.info("获取第一个按钮的文本信息!")
        t = self.find_元素(*self.btn_城市列表第一个).text
        logging.info("第一个按钮的文本信息为:{}".format(t))
        logging.info("清空输入框信息!")
        self.find_元素(*self.ipb_搜索输入框).clear()
        return t

    @allure.step(title='点击热门城市')
    def check_热门城市1_1(self,实际结果,预期结果,模块名):
        if 实际结果 != 预期结果:
            self.fun_截图(模块名)
        else:
            pass


if __name__ == '__main__':
    from appiumDriver.desired_caps import appium_微信车站通
    driver = appium_微信车站通()
    dr = page_城市搜索(driver)
    dr.click_切换站点()
    dr.wait_text_所在城市站点()
    dr.click_所在城市站点()

