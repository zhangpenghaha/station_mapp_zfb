from common.loc import *
from businessView.page_首页 import page_首页
from time import sleep
from common.request import *
import allure


class page_车站大屏(page_首页):


    "车站大屏顶部模块"
    # text_点击车次查看详情文案提示 = loc_child_TtoC_Number(
    #     "wx8d75e764f0c4bf1c:pages/station/pages/stationLargeScreen/index.html:VISIBLE", "android.view.View", 1)
    #
    # btn_车站大屏_候车=loc_child_TtoC_Number("wx8d75e764f0c4bf1c:pages/station/pages/stationLargeScreen/index.html:VISIBLE","android.view.View",2)
    # btn_车站大屏_到达=loc_child_TtoC_Number("wx8d75e764f0c4bf1c:pages/station/pages/stationLargeScreen/index.html:VISIBLE","android.view.View",3)
    # "输入车次号前,点击此按钮"
    # btn_车站大屏_车次号=loc_child_TtoC_Number("wx8d75e764f0c4bf1c:pages/station/pages/stationLargeScreen/index.html:VISIBLE","android.view.View",4)
    # btn_车站大屏_高铁动车=loc_child_TtoCT_Number("wx8d75e764f0c4bf1c:pages/station/pages/stationLargeScreen/index.html:VISIBLE","android.view.View",5)
    btn_C = loc_text("C")
    text_点击车次查看详情文案提示 = loc_text("点击车次 查看详情")
    btn_车站大屏_候车 = loc_text("候车")
    btn_车站大屏_到达 = loc_text("到达")
    btn_车站大屏_车次号 = loc_text("请输入要查询的车次号")
    btn_车站大屏_高铁动车 = loc_text("高铁动车")
    # btn_车站大屏_高铁动车 = loc_text("高铁动车")
    text_输入框文案 = loc_text("请输入要查询的车次号")
    text_以上信息仅供参考文案 = loc_text("以上信息仅供参考，实际情况以车站公告为准")
    "车次列表"

    btn_车站大屏_第一行=loc_child_TtoCT_Number("wx8d75e764f0c4bf1c:pages/station/pages/stationLargeScreen/index.html:VISIBLE",":",0)

    btn_车站大屏_小键盘_回退=loc_child_TtoC_Number("wx8d75e764f0c4bf1c:pages/station/pages/stationLargeScreen/index.html:VISIBLE","android.widget.Image",3)
    btn_车站大屏_小键盘_收起=loc_child_TtoC_Number("wx8d75e764f0c4bf1c:pages/station/pages/stationLargeScreen/index.html:VISIBLE","android.widget.Image",4)

    "操作层"

    def get_点击车次查看详情文案( self ):
        return self.get_元素文本(self.text_点击车次查看详情文案提示, 'text_点击车次查看详情')

    def get_以上信息仅供参考文案( self ):
        return self.get_元素文本(self.text_以上信息仅供参考文案, 'text_以上信息仅供参考文案')

    @allure.step(title='获取车次查看详情')
    def get_点击车次查看详情文案(self):
        return self.get_元素文本(self.text_点击车次查看详情文案提示,'text_点击车次查看详情')

    @allure.step(title='点击_车站大屏_候车')
    def click_车站大屏_候车(self):
        return self.click_点击(self.btn_车站大屏_候车,"btn_车站大屏_候车")

    @allure.step(title='点击_车站大屏_到达')
    def click_车站大屏_到达(self):
        return self.click_点击(self.btn_车站大屏_到达,"btn_车站大屏_到达")

    @allure.step(title='点击_车站大屏_到达')
    def get_键盘元素(self):
        self.click_点击(self.text_输入框文案,"text_输入框文案")
        return self.get_元素文本(self.btn_C,"btn_C")

    @allure.step(title='点击_车站大屏_到达')
    def input_输入车次号(self,TrainNo,text):
        self.click_点击(self.text_输入框文案, "text_输入框文案")
        self.act_键盘输入(TrainNo)
        return self.get_toast(text)

    @allure.step(title='点击_车站大屏_到达')
    def click_勾选高铁动车(self):
        self.click_点击(self.btn_车站大屏_高铁动车,"btn_车站大屏_高铁动车")
        return self.get_toast("暂无相关数据")

    @allure.step(title='点击_车站大屏_到达')
    def click_清空(self,TrainNo):
        self.click_点击(self.text_输入框文案, "text_输入框文案")
        self.act_键盘输入(TrainNo)
        self.click_点击(self.img_清空,"img_清空")
        return self.get_toast(TrainNo)

    @allure.step(title='点击_车站大屏_到达')
    def click_车次号(self,TrainNo):
        self.click_点击(self.text_输入框文案, "text_输入框文案")
        self.act_键盘输入(TrainNo)
        self.click_点击(self.text_车次号,"text_车次号")
        return self.get_toast("请选择出发站和到达站")

    @allure.step(title='点击_车站大屏_到达')
    def check_起始站(self,TrainNo):
        self.click_点击(self.text_输入框文案, "text_输入框文案")
        self.act_键盘输入(TrainNo)
        self.click_点击(self.text_车次号, "text_车次号")
        return self.get_元素文本(self.text_浠水站,"text_浠水站")

    @allure.step(title='点击_车站大屏_到达')
    def check_结果页文案(self,TrainNo,text):
        self.click_点击(self.text_输入框文案, "text_输入框文案")
        self.act_键盘输入(TrainNo)
        self.click_点击(self.text_车次号, "text_车次号")
        return self.get_toast(text)

    @allure.step(title='获取——输入框文文本')
    def get_输入框文案(self):
        return self.get_元素文本(self.text_输入框文案,"text_输入框文案")

    "业务层"

    @allure.step(title='点击所在城市站点')
    def bus_车站大屏_点击指定行(self,number=0):
        return self.click_点击(loc_child_TtoCT_Number("wx8d75e764f0c4bf1c:pages/station/pages/stationLargeScreen/index.html:VISIBLE",":",number),"bus_车站大屏_第{}行".format(number))

    @allure.step(title='车站大屏_候车信息检查')
    def bus_车站大屏_候车信息检查(self,候车or到达):
        instance1=[6,7,8,9,10]
        a1=[]
        if 候车or到达=="候车":
            self.click_车站大屏_候车()
            a = ["车次", "终到站", "发车", "检票口", "状态"]
            for i in a:
                eg1 = self.get_toast(i)
                a1.append(eg1)
            print(a1)
            return a1
        elif 候车or到达=="到达":
            self.click_车站大屏_到达()
            a = ["车次", "始发站", "到本站", "出站口", "状态"]
            for i in a:
                eg1 = self.get_toast(i)
                a1.append(eg1)
            return a1
        # for i in instance1:
           # eg1=self.get_元素文本(loc_child_TtoC_Number("wx8d75e764f0c4bf1c:pages/station/pages/stationLargeScreen/index.html:VISIBLE","android.view.View",i),"循环获取字段信息!")
           # eg1 = self.get_元素文本(loc_child_IDtoC_Number("__react-content","android.view.View",i),"循环获取字段信息!")
           # a1.append(eg1)
        # return a1

    @allure.step(title='车站大屏_车次搜索数据')
    def bus_车站大屏_车次搜索数据(self):
        res={}
        data = {"stationName": "浠水站", "pageNumber": 1, "pageSize": 20, "trainType": 2}
        r = get_requests("/vega-station/vehiclenavigation/getMiniAppWaitListNew", data)
        终点站 = r["data"][0]["route"][1]
        trainNo=r["data"][0]["trainNo"]
        res["终点站"]=终点站
        res["trainNo"]=trainNo
        return res

    @allure.step(title='车站大屏_输入车次号')
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




