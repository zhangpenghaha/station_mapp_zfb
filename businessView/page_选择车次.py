from businessView.page_车次详情 import page_车次详情
from common.loc import *
from businessView.page_首页 import page_首页
import allure


class page_选择车次(page_首页):
    # 站站查询选择车次

    title_选择车次=loc_text("选择车次")
    date_日期=loc_id("ATfind1")
    img_高铁动车=loc_text("高铁动车")
    text_共XX车次=loc_child_IDtoC_Number("ATfind3","android.view.View",2)
    text_武汉到北京=loc_text("武汉-北京")
    img_日历icon = loc_child_TtoC_Number("wx8d75e764f0c4bf1c:pages/station/pages/findStation/findStation.html:VISIBLE",
                                     "android.widget.Image", 0)

    text_所有车次 = loc_id("ATfind4")
    text_第一列车次 = loc_id("ATfind5_0")
    text_选择日期=loc_text("选择日期")
    text_点击日期 = loc_child_TtoC_Number("wx8d75e764f0c4bf1c:pages/station/pages/calendar/calendar.html:VISIBLE","android.view.View",24)

    text_底线 = loc_text("— 我也是有底线的 —")

    txt_选择车次_出发地_目的地 = loc_text("武汉")
    # txt_选择车次_出发地_目的地=loc_child_TtoC_Number("wx8d75e764f0c4bf1c:pages/station/pages/findStation/findStation.html:VISIBLE","android.view.View",4)
    #结果页

    # text_结果页=loc_text("K600 武昌-北京西")
    text_到达正点率=loc_text("到达正点率")
    text_正点率=loc_text("正点率")
    text_展开=loc_text("展开")
    text_收起 =loc_text("收起")
    text_前序站=loc_text("7个前序站")
    text_后序站 = loc_text("7个后序站")
    text_添加行程文案 = loc_text("添加行程，列车动态实时提醒")
    text_确定添加 = loc_text("确定添加")

    #行程详情页面
    text_全程预计剩余=loc_text("全程预计剩余")

    @allure.step(title='获取选择车次_出发地_目的地文本')
    def get_选择车次_出发地_目的地(self):
        return self.get_元素文本(self.txt_选择车次_出发地_目的地,"txt_选择车次_出发地_目的地")

    @allure.step(title='获取选择车次文本')
    def get_选择车次(self):
        return self.get_元素文本(self.title_选择车次,"title_选择车次")

    def check_文案检查(self,text):
        return self.get_元素文本(loc_text(text), "检查文案")

    @allure.step(title='获取当前日期文本')
    def get_当前日期(self):
        return self.get_元素文本(self.date_日期,"date_日期")

    @allure.step(title='勾选高铁动车按钮')
    def click_勾选高铁动车(self, TrainNo):
        self.click_点击(self.img_高铁动车, 'img_高铁动车')
        a = self.get_toast(loc_text(TrainNo))
        self.click_点击(self.img_高铁动车, 'img_高铁动车')
        return a

    @allure.step(title='获取武汉到北京文本')
    def text_武汉到北京文案(self):
        return self.get_元素文本(self.text_武汉到北京,"text_武汉到北京")

    @allure.step(title='点击_日历')
    def click_日历icon(self):
        self.click_点击(self.img_日历icon,"img_日历icon")
        return self.get_元素文本(self.text_选择日期,"text_选择日期")

    @allure.step(title='点击_今天')
    def click_今天(self):
        self.click_点击(self.text_点击日期,"text_点击日期")
        return self.get_元素文本(self.date_日期,"date_日期")


#######################################################################################
    @allure.step(title='点击_车次')
    def click_点击车次(self, text):
        text_车次 = loc_contains_text(text)
        return self.click_点击(text_车次,"text_车次")
        # text_结果页 = loc_text(text)
        # return self.get_元素文本(text_结果页,"text_结果页")
        # self.click_loc_with_scroll(text)
#######################################################################################
        # 结果页
    @allure.step(title='点击_到达正点率')
    def click_到达正点率(self):
        self.click_点击(self.text_到达正点率,"text_到达正点率")
        return self.get_元素文本(self.text_正点率,"text_正点率")

    @allure.step(title='点击_展开')
    def click_展开(self):
        self.click_点击(self.text_展开,"text_展开")
        return self.get_元素文本(self.text_收起,"text_收起")

    @allure.step(title='点击_前序站')
    def get_前序站(self):
        return self.get_元素文本(self.text_前序站,"text_前序站")

    @allure.step(title='点击_后序站')
    def get_后序站(self):
        # self.act_上滑()
        return self.get_元素文本(self.text_后序站,"text_后序站")

    @allure.step(title='获取添加行程文本')
    def get_添加行程文案(self):
        return self.get_元素文本(self.text_添加行程文案, "text_添加行程文案")

    @allure.step(title='点击_确认添加')
    def click_确定添加(self):
        self.click_点击(self.text_确定添加, "text_确定添加")
        return self.get_toast("行李托运")

    @allure.step(title='检查选择车次结果页文案')
    def check_选择车次结果页文案(self):
        a0 = []
        a1 = ["到达正点率", "站名", "到站", "停留", "出发", "状态", "到站", "7个前序站", "7个后序站", "北京西 车次变更为K597", "添加行程，列车动态实时提醒"]
        for i in a1:
            text = self.get_toast(i)
            a0.append(text)
        return a0

    def get_总共多少趟(self):
        return self.get_元素文本(self.text_共XX车次)


if __name__ =="__main__":

    from appiumDriver.desired_caps import appium_微信车站通
    from function.funcdate import get_当前月日, get_获取当前星期
    driver=appium_微信车站通()
    dr=page_首页(driver)
    dr.act_下滑(3)
    dr.act_滑动_byYourSelf(dr.txt_首页_时刻查询模块名, 0.5, 0.15, "txt_首页_时刻查询模块名移动到0.15位置")
    dr.click_首页_站站查询()
    dr.click_首页_时刻查询_查询()
    dr = page_选择车次(driver)
    a = dr.get_总共多少趟()
    num = str(a)[1]+ str(a)[2]
    print(num)
    # "ATfind5_0"
    b ="ATfind5_" + str(int(num)-1)
    last_train = loc_id(b)
    dr.click_点击(last_train)




