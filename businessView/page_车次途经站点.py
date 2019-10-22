from common.loc import *
from businessView.page_选择车次出发和到达 import page_选择车次出发和到达
import allure

class page_车次途经站点(page_选择车次出发和到达):

    btn_车次途经站点_确认添加 = loc_text('确定添加')

    @allure.step(title='点击_途经站点_确认添加')
    def click_车次途经站点_确认添加(self):
        self.click_点击(self.btn_车次途经站点_确认添加,'btn_车次途经站点_确认添加')