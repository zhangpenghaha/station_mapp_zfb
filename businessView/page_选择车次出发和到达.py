from businessView.page_首页 import page_首页
from businessView.page_添加行程 import page_添加行程
from common.request import get_requests
from common.loc import *
from datetime import time
from function.funcdate import *
import logging
import allure
class page_选择车次出发和到达(page_首页,page_添加行程):
    # Host: www.cx9z.com
    '''
    定位器
    '''
    title_选择车次出发和到达_车次号 = loc_id('com.tencent.mm:id/ox')

    btn_选择车次出发和到达_跨天第一个 = loc_contains_text_instance('→', 0)

    btn_选择车次出发和到达_确认添加 = loc_text("确定添加")

    '''
    操作层
    '''

    @allure.step(title='点击_选择车次出发和到达_跨天第一个')
    def click_选择车次出发和到达_跨天第一个(self):
        return self.click_点击(self.btn_选择车次出发和到达_跨天第一个, 'btn_选择车次出发和到达_跨天第一个')

    @allure.step(title='获取选择车次出发和到达_车次号文本')
    def get_选择车次出发和到达_车次号(self):
        return self.get_元素文本(self.title_选择车次出发和到达_车次号, 'title_选择车次出发和到达_车次号')

    @allure.step(title='点击_选择车次出发和到达_确认添加')
    def click_选择车次出发和到达_确认添加(self):
        return self.click_点击(self.btn_选择车次出发和到达_确认添加,"btn_选择车次出发和到达_确认添加")

    # G74
    @allure.step(title='根据车次号获取车次详情api信息')
    def get_api_车次详情根据车次号(self,车次号):
        '''# 调用了获取列车详情接口
        :return: 字典   字段"endDate" 字段为到达时间 ,字段"arr_station"为途径站点列表
        '''
        返回结果 = {}
        回返途径站点 = []
        # 车次号 = self.get_选择车次出发和到达_车次号()
        path = '/vega-station/schedule/detailByTrainNo'
        form_datas = {"date": get_当前年月日(), "trainNO": 车次号}
        r = get_requests(path, form_datas=form_datas)
        返回结果['endDate'] = r['endDate']
        for i in range(len(r['data'])):
            for j in r['data'][i]:
                回返途径站点.append(j['station_name'])
        返回结果['arr_station'] = 回返途径站点
        return 返回结果

    @allure.step(title='选择始终站')
    def bus_选择始终站(self,车次号,滑动次数=4,点击确认添加=False):
        起点站 = self.get_api_车次详情根据车次号(车次号)['arr_station'][0]
        logging.info(起点站)
        终到站 = self.get_api_车次详情根据车次号(车次号)['arr_station'][-1]
        logging.info(起点站)
        if self.get_api_车次详情根据车次号(车次号)['endDate'] == get_当前年月日():
            self.click_点击(loc_text(起点站), "点击起点站点" + 起点站)
            self.act_上滑(滑动次数)
            self.click_点击(loc_text(终到站), "点击起点站点" + 终到站)
        else:
            self.click_点击(loc_text(起点站), "点击起点站点" + 起点站)
            self.act_上滑(滑动次数)
            self.click_点击(loc_text(终到站), "点击起点站点" + 终到站)
            self.click_选择车次出发和到达_跨天第一个()
        if 点击确认添加==True:
            self.click_选择车次出发和到达_确认添加()

if __name__ == '__main__':
    # form_datas={"date":"2019-08-27","trainNO":"G74"}
    # r = get_requests('/vega-station/schedule/detailByTrainNo',form_datas=form_datas)
    # print(r['data'][0])
    返回结果 = {}
    回返途径站点 = []
    path = '/vega-station/schedule/detailByTrainNo'
    form_datas = {"date": get_当前年月日(), "trainNO": str("G835")}
    r = get_requests(path, form_datas=form_datas)
    返回结果['endDate'] = r['endDate']
    for i in range(len(r['data'])):
        for j in r['data'][i]:
            回返途径站点.append(j['station_name'])
    返回结果['arrive_time'] = 回返途径站点
    print(返回结果)