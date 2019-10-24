import allure

from common.common import common
from common.loc import *
from common.request import *


class page_首页(common):
    "定位器!!!!!!!!!!!!!!!!!!!!!!!"

    "焦点"
    btn_首页_焦点 = loc_id("com.tencent.mm:id/ut")

    "页面标题"
    txt_车站通_标题 = loc_text("车站通")

    "顶部模块栏位(城市和天气按钮)"
    # btn_切换站点 = loc_child_TtoCT_Number("wx8d75e764f0c4bf1c:pages/tabBar/station/index.html:VISIBLE", "站", 0)
    # btn_切换站点 = loc_text("切换站点")
    # btn_切换站点 = loc_contains_text("站")
    btn_切换站点 = loc_child_IDtoC_Number("AThome1_1","android.view.View", 0)
    btn_首页_天气页面 = loc_id("AThome2")

    "站点切换提示"
    txt_首页_站点切换提示 = loc_start_text("定位显示您在")
    btn_首页_切换站点按钮 = loc_start_text("切换到")

    "banner图"
    btn_首页_banner_1=loc_id("AThome3_0")
    btn_点击查看车站流量 = loc_text("点击查看车站流量")

    "菜单模块阵列下面的按钮"
    btn_余票查询 = loc_text("余票查询")
    btn_更多服务 = loc_text("更多服务")
    txt_更多服务 = loc_text("更多服务")
    btn_车站大屏 = loc_text("车站大屏")

    "车站头条"
    btn_滚动公告 = loc_text("可竖向滚动")
    btn_更多_车站头条 = loc_text("更多")

    " 时刻查询模块按钮 "
    txt_首页_时刻查询模块名 = loc_text("时刻查询")
    txt_请输入正确的车次号_toast = loc_text("请输入正确的车次号")
    btn_出发时间_今天 = loc_text("今天")
    btn_车次号输入框 = loc_start_text("车次号")
    # btn_首页_时刻查询_扫码 = loc_class_instance("android.widget.Button", 0)
    btn_首页_时刻查询_扫码 = loc_id("scanbtn")
    btn_首页_切换起始站点 = loc_class_instance("android.widget.Image", 10)
    # btn_首页_切换起始站点 = loc_child_TtoCT_Number("wx8d75e764f0c4bf1c:pages/tabBar/station/index.html:VISIBLE","android.widget.Image", 10)
    btn_首页_车次查询 = loc_text("车次查询")
    btn_首页_站站查询 = loc_text("站站查询")
    btn_首页_查询 = loc_text("查询")
    btn_关注车次信息 = loc_text("关注车次信息")
    btn_武汉 = loc_text("武汉")
    btn_站站查询_默认北京 = loc_text("北京")
    btn_出发时间月日 = loc_contains_text_instance("日", 0)
    btn_出发时间星期 = loc_contains_text("星期")
    txt_车次号输入框示例 = loc_start_text("例如: G520")
    btn_分享行程 = loc_text("分享行程")
    btn_关闭分享 = loc_id("AThome5")

    " 车站大屏 "
    txt_首页_车站大屏模块名 = loc_text_instance("车站大屏",0)
    btn_查看全部车次 = loc_text("查看全部车次")
    btn_首页车站大屏_到达按钮 = loc_text("到达")
    btn_首页车站大屏_候车按钮 = loc_text("候车")
    txt_首页车站大屏_发车 = loc_text("发车")
    txt_首页车站大屏_到本站 = loc_text("到本站")
    txt_首页车站大屏_终到站 = loc_text_instance("终到站",0)
    txt_首页车站大屏_始发站 = loc_text_instance("始发站",0)

    "======车站商业====="
    txt_首页_车站商业模块名 = loc_text("车站商业")
    btn_首页站内商业_查看全部 = loc_text("查看全部")
    btn_首页站内商业_进站前 = loc_text_instance("进站前",0)
    btn_首页站内商业_进站后 = loc_text_instance("进站后",0)

    "商铺"
    btn_首页_车站商业进站前1号位 = loc_text("便民超市")
    btn_首页_车站商业进站后1号位 = loc_text("平价自选商店")

    "=====更多服务====="
    btn_首页_更多服务_售卖机 = loc_text("售卖机")
    btn_首页_更多服务_洗手间 = loc_text("洗手间")


    "======底部模块====="
    btn_首页军人优先 = loc_text("军人优先")
    btn_首页服务评价 = loc_text("服务评价")
    btn_首页常见问题 = loc_text("常见问题")
    btn_首页关于我们 = loc_text("关于我们")

    "===========================操作层==========================="

    "首页焦点"

    @allure.step(title='关闭分享')
    def click_关闭分享(self):
        return self.click_点击(self.btn_关闭分享,"关闭分享")

    @allure.step(title='点击首页_焦点')
    def click_首页_焦点(self):
        return self.click_点击(self.btn_首页_焦点, "btn_首页_焦点")

    "顶部模块"
    def click_车站大屏(self):
        return self.click_点击(self.btn_车站大屏, "btn_车站大屏")

    @allure.step(title='点击_切换站点')
    def click_首页_切换站点按钮(self):
        return self.click_点击(self.btn_切换站点, "btn_切换站点")

    @allure.step(title='获取切换站点文本')
    def get_首页顶部_当前站点(self):
        return self.get_元素文本(self.btn_切换站点, "btn_切换站点")

    @allure.step(title='点击首页_天气页面')
    def click_首页_天气页面(self):
        return self.click_点击(self.btn_首页_天气页面,"btn_首页_天气页面")

    "切换站点提示"

    @allure.step(title='获取首页_切换站点提示')
    def get_首页_切换站点提示(self):
        return self.get_元素文本(self.txt_首页_站点切换提示, "txt_首页_站点切换提示")

    @allure.step(title='点击首页_切换站点提示按钮')
    def click_首页_切换站点提示按钮(self):
        return self.click_点击(self.btn_首页_切换站点按钮, "btn_首页_切换站点按钮")

    "banner图"

    @allure.step(title='点击首页_banner')
    def click_首页_banner_1(self):
        return self.click_点击(self.btn_首页_banner_1,"btn_首页_banner_1")

    @allure.step(title='点击_查看车站流量')
    def click_点击查看车站流量(self):
        return self.click_点击(self.btn_点击查看车站流量, "btn_点击查看车站流量")

    "菜单模块"

    @allure.step(title='点击_余票查询')
    def click_余票查询(self):
        return self.click_点击(self.btn_余票查询, "btn_余票查询")

    @allure.step(title='点击_更多服务_菜单')
    def click_更多服务_菜单(self):
        return self.click_点击(self.btn_更多服务, "btn_更多服务")

    "功能菜单"

    @allure.step(title='点击_更多服务')
    def click_更多服务(self):
        return self.click_点击(self.btn_更多服务, "btn_更多服务")

    "车站头条"

    @allure.step(title='点击_滚动公告')
    def click_滚动公告(self):
        return self.click_点击(self.btn_更多_车站头条, "btn_滚动公告")

    @allure.step(title='点击_更多资讯')
    def click_更多资讯(self):
        return self.click_点击(self.btn_更多_车站头条, "btn_更多_车站头条")

    "更多服务模块"

    @allure.step(title='获取_更多服务模块标题')
    def get_更多服务模块标题(self):
        return self.get_元素文本(self.txt_更多服务, "txt_更多服务")

    "绑定的行程"

    @allure.step(title='获取绑定的行程')
    def get_api_首页_绑定的行程(self):
        path = r"/galaxy/schedule/getUserNearestScheduleAli"

        get_requests(path)




    "时刻查询"

    @allure.step(title='点击首页_摄像头')
    def click_首页_摄像头(self):
        # self.click_首页_车次查询()
        return self.click_点击(self.btn_首页_时刻查询_扫码, "btn_首页_时刻查询_扫码")

    @allure.step(title='点击首页_切换起始站点')
    def click_首页_切换起始站点(self):
        self.click_首页_站站查询()
        return self.click_点击(self.btn_首页_切换起始站点, "btn_首页_切换起始站点")

    @allure.step(title='点击_出发时间_今天')
    def click_出发时间_今天(self):
        # return self.find_loc_with_scroll("今天")
        return self.click_点击(self.btn_出发时间_今天, "btn_出发时间_今天")

    @allure.step(title='点击首页_车次查询')
    def click_首页_车次查询(self):
        return self.click_点击(self.btn_首页_车次查询, "btn_车次查询")

    @allure.step(title='获取车次号输入框示例文本')
    def get_车次号输入框示例(self):
        return self.get_元素文本(self.txt_车次号输入框示例, "txt_车次号输入框示例")

    @allure.step(title='点击_车次号输入')
    def click_车次号输入(self):
        return self.click_点击(self.btn_车次号输入框, "btn_车次号输入框")

    @allure.step(title='获取_请输入正确的车次号_toast')
    def get_请输入正确的车次号_toast(self):
        return self.get_元素文本(self.txt_请输入正确的车次号_toast, "txt_请输入正确的车次号_toast")

    @allure.step(title='点击首页_时刻查询_查询')
    def click_首页_时刻查询_查询(self):
        # return self.find_loc_with_scroll("查询")
        return self.click_点击(self.btn_首页_查询, "btn_时刻查询_查询")

    @allure.step(title='点击首页_站站查询')
    def click_首页_站站查询(self):
        # btn_首页_站站查询 = self.find_loc_with_scroll("站站查询")
        return self.click_点击(self.btn_首页_站站查询, "btn_站站查询")

    @allure.step(title='点击_关注车次信息')
    def click_关注车次信息(self):
        return self.click_点击(self.btn_关注车次信息, "btn_关注车次信息")

    @allure.step(title='点击_出发时间日月')
    def click_某月某日(self):
        return self.click_点击(self.btn_出发时间月日, "btn_出发时间月日")

    @allure.step(title='获取出发时间日月文本')
    def get_选择后的出发某月某日(self):
        return self.get_元素文本(self.btn_出发时间月日, "btn_出发时间月日")

    @allure.step(title='获取_选择后的出发星期文本')
    def get_选择后的出发星期(self):
        return self.get_元素文本(self.btn_出发时间星期, "出发时间星期")

    @allure.step(title='获取_站站查询_目的地_北京文本')
    def get_站站查询_目的地_北京(self):
        return self.get_元素文本(self.btn_站站查询_默认北京, "btn_站站查询_默认北京")

    "车站大屏"

    @allure.step(title='点击查看全部车次')
    def click_查看全部车次(self):
        return self.click_点击(self.btn_查看全部车次, "btn_查看全部车次")

    @allure.step(title='点击_首页车站大屏_到达')
    def click_首页车站大屏_到达(self):
        return self.click_点击(self.btn_首页车站大屏_到达按钮, "btn_首页车站大屏_到达按钮")

    @allure.step(title='点击首页_车站大屏_候车')
    def click_首页车站大屏_候车(self):
        return self.click_点击(self.btn_首页车站大屏_候车按钮, "btn_首页车站大屏_候车按钮")

    @allure.step(title='获取_首页车站大屏_发车文本')
    def get_首页车站大屏_发车(self):
        return self.get_元素文本(self.txt_首页车站大屏_发车, "txt_首页车站大屏_发车")

    @allure.step(title='获取_首页车站大屏_终点站文本')
    def get_首页车站大屏_终到站(self):
        return self.get_元素文本(self.txt_首页车站大屏_终到站, "txt_首页车站大屏_终到站")

    @allure.step(title='获取首页_车站大屏_始发站文本')
    def get_首页车站大屏_始发站(self):
        return self.get_元素文本(self.txt_首页车站大屏_始发站, ".txt_首页车站大屏_始发站")

    @allure.step(title='获取首页_车站大屏_到本站文本')
    def get_首页车站大屏_到本站(self):
        return self.get_元素文本(self.txt_首页车站大屏_到本站, "txt_首页车站大屏_到本站")

    "站内商业"

    @allure.step(title='点击首页_车站山野进站前1号位')
    def click_首页_车站商业进站前1号位(self):
        return self.click_点击(self.btn_首页_车站商业进站前1号位, "btn_首页_车站商业进站前1号位")

    @allure.step(title='获取首页_车站商业进站前1号位文本')
    def get_首页_车站商业进站前1号位(self):
        return self.get_元素文本(self.btn_首页_车站商业进站前1号位, "btn_首页_车站商业进站前1号位")

    @allure.step(title='点击首页_车站商业进站后1号位')
    def click_首页_车站商业进站后1号位(self):
        return self.click_点击(self.btn_首页_车站商业进站后1号位, "btn_首页_车站商业进站后1号位")

    @allure.step(title='获取首页_车站商业进站后1号位文本')
    def get_首页_车站商业进站后1号位(self):
        return self.get_元素文本(self.btn_首页_车站商业进站后1号位, "btn_首页_车站商业进站后1号位")

    @allure.step(title='点击首页_车站商业_查看全部')
    def click_首页_车站商业查看全部(self):
        return self.click_点击(self.btn_首页站内商业_查看全部, "btn_首页站内商业_查看全部")

    @allure.step(title='点击首页_车站商业_进站前')
    def click_首页_车站商业进站前(self):
        return self.click_点击(self.btn_首页站内商业_进站前, "_首页站内商业_进站前")

    @allure.step(title='点击首页_车站商业_进站后')
    def click_首页_车站商业进站后(self):
        return self.click_点击(self.btn_首页站内商业_进站后, "_首页站内商业_进站后")

    "=========更多 服务========="

    @allure.step(title='点击首页_更多服务_服务项')
    def click_首页更多服务_服务项(self,server):
        return self.click_点击(loc_text(server), "点击"+server+"服务!")

    @allure.step(title='点击_分享行程')
    def click_分享行程(self):
        return self.click_点击(self.btn_分享行程, "btn_分享行程")

    "==========首页底部服务页面=========="

    @allure.step(title='点击首页_军人优先')
    def click_首页军人优先(self):
        # btn_首页军人优先 = self.find_loc_with_scroll("军人优先")
        return self.click_点击(self.btn_首页军人优先, "btn_首页军人优先")

    @allure.step(title='点击首页_服务评价')
    def click_首页服务评价(self):
        # btn_首页服务评价 = self.find_loc_with_scroll("服务评价")
        return self.click_点击(self.btn_首页服务评价, "btn_首页服务评价")

    @allure.step(title='点击首页_常见问题')
    def click_首页常见问题(self):
        # btn_首页常见问题 = self.find_loc_with_scroll("常见问题")
        return self.click_点击(self.btn_首页常见问题, "btn_首页常见问题")

    @allure.step(title='点击首页_关于我们')
    def click_首页关于我们(self):
        # btn_首页关于我们 = self.find_loc_with_scroll("关于我们")
        return self.click_点击(self.btn_首页关于我们, "btn_首页关于我们")

    "====================业务层====================="
    "时刻查询"

    @allure.step(title='点击首页_车次号搜索_时刻查询')
    def bus_首页_车次号搜索(self,车次号='K751'):
        self.click_车次号输入()
        self.act_键盘输入(车次号)
        self.click_首页_时刻查询_查询()
        return 车次号

# if __name__ == '__main__':
    # from appiumDriver.desired_caps import appium_微信车站通
    #
    # driver = appium_微信车站通()
    # dr = page_首页(driver)
    # dr.click_首页_切换站点提示按钮()
    # dr.click_首页_切换站点按钮()
    # path = r"/galaxy/schedule/getUserNearestScheduleAli"

    # a= get_requests_(path)
    # print(a)
