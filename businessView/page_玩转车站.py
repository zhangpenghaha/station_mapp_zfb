from common.common import common
from common.loc import *
import allure


class page_玩转车站(common):


    btn_探索附近=loc_id("toQuickPage")

    btn_附近洗手间=loc_text_instance("洗手间",2)
    btn_附近检票口=loc_text_instance("检票口",1)

    btn_关闭结果按钮=loc_child_ItoC_Number("floorSelect","android.view.View",2)

    btn_玩转车站_实时共享=loc_child_IDtoT("app","实时共享")

    @allure.step(title='获取_玩转车站_实时共享文本')
    def get_玩转车站_实时共享(self):
        return self.get_元素文本(self.btn_玩转车站_实时共享,"btn_玩转车站_实时共享")

    @allure.step(title='点击探索附近')
    def click_探索附近(self):
        return self.click_点击(self.btn_探索附近,"btn_搜索附近")

    @allure.step(title='点击附近洗手间')
    def click_附近洗手间(self):
        return self.click_点击(self.btn_附近洗手间,"btn_附近洗手间")

    @allure.step(title='点击附近检票口')
    def click_附近检票口(self):
        return self.click_点击(self.btn_附近检票口,"btn_附近检票口")

    @allure.step(title='点击关闭结果按钮')
    def click_关闭结果按钮(self):
        return self.click_点击(self.btn_关闭结果按钮,"关闭结果按钮")



if __name__ == '__main__':
    from appiumDriver.desired_caps import appium_微信车站通_tmp
    from businessView.page_切换站点 import page_切换站点
    driver=appium_微信车站通_tmp()
    dr=page_切换站点(driver)
    dr.click_切换站点()
    dr.click_切换站点焦点()
    dr.send_站点城市("长春站")
    dr.click_第一个结果()
    dr=page_玩转车站(driver)

    dr.click_玩转车站()
    dr.click_探索附近()
    for i in range(100):
        dr.click_附近洗手间()
        dr.click_关闭结果按钮()
        print(i)