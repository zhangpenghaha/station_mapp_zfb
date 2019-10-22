from businessView.page_首页 import page_首页
from common.loc import *
from function.tools import *
from function.funcdate import *
import logging
import allure
class page_选择日期(page_首页):

    "页面标题"

    txt_选择日期_标题=loc_id("com.tencent.mm:id/pg")

    day = tools_选择日期()

    "第一个月标题"
    date_选择日期_当前年月=get_当前年月()
    txt_选择日期_当前年月=loc_text(date_选择日期_当前年月)

    btn_加60天_try1 = loc_text_instance(day, 0)
    btn_加60天_try2 = loc_text_instance(day, 1)

    @allure.step(title='获取当前日期')
    def get_选择日期_当前年月(self):
        return self.get_元素文本(self.txt_选择日期_当前年月,"txt_选择日期_当前年月")

    @allure.step(title='获取选择日期页面标题')
    def get_选择日期页面标题(self):
        return self.get_元素文本(self.txt_选择日期_标题,"txt_选择日期_标题")

    @allure.step(title='选择当前日期加60天')
    def click_当前日期加60天(self):
        self.act_上滑()
        if self.judge_元素(8, self.btn_加60天_try2)==1:
            return self.click_点击(self.btn_加60天_try2, "btn_加60天_try2")
        elif self.judge_元素(8, self.btn_加60天_try1)==1:
            return self.click_点击(self.btn_加60天_try1, "btn_加60天_try1")
        else:
            return 0

    @allure.step(title='选择日期')
    def get_选择日期(self, text):
        listdate = get_当前日期加指定日(text).split("-")
        if int(listdate[1]) < 10:
            months = listdate[1][1]
        else:
            months = listdate[1]
        if int(listdate[2]) < 10:
            days = listdate[2][1]
        else:
            days = listdate[2]
        targetdate = get_当前日期加指定日(60, format=False)
        weekday = get_指定日期星期(targetdate)
        logging.info(weekday)
        monthdaydate = months + "月" + days + "日"
        logging.info(monthdaydate)
        return monthdaydate,days

    @allure.step(title='选择几天后的日期')
    def click_选择几天后日期(self,num):
        monthday, days = self.get_选择日期(num)
        btn_选择日期 = loc_text(days)
        self.click_点击(btn_选择日期, "选择日期")


if __name__ == '__main__':
    listdate=get_当前日期加指定日(2).split("-")
    if  int(listdate[1])<10:
        months=listdate[1][1]
    else:
        months=listdate[1]
    if int(listdate[2])<10:
        days=listdate[2][1]
    else:
        days=listdate[2]
    targetdate = get_当前日期加指定日(60,format=False)
    weekday = get_指定日期星期(targetdate)
    monthdaydate = months+"月"+days+"日"
    print(monthdaydate, days)