from businessView.page_首页 import page_首页
from common.loc import *
import allure


class page_车站流量(page_首页):

    btn_车站流量_旅客流量=loc_child_TtoT("wx8d75e764f0c4bf1c:pages/station/pages/stationInfo/stationInfo.html:VISIBLE","旅客流量")
    txt_车站流量_旅客流量=loc_child_TtoT("wx8d75e764f0c4bf1c:pages/station/pages/stationInfo/stationInfo.html:VISIBLE","旅客流量")
    txt_车站流量_车次流量=loc_child_TtoT("wx8d75e764f0c4bf1c:pages/station/pages/stationInfo/stationInfo.html:VISIBLE","车次流量")
    btn_车站流量_车次流量=loc_child_TtoT("wx8d75e764f0c4bf1c:pages/station/pages/stationInfo/stationInfo.html:VISIBLE","车次流量")

    btn_车站流量_候车大屏=loc_child_TtoT("wx8d75e764f0c4bf1c:pages/station/pages/stationInfo/stationInfo.html:VISIBLE","候车大屏")
    btn_车站流量_到达大屏=loc_child_TtoT("wx8d75e764f0c4bf1c:pages/station/pages/stationInfo/stationInfo.html:VISIBLE","到达大屏")


    btn_车站流量_查看全部车次=loc_child_TtoT("wx8d75e764f0c4bf1c:pages/station/pages/stationInfo/stationInfo.html:VISIBLE","查看全部车次")

    btn_车站流量_时刻查询=loc_child_TtoT("wx8d75e764f0c4bf1c:pages/station/pages/stationInfo/stationInfo.html:VISIBLE","时刻查询")
    btn_车站流量_行李托运=loc_child_TtoT("wx8d75e764f0c4bf1c:pages/station/pages/stationInfo/stationInfo.html:VISIBLE","行李托运")
    btn_车站流量_车站地图=loc_child_TtoT("wx8d75e764f0c4bf1c:pages/station/pages/stationInfo/stationInfo.html:VISIBLE","车站地图")

    "操作层"

    @allure.step(title='点击_车站流量_旅客流量')
    def click_车站流量_旅客流量(self):
        return self.click_点击(self.btn_车站流量_旅客流量,"click_车站流量_旅客流量")

    @allure.step(title='点击_车站流量_车次流量')
    def click_车站流量_车次流量(self):
        return self.click_点击(self.btn_车站流量_车次流量,"click_车站流量_车次流量")

    @allure.step(title='点击_车站流量_候车大屏')
    def click_车站流量_候车大屏(self):
        return self.click_点击(self.btn_车站流量_候车大屏,"click_车站流量_候车大屏")

    @allure.step(title='点击_车站流量_到达大屏')
    def click_车站流量_到达大屏(self):
        return self.click_点击(self.btn_车站流量_到达大屏,"click_车站流量_到达大屏")

    @allure.step(title='点击_车站流量_查看全部车次')
    def click_车站流量_查看全部车次(self):
        return self.click_点击(self.btn_车站流量_查看全部车次,"btn_车站流量_查看全部车次")

    @allure.step(title='点击_车站流量_时刻查询')
    def click_车站流量_时刻查询(self):
        btn_车站流量_时刻查询 = self.find_element_with_scroll("时刻查询")
        return self.click_点击(btn_车站流量_时刻查询,"btn_车站流量_时刻查询")

    @allure.step(title='点击_车站流量_行李托运')
    def click_车站流量_行李托运(self):
        return self.click_点击(self.btn_车站流量_行李托运,"btn_车站流量_行李托运")

    @allure.step(title='点击_车站流量_车站地图')
    def click_车站流量_车站地图(self):
        return self.click_点击(self.btn_车站流量_车站地图,"btn_车站流量_车站地图")

    @allure.step(title='获取_车站流量_旅客流量文本')
    def get_车站流量_旅客流量(self):
        return self.get_元素文本(self.txt_车站流量_旅客流量,"txt_车站流量_旅客流量")

    @allure.step(title='获取_车站流量_车次流量文本')
    def get_车站流量_车次流量(self):
        return self.get_元素文本(self.txt_车站流量_车次流量,"txt_车站流量_旅客流量")

    @allure.step(title='检查_车站流量_旅客流量or车次流量')
    def check_车站流量_车次流量or旅客流量(self,车次流量or旅客流量):
        instance1=[7,9,11,13,15,17]
        instance2=[7,9,11,13,15]
        a1=[]
        a2=[]
        if 车次流量or旅客流量=="车次流量":
            self.click_车站流量_车次流量()
            for i in instance1:
                eg1=self.get_元素文本(loc_child_TtoC_Number("wx8d75e764f0c4bf1c:pages/station/pages/stationInfo/stationInfo.html:VISIBLE","android.view.View",i-1),"循环获取字段")
                a1.append(eg1)
            return a1
        elif 车次流量or旅客流量=="旅客流量":
            self.click_车站流量_旅客流量()
            for j in instance2:
                eg2=self.get_元素文本(loc_child_TtoC_Number("wx8d75e764f0c4bf1c:pages/station/pages/stationInfo/stationInfo.html:VISIBLE","android.view.View",j-1),"循环获取字段")
                a2.append(eg2)
            return a2

    @allure.step(title='检查_车站流量_候车大屏')
    def check_车站流量_候车大屏or到达大屏(self,候车大屏or到达大屏):
        instance1=[23,24,25,26,27]
        a1=[]
        self.act_上滑(2)
        if 候车大屏or到达大屏=="候车大屏":
            self.click_车站流量_候车大屏()
        elif 候车大屏or到达大屏=="到达大屏":
            self.click_车站流量_到达大屏()
        for i in instance1:
           eg1=self.get_元素文本(loc_child_TtoC_Number("wx8d75e764f0c4bf1c:pages/station/pages/stationInfo/stationInfo.html:VISIBLE","android.view.View",i),"循环获取字段")
           a1.append(eg1)
        return a1
