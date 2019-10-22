from common.loc import *
from businessView.page_首页 import page_首页
from time import sleep
from common.request import *
class page_车站大屏(page_首页):


    "车站大屏顶部模块"
    text_点击车次查看详情文案提示 = loc_child_TtoC_Number(
        "wx8d75e764f0c4bf1c:pages/station/pages/stationLargeScreen/index.html:VISIBLE", "android.view.View", 1)

    btn_车站大屏_候车=loc_child_TtoC_Number("wx8d75e764f0c4bf1c:pages/station/pages/stationLargeScreen/index.html:VISIBLE","android.view.View",2)
    btn_车站大屏_到达=loc_child_TtoC_Number("wx8d75e764f0c4bf1c:pages/station/pages/stationLargeScreen/index.html:VISIBLE","android.view.View",3)
    "输入车次号前,点击此按钮"
    btn_车站大屏_车次号=loc_child_TtoC_Number("wx8d75e764f0c4bf1c:pages/station/pages/stationLargeScreen/index.html:VISIBLE","android.view.View",4)
    btn_车站大屏_高铁动车=loc_child_TtoCT_Number("wx8d75e764f0c4bf1c:pages/station/pages/stationLargeScreen/index.html:VISIBLE","android.view.View",5)


    "车次列表"

    btn_车站大屏_第一行=loc_child_TtoCT_Number("wx8d75e764f0c4bf1c:pages/station/pages/stationLargeScreen/index.html:VISIBLE",":",0)

    btn_车站大屏_小键盘_回退=loc_child_TtoC_Number("wx8d75e764f0c4bf1c:pages/station/pages/stationLargeScreen/index.html:VISIBLE","android.widget.Image",3)
    btn_车站大屏_小键盘_收起=loc_child_TtoC_Number("wx8d75e764f0c4bf1c:pages/station/pages/stationLargeScreen/index.html:VISIBLE","android.widget.Image",4)

    "操作层"
    def get_点击车次查看详情文案(self):
        return self.get_元素文本(self.text_点击车次查看详情文案提示,'text_点击车次查看详情')

    def click_车站大屏_候车(self):
        return self.click_点击(self.btn_车站大屏_候车,"btn_车站大屏_候车")

    def click_车站大屏_到达(self):
        return self.click_点击(self.btn_车站大屏_到达,"btn_车站大屏_到达")


    "业务层"
    def bus_车站大屏_点击指定行(self,number=0):
        return self.click_点击(loc_child_TtoCT_Number("wx8d75e764f0c4bf1c:pages/station/pages/stationLargeScreen/index.html:VISIBLE",":",number),"bus_车站大屏_第{}行".format(number))

    def bus_车站大屏_候车信息检查(self,候车or到达):
        instance1=[6,7,8,9,10]
        a1=[]
        if 候车or到达=="候车":
            self.click_车站大屏_候车()
        elif 候车or到达=="到达":
            self.click_车站大屏_到达()
        for i in instance1:
           eg1=self.get_元素文本(loc_child_TtoC_Number("wx8d75e764f0c4bf1c:pages/station/pages/stationLargeScreen/index.html:VISIBLE","android.view.View",i),"循环获取字段信息!")
           a1.append(eg1)
        return a1

    def bus_车站大屏_车次搜索数据(self):
        res={}
        data = {"stationName": "浠水站", "pageNumber": 1, "pageSize": 20, "trainType": 2}
        r = get_requests("/vega-station/vehiclenavigation/getMiniAppWaitListNew", data)
        终点站 = r["data"][0]["route"][1]
        trainNo=r["data"][0]["trainNo"]
        res["终点站"]=终点站
        res["trainNo"]=trainNo
        return res

    def bus_车站大屏_输入车次号(self):
        info=self.bus_车站大屏_车次搜索数据()["trainNo"]
        self.act_键盘输入(info)
        self.click_点击(info,"点击"+info+"车次")

if __name__ == '__main__':
    data = {"stationName": "浠水站", "pageNumber": 1, "pageSize": 20, "trainType": 2}
    r=get_requests("/vega-station/vehiclenavigation/getMiniAppWaitListNew", data)
    终点站 = r["data"][0]
    print(终点站)
    # kv = r["data"][0]
    # for k in kv:
    #     print(str(k) + ":" + str(kv[k]))




