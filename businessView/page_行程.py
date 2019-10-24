from appium.webdriver.common.touch_action import TouchAction
from common.common import common
from common.loc import *
from common.request import *
import allure

class page_行程(common):
    "定位器!!!!!!!!!!!!!!!!!!!!!!!"
    btn_行程 = loc_text("行程")
    btn_行程_添加行程1 = loc_text("+添加行程")
    btn_行程_添加行程2 = loc_id("ATtrain2")

    btn_行程_手动添加 = loc_text("手动添加")
    btn_行程_取消 = loc_text("取消")
    btn_行程_删除 = loc_id_instance("detele", 0)
    btn_分享 = loc_id("ATtrain1_0")
    btn_关闭分享 = loc_id("ATtrain3")
    "操作层"

    @allure.step(title='点击行程')
    def click_点击行程(self):
        return self.click_点击(self.btn_行程, "btn_点击行程")

    @allure.step(title='点击分享行程')
    def click_点击分享(self):
        return self.click_点击(self.btn_分享, "btn_分享")

    @allure.step(title='关闭分享')
    def click_关闭分享行程(self):
        return self.click_点击(self.btn_关闭分享, "关闭分享行程")

    @allure.step(title='点击添加行程_十字图标')
    def click_添加行程2(self):
        return self.click_点击(self.btn_行程_添加行程2, "添加行程")
        # a = self.get_screenSize()
        # x = a[0] * 0.92
        # y = a[1] * 0.77
        # return TouchAction(self.driver).tap(x=x, y=y).perform()

    @allure.step(title='点击添加行程')
    def click_行程_添加行程(self):
        if self.click_点击(self.btn_行程_添加行程1, "btn_行程_添加行程"):
            return
        else:
            return self.click_添加行程2()

    @allure.step(title='获取添加行程文本')
    def get_行程_添加行程(self):
        return self.get_元素文本(self.btn_行程_添加行程1, "btn_添加行程1")

    @allure.step(title='获取添加行程_手动添加文本')
    def get_行程_手动添加(self):
        return self.get_元素文本(self.btn_行程_手动添加, "btn_手动添加")

    @allure.step(title='点击行程_手动添加行程')
    def click_行程_手动添加(self):
        self.click_点击(self.btn_行程_手动添加,"btn_行程_手动添加")

    @allure.step(title='点击_行程_删除行程')
    def click_行程_删除(self):
        return self.click_点击(self.btn_行程_删除, "btn_行程_删除")

    @allure.step(title='点击_行程_删除首个行程')
    def bus_行程_删除首个行程(self):
        a = self.click_行程_删除()
        b = self.click_确定()
        # return a + b

    @allure.step(title='点击行程_删除全部行程')
    def bus_行程_删除全部(self, num_删除个数=20):
        num = 0
        while True:
            num += 1
            self.bus_行程_删除首个行程()
            if  self.click_点击(self.btn_行程_删除, "btn_行程_删除") is None:
                break
            if num_删除个数 == num :
                break

    def scoll_滑动找车次信息(self, text):
        return self.click_loc_with_scroll(text)

    @allure.step(title='获取行程_车次_api信息')
    def get_api_行程_车次(self):
        """

        :param userID: 配置文件获取
        :return: 当前用户绑定的行程列表  按时间排序的车次  列表
        """
        with open(path_项目路径() + r"config\api_conf.yaml", "r", encoding="utf-8") as file:
            yamldata = yaml.load(file, Loader=yaml.FullLoader)
        我的行程 = {}
        行程=[]
        path = "/galaxy/schedule/queryScheduleListWithXiaochangNew/"
        # data = {"userId": "111434"}
        data = {"userId":str(yamldata["userId"])}
        a = post_requests(path, form_datas=data)

        for i in range(len(a['data']['current'])):
            行程.append(a['data']['current'][i]['schedule']['trainNo'])
        我的行程["行程"] = 行程
        我的行程["数量"] = len(a['data']['current'])
        return 我的行程

    @allure.step(title='手动添加行程')
    def bus_行程_手动添加(self):
        self.click_行程_添加行程()
        self.click_行程_手动添加()

    @allure.step(title='删除行程')
    def check_行程_删除行程(self):
        flag = 1
        a1 = self.get_api_行程_车次()["行程"]
        s1 = self.bus_行程_删除首个行程()
        for i in range(1,len(a1)):
            b = self.judge_元素(loc_text(a1[i]))
            flag*=b
        c = self.judge_元素(loc_text(a1[0]))
        actrul=str(s1) + str(flag) + str(c)
        if actrul=="210":
            return 1
        else:
            return 0


        # get_requests()
        # for i in 车次号:
        #     self.


if __name__ == '__main__':
    with open(path_项目路径() + r"config\api_conf.yaml", "r", encoding="utf-8") as file:
        yamldata = yaml.load(file, Loader=yaml.FullLoader)
    我的行程 = {}
    行程 = []
    path = "/galaxy/schedule/queryScheduleListWithXiaochangNew/"
    # data = {"userId": "111434"}
    data = {"userId": str(yamldata["userId"])}
    a = post_requests(path, form_datas=data)

    for i in range(len(a['data']['current'])):
        行程.append(a['data']['current'][i]['schedule']['trainNo'])
    我的行程["行程"] = 行程
    我的行程["数量"] = len(a['data']['current'])
    print(我的行程)
