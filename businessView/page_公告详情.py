from businessView.page_首页 import page_首页
from common.loc import *
import allure

class page_公告详情(page_首页):

    "定位器"

    title_公告详情=loc_id("com.tencent.mm:id/ph")

    "操作层"

    @allure.step(title='"title_公告详情')
    def get_公告详情_标题(self):
        return self.get_元素文本(self.title_公告详情,"title_公告详情")


