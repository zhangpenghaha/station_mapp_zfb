from common.loc import *
from businessView.page_首页 import page_首页
import allure

class page_店铺详情(page_首页):

    btn_店铺详情_评论此商家=loc_text("评论此商家")

    @allure.step(title='点击_店铺详情_[评论此商家')
    def click_店铺详情_评论此商家(self):
        return self.click_点击(self.btn_店铺详情_评论此商家,"btn_店铺详情_评论此商家")

    @allure.step(title='获取_填写评论_商家评论文本')
    def get_店铺详情_评论此商家(self):
        return self.get_元素文本(self.btn_店铺详情_评论此商家,"btn_店铺详情_评论此商家")


if __name__ == '__main__':
    from appiumDriver.desired_caps import appium_微信车站通
    driver=appium_微信车站通()
    dr = page_店铺详情(driver)
    dr.act_上滑(2)
    dr.click_小胡鸭()
    dr.click_评论此商家()