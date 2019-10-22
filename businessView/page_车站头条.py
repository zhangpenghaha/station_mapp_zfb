from businessView.page_首页 import page_首页
from common.loc import *
import allure

class page_车站头条(page_首页):

    "定位层"

    "页面标题"

    txt_车站头条_标题=loc_id("com.tencent.mm:id/pg")

    "tab标签页"
    btn_车站头条_车站资讯=loc_text("车站资讯")

    "操作层"

    @allure.step(title='获取_车站头条_标题文本')
    def get_车站头条_标题(self):
        return self.get_元素文本(self.txt_车站头条_标题,"txt_车站头条_标题")

    @allure.step(title='获取_车站头条_车站咨询文本')
    def get_车站头条_车站资讯(self):
        return self.get_元素文本(self.btn_车站头条_车站资讯,"btn_车站头条_车站资讯")

