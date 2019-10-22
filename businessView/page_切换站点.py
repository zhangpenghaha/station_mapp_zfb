from businessView.page_首页 import page_首页
from common.loc import *
from time import sleep
import allure
class page_切换站点(page_首页):

    "定位器"


    "搜索框"
    btn_切换站点焦点=loc_id("com.tencent.mm:id/uv")
    # ipb_切换站点_输入框=loc_child_IDtoC_Number("com.tencent.mm:id/y","android.widget.EditText",0)
    # ipb_切换站点_输入框 = loc_text("中文 / 英文 / 首字母")
    ipb_切换站点_输入框 = loc_class("android.widget.EditText")
    "搜索结果"
    btn_切换站点_第一个结果=loc_child_TtoCT_Number("wx8d75e764f0c4bf1c:pages/station/pages/switchStation/switchStation.html:VISIBLE","站",0)


    "定位站点"
    txt_切换站点_定位站点模块名=loc_text("定位站点")


    "热门站点"
    btn_热门站点长春=loc_child_TtoT("wx8d75e764f0c4bf1c:pages/station/pages/switchStation/switchStation.html:VISIBLE","长春站")

    btn_所在城市站点八大家站=loc_child_ItoC_Number("wx8d75e764f0c4bf1c:pages/station/pages/switchStation/switchStation.html:VISIBLE","android.view.View",9)

    btn__热门站点驻马店站=loc_child_ItoC_Number("wx8d75e764f0c4bf1c:pages/station/pages/switchStation/switchStation.html:VISIBLE","android.view.View",46)


    "ABCDEFG....."


    # WEBVIEW_com.tencent.mm:appbrand0





    "=========================操作层============================="

    "定位站点"

    @allure.step(title='"title_定位站点_模块名')
    def get_切换站点_定位站点模块名(self):
        self.click_切换站点焦点()
        sleep(2)
        self.click_切换站点焦点()
        return self.get_元素文本(self.txt_切换站点_定位站点模块名,"txt_定位站点_模块名")

    @allure.step(title='"点击切换站点第一个结果')
    def click_切换站点_第一个结果(self):
        return self.click_点击(self.btn_切换站点_第一个结果,"btn_第一个结果")

    @allure.step(title='"点击所在城市站点八大家站')
    def click_所在城市八大家站(self):
        return self.click_点击(self.btn_所在城市站点八大家站,"btn_所在城市站点八大家站")

    @allure.step(title='"点击长春站点')
    def click_热门站点长春(self):
        return self.click_点击(self.btn_热门站点长春,"btn_热门站点长春")

    # def click_切换站点焦点(self):
    #     return self.click_点击(self.btn_切换站点焦点,"btn_切换站点焦点")

    @allure.step(title='"点击驻马店站点')
    def click_驻马店站(self):
        return self.click_点击(self.btn__热门站点驻马店站,"btn__热门站点驻马店站")

    @allure.step(title='"点击站点焦点')
    def click_切换站点焦点(self):
        return self.click_点击(self.btn_切换站点焦点, "btn_切换站点焦点")

    @allure.step(title='"点击切换站点输入框')
    def send_站点城市(self,cityStation):
        self.click_点击(self.ipb_切换站点_输入框,"ipb_切换站点_输入框")
        # print(self.click_点击(self.ipb_切换站点_输入框,"ipb_切换站点_输入框"))
        # sleep(4)
        return self.send_输入(self.ipb_切换站点_输入框,"ipb_切换站点_输入框",cityStation)


    "==================================业务层===================================="
    def bus_切换站点_切换到指定站点(self,cityStation):
        # self.wait_显式等待(20,self.btn_切换站点焦点)
        # self.click_切换站点焦点()
        sleep(5)
        self.send_站点城市(cityStation)
        sleep(2)
        self.click_点击(loc_text(cityStation+"站"),"点击获取搜索结果")




if __name__ == '__main__':
    #Chrome/66.0.3359.126
    from appiumDriver.desired_caps import appium_微信车站通
    driver=appium_微信车站通()
    dr=page_切换站点(driver)
    dr.click_首页_切换站点提示按钮()
    dr.click_首页_切换站点按钮()
    dr.bus_切换站点_切换到指定站点("浠水站")
