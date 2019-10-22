from businessView.page_个人中心 import page_个人中心
from common.loc import *
import allure
class page_我的积分(page_个人中心):

    text_做任务领积分=loc_text("做任务领积分")

    @allure.step(title='点击_意见反馈_优化意见')
    def get_做任务领积分(self):
        return self.get_元素文本(self.text_做任务领积分,"text_做任务领积分")