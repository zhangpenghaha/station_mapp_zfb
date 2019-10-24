from businessView.page_首页 import page_首页
from common.loc import *
import allure

class page_站内商业(page_首页):


    "===========定位层==========="

    "大图"
    # image_站内商业_大图=loc_id("intoT")
    image_站内商业_大图 = loc_id("intoM1")

    "站内商业赛选按钮"

    btn_站内商业_所有楼层 = loc_id("ATshop2")
    btn_站内商业_全部分类 = loc_id("ATshop3")
    btn_站内商业_智能排序 = loc_id("ATshop4")
    btn_站内商业_进站前后 = loc_id("ATshop5")


    "站内商业赛选按钮,展开后"
    btn_站内商业_筛选展开_1=loc_child_IDtoC_Number("screen","android.view.View",14)
    btn_站内商业_所有楼层_B1 = loc_text("B1")
    # btn_站内商业_筛选展开_2=loc_child_IDtoC_Number("screen","android.view.View",15)
    btn_站内商业_筛选展开_2 = loc_text("进站前")

    # btn_站内商业_筛选展开_3=loc_child_IDtoC_Number("screen","android.view.View",16)
    btn_站内商业_进站前后 = loc_text("进站后")

    # btn_站内商业_筛选展开_4=loc_child_IDtoC_Number("screen","android.view.View",17)
    btn_站内商业_筛选展开_4 = loc_text("美食")
    # btn_站内商业_筛选展开_5=loc_child_IDtoC_Number("screen","android.view.View",18)
    btn_站内商业_筛选展开_5 = loc_text("娱乐休闲")
    btn_站内商业_筛选展开_6=loc_child_IDtoC_Number("screen","android.view.View",19)

    # btn_站内商业_筛选展开_美食=loc_child_IDtoC_Number("screen","android.view.View",17)
    btn_站内商业_筛选展开_美食 = loc_text("美食")

    btn_站内商业_筛选展开_百货超市 = loc_text("百货超市")
    "店铺列表"

    btn_站内商业_店铺列表_便民超市 = loc_text("便民超市")

    btn_站内商业_店铺列表_平价自选商店 = loc_text("平价自选商店")
    "提示"
    tip_站内商业_无搜索结果=loc_text("暂无相关商家")

    @allure.step(title='获取站内商业_大图文本')
    def get_站内商业_大图(self):
        return self.get_元素文本(self.image_站内商业_大图,"image_站内商业_大图")

    @allure.step(title='点击站内商业_所有楼层')
    def click_站内商业_所有楼层(self):
        return self.click_点击(self.btn_站内商业_所有楼层,"btn_站内商业_所有楼层")

    @allure.step(title='点击站内商业_全部分类')
    def click_站内商业_全部分类(self):
        return self.click_点击(self.btn_站内商业_全部分类,"btn_站内商业_全部分类")

    @allure.step(title='点击_站内商业_智能排序')
    def click_站内商业_智能排序(self):
        return self.click_点击(self.btn_站内商业_智能排序,"btn_站内商业_智能排序")

    @allure.step(title='获取站内商业_智能排序文本')
    def get_站内商业_智能排序(self):
        return self.get_元素文本(self.btn_站内商业_智能排序,"btn_站内商业_智能排序")

    @allure.step(title='点击站内商业_进站前后')
    def click_站内商业_进站前后(self):
        return self.click_点击(self.btn_站内商业_进站前后,"btn_站内商业_进站前后")

    @allure.step(title='点击站内商业_筛选展开1')
    def click_站内商业_筛选展开1(self):
        return self.click_点击(self.btn_站内商业_筛选展开_1,"btn_站内商业_筛选展开_1")

    @allure.step(title='获取站内商业_筛选展开1文本')
    def get_站内商业_筛选展开1(self):
        return self.get_元素文本(self.btn_站内商业_筛选展开_1,"btn_站内商业_筛选展开_1",2)

    @allure.step(title='点击站内商业_筛选展开2')
    def click_站内商业_筛选展开2(self):
        return self.click_点击(self.btn_站内商业_筛选展开_2,"btn_站内商业_筛选展开_2")

    @allure.step(title='获取站内商业_筛选展开2_文本')
    def get_站内商业_筛选展开2(self):
        return self.get_元素文本(self.btn_站内商业_筛选展开_2,"btn_站内商业_筛选展开_2",2)

    @allure.step(title='btn_站内商业_所有楼层_B1')
    def click_站内商业_筛选展开3(self):
        return self.click_点击(self.btn_站内商业_所有楼层_B1,"btn_站内商业_所有楼层_B1")

    @allure.step(title='获取站内商业_筛选展开3_文本')
    def get_站内商业_筛选展开3(self):
        return self.get_元素文本(self.btn_站内商业_筛选展开_3,"btn_站内商业_筛选展开_3",2)

    "针对全部分类赛选展开的组件结构不一样如下"
    "展开后的第二项"

    @allure.step(title='点击站内商业_筛选展开4')
    def click_站内商业_筛选展开4(self):
        return self.click_点击(self.btn_站内商业_筛选展开_4,"btn_站内商业_筛选展开_4")

    @allure.step(title='获取站内商业_筛选展开4文本')
    def get_站内商业_筛选展开4(self):
        return self.get_元素文本(self.btn_站内商业_筛选展开_4,"btn_站内商业_筛选展开_4",2)
    "展开后的第三项"

    @allure.step(title='点击站内商业_筛选展开5')
    def click_站内商业_筛选展开5(self):
        return self.click_点击(self.btn_站内商业_筛选展开_5,"btn_站内商业_筛选展开_5")

    @allure.step(title='获取站内商业_筛选展开5文本')
    def get_站内商业_筛选展开5(self):
        return self.get_元素文本(self.btn_站内商业_筛选展开_5,"btn_站内商业_筛选展开_5",2)
    "展开后的第四项"

    @allure.step(title='点击站内商业_筛选展开3')
    def click_站内商业_筛选展开6(self):
        return self.click_点击(self.btn_站内商业_筛选展开_6,"btn_站内商业_筛选展开_6")

    @allure.step(title='获取站内商业_筛选展开6文本')
    def get_站内商业_筛选展开6(self):
        return self.get_元素文本(self.btn_站内商业_筛选展开_6,"btn_站内商业_筛选展开_6",2)


    "展开项目"

    @allure.step(title='点击站内商业_筛选展开_美食')
    def click_站内商业_展开筛选_美食(self):
        return self.click_点击(self.btn_站内商业_筛选展开_美食,"btn_站内商业_筛选展开_美食")

    @allure.step(title='获取站内商业_筛选展开_美食文本')
    def get_站内商业_展开筛选_美食(self):
        return self.get_元素文本(self.btn_站内商业_筛选展开_美食,"btn_站内商业_筛选展开_美食",2)

    @allure.step(title='点击站内商业_筛选展开_百货超市')
    def click_站内商业_展开筛选_百货超市(self):
        return self.click_点击(self.btn_站内商业_筛选展开_百货超市,"btn_站内商业_筛选展开_百货超市")

    @allure.step(title='获取站内商业_筛选展开_百货超市文本')
    def get_站内商业_展开筛选_百货超市(self):
        return self.get_元素文本(self.btn_站内商业_筛选展开_百货超市,"btn_站内商业_筛选展开_百货超市",2)

    "=========店铺列表========="

    @allure.step(title='点击站内商业_店铺列表_便民超市')
    def click_站内商业_店铺列表_便民超市(self):
        return self.click_点击(self.btn_站内商业_店铺列表_便民超市,"btn_站内商业_店铺列表_便民超市")

    @allure.step(title='获取站内商业_店铺列表_便民超市文本')
    def get_站内商业_店铺列表_便民超市(self):
        return self.get_元素文本(self.btn_站内商业_店铺列表_便民超市,"btn_站内商业_店铺列表_便民超市",3)

    @allure.step(title='点击站内商业_店铺列表_评价自选超市')
    def click_站内商业_店铺列表_平价自选商店(self):
        return self.click_点击(self.btn_站内商业_店铺列表_平价自选商店,"btn_站内商业_店铺列表_平价自选商店")

    @allure.step(title='获取站内商业_店铺列表_平价自选超市')
    def get_站内商业_店铺列表_平价自选商店(self):
        return self.get_元素文本(self.btn_站内商业_店铺列表_平价自选商店,"btn_站内商业_店铺列表_平价自选商店",3)

    "=======提示======"

    @allure.step(title='获取站内商业_无搜索结果提示')
    def get_站内商业_无搜索结果提示(self):
        return self.get_元素文本(self.tip_站内商业_无搜索结果,"tip_站内商业_无搜索结果")



if __name__ == '__main__':
    from appiumDriver.desired_caps import appium_微信车站通
    from businessView.page_切换站点 import page_切换站点
    driver=appium_微信车站通()
    dr=page_切换站点(driver)
    dr.click_首页_切换站点按钮()
    dr.bus_切换站点_切换到指定站点("浠水站")
    dr.act_上滑(3)
    dr.click_首页_车站商业查看全部()
    dr=page_站内商业(driver)
    dr.click_站内商业_进站前后()