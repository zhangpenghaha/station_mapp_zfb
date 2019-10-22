from businessView.page_首页 import page_首页
from common.loc import *
import allure


class page_首页底部服务页面(page_首页):

    txt_军人优先_文章标题=loc_text("【军人优先】风里雨里你在前，铁路出行你优先")
    def get_军人优先_文章标题(self):
        return self.get_元素文本(self.txt_军人优先_文章标题,"txt_军人优先_文章标题")


    txt_服务评价_文章标题=loc_text("【服务评价】欢迎您对铁路出行服务进行评价！")
    def get_服务评价_文章标题(self):
        return self.get_元素文本(self.txt_服务评价_文章标题,"txt_服务评价_文章标题")


    txt_常见问题_文章标题=loc_text("出行常见问题之火车票相关")
    def get_常见问题_文章标题(self):
        return self.get_元素文本(self.txt_常见问题_文章标题,"txt_常见问题_文章标题")


    txt_关于我们_文章标题=loc_text("威泰科技")
    def get_关于我们_文章标题(self):
        return self.get_元素文本(self.txt_关于我们_文章标题,"关于我们_文章标题")