# codding:utf-8
import requests
import time
import logging
from function.function import path_项目路径
import yaml

"token: deb146f5ccb2490e99f7f5c92ee80634"
'token: c9e2527e3962444698575a83a1a638e6'

def get_host_cx9z():
    with open(path_项目路径() + r"config\api_conf.yaml", "r", encoding="utf-8") as file:
        yamldata = yaml.load(file, Loader=yaml.FullLoader)
        return [yamldata["host1"], yamldata["token"]]

def get_host_wtkj():
    with open(path_项目路径() + r"config\api_conf.yaml", "r", encoding="utf-8") as file:
        yamldata = yaml.load(file, Loader=yaml.FullLoader)
        return [yamldata["host3"], yamldata["token"]]

def get_requests_wtkj(path,form_datas=None):
    base_url = get_host_cx9z()[0] + path
    header = {"content-type": "application/x-www-form-urlencoded", "token": get_host_cx9z()[1]}
    if form_datas==None:
        r = requests.get(base_url, headers=header)
    else:
        r = requests.get(base_url, headers=header, params=form_datas)
    return r.json()

def get_requests(path,form_datas=None):
    base_url = get_host_cx9z()[0] + path
    header = {"content-type": "application/x-www-form-urlencoded", "token": get_host_cx9z()[1]}
    if form_datas==None:
        r = requests.get(base_url, headers=header)
    else:
        r = requests.get(base_url, headers=header, params=form_datas)
    return r.json()

def post_requests(path,form_datas=None):
    base_url = get_host_wtkj()[0] + path
    print(base_url)
    header = {"content-type": "application/json","charset":"UTF-8", "token": get_host_wtkj()[1]}
    print(get_host_wtkj())
    if form_datas==None:
        r = requests.post(base_url, headers=header)
    else:
        r = requests.post(base_url, headers=header, data=form_datas)
    return r.json()

def delete_所有绑定行程(token, ):
    # e88dab00c8c24e89865c6abf9cc0f9de(测试环境)
    # "bdadc81b4ebb40af8c4af9e35a6552fd"(线上)
    host = get_host()
    base_url = host + r"galaxy/schedule/queryScheduleListWithXiaochang"
    header = {"content-type": "application/x-www-form-urlencoded", "token": token}
    r = requests.post(base_url, headers=header)
    route_data = r.json()["data"]["data"]
    # return r.headers
    if route_data == None:
        print("没有绑定行程")
        logging.info("没有绑定行程")
    else:
        lens = len(r.json()["data"]["data"])
        for i in range(lens):
            # print(route_data[i]["trainSchedule"]["startStation"])
            # print(route_data[i]["trainSchedule"]["startTime"])
            # print(route_data[i]["trainSchedule"]["trainNo"])
            # print(route_data[i]["trainSchedule"]["scheduleType"])
            startStation = route_data[i]["trainSchedule"]["startStation"]
            trainNo = route_data[i]["trainSchedule"]["trainNo"]
            scheduleType = route_data[i]["trainSchedule"]["scheduleType"]
            times = route_data[i]["trainSchedule"]["startTime"]
            timeStamp = int(times) / 1000
            timeArray = time.localtime(timeStamp)
            formatTime = time.strftime("%Y-%m-%d %H:%M", timeArray)
            base_url2 = host + r"galaxy/schedule/deleteRefundScheduleV2"
            fdata = {"trainNo": trainNo, "startStation": startStation, "startTime": formatTime,
                     "scheduleType": scheduleType}
            r = requests.post(base_url2, headers=header, data=fdata)
            if r.json()["msg"] == "删除成功":
                print("删除成功")
                logging.info("删除成功!")
            else:
                print("删除失败")
                logging.info("删除失败")

if __name__ == '__main__':
    import json
    form_datas={"date":"2019-08-27","trainNO":"G74"}
    r = get_requests('/vega-station/schedule/detailByTrainNo',form_datas=form_datas)
    print(r)