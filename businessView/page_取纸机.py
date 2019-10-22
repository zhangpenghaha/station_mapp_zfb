from businessView.page_首页 import page_首页
from selenium.webdriver.common.by import By
import logging
from time import sleep
import allure
class page_取纸机(page_首页):
    "!!!!定位器!!!!"

    "按钮定位器"
    btn_热线 = (By.XPATH, "//*[@bounds='[0,1984][1080,2060]']")

    "文本定位器"
    txt_设施位置 = (By.XPATH, '//*[@text="设施位置"]')

    "!!!操作层!!!!"

    def wait_取纸机(self):
        logging.info("等待页面加载\"设施位置\"")
        self.wait_显式等待(10,*self.txt_设施位置)

    @allure.step(title='"点击求助热线电话')
    def click_热线(self):
        self.act_上滑()
        logging.info("点击求助热线的电话!")
        p = self.find_元素(*self.btn_热线).text
        logging.info("求助热线电话为:"+p)
        self.find_元素(*self.btn_热线).click()
        return p




if __name__ == '__main__':
    from appiumDriver.desired_caps import appium_微信车站通
    from time import sleep
    driver= appium_微信车站通()
    dr = page_取纸机(driver)

    for i in range(2):
        sleep(2)
        dr.act_上滑()
    dr.click_取纸机()
    sleep(3)
    dr.act_上滑()
    a = dr.click_热线()
    e = dr.check_热线()
    print(a ,e)