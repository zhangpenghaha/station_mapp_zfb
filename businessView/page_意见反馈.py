from businessView.page_个人中心 import page_个人中心
from common.loc import *
from time import sleep
import logging
import allure
class page_意见反馈(page_个人中心):

    # btn_意见反馈_优化意见=loc_child_TtoT("wx8d75e764f0c4bf1c:pages/mine/pages/feedback/index.html:VISIBLE","优化意见")
    btn_意见反馈_优化意见 = loc_text("优化建议")
    # btn_意见反馈_服务体验=loc_child_TtoT("wx8d75e764f0c4bf1c:pages/mine/pages/feedback/index.html:VISIBLE","服务体验")
    btn_意见反馈_服务体验 = loc_text("服务体验")
    # btn_意见反馈_问题反馈=loc_child_TtoT("wx8d75e764f0c4bf1c:pages/mine/pages/feedback/index.html:VISIBLE","问题反馈")
    btn_意见反馈_问题反馈 = loc_text('问题反馈')
    # ipb_意见反馈_详细描述=loc_child_IDtoC_Number("com.tencent.mm:id/y","android.widget.EditText",0)
    btn_意见反馈_详细描述 = loc_class_instance("android.widget.EditText", 0)
    # btn_意见反馈_联系方式=loc_child_TtoST("wx8d75e764f0c4bf1c:pages/mine/pages/feedback/index.html:VISIBLE","请输入手机号")
    btn_意见反馈_联系方式 = loc_class_instance("android.widget.EditText", 1)
    btn_提交反馈 = loc_text("提交反馈")
    "操作层"

    @allure.step(title='点击_意见反馈_优化意见')
    def click_意见反馈_优化意见(self):
        self.click_点击(self.btn_意见反馈_优化意见,"btn_优化意见")

    @allure.step(title='点击_意见反馈_服务体验')
    def click_意见反馈_服务体验(self):
        self.click_点击(self.btn_意见反馈_服务体验,"btn_服务体验")

    @allure.step(title='点击_意见反馈_问题反馈')
    def click_意见反馈_问题反馈(self):
        return self.click_点击(self.btn_意见反馈_问题反馈,"btn_问题反馈")

    @allure.step(title='输入_意见反馈_详细描述')
    def send_意见反馈_详细描述(self,详细描述内容):
        self.click_点击(self.btn_意见反馈_详细描述, "btn_详细描述")
        self.clear_清除(self.btn_意见反馈_详细描述,"ipb_详细描述")
        self.send_输入(self.btn_意见反馈_详细描述,"ipb_详细描述",详细描述内容)

    @allure.step(title='输入_意见反馈_联系方式')
    def send_意见反馈_联系方式(self,联系方式内容):
        self.click_点击(self.btn_意见反馈_联系方式,"btn_联系方式")
        sleep(1)
        self.clear_清除(self.btn_意见反馈_联系方式,"ipb_联系方式")
        self.send_输入(self.btn_意见反馈_联系方式,"ipb_联系方式",联系方式内容)

    @allure.step(title='点击_意见反馈_提交反馈')
    def click_意见反馈_提交反馈(self):
        self.click_点击(self.btn_提交反馈,"btn_提交反馈")

    def bus_提交意见反馈(self,意见类型=False,详细描述=False,联系方式=False,提交反馈=True):
        if 意见类型!=False:
            if 意见类型=="优化意见":
                self.click_意见反馈_优化意见()
            elif 意见类型=="服务体验":
                self.click_意见反馈_服务体验()
            elif 意见类型=="问题反馈":
                self.click_意见反馈_问题反馈()
        if 详细描述!=False:
            self.send_意见反馈_详细描述(详细描述)
        if 联系方式!=False:
            self.send_意见反馈_联系方式(联系方式)
        if 提交反馈==True:
            self.click_意见反馈_提交反馈()


if __name__ == '__main__':
    from appiumDriver.desired_caps import appium_微信车站通
    driver=appium_微信车站通()
