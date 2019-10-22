from businessView import page_始发站选择, page_更多服务, page_站点搜索, page_车次正点率, page_选择城市
from businessView.page_个人中心 import page_个人中心
from businessView.page_优惠券 import page_优惠券
from businessView.page_余票查询 import page_余票查询
from businessView.page_公告详情 import page_公告详情
from businessView.page_切换站点 import page_切换站点
from businessView.page_取纸机 import page_取纸机
from businessView.page_城市搜索 import page_城市搜索
from businessView.page_填写评论 import page_填写评论
from businessView.page_店铺详情 import page_店铺详情
from businessView.page_意见反馈 import page_意见反馈
from businessView.page_我的 import page_我的
from businessView.page_我的积分 import page_我的积分
from businessView.page_我的资料 import page_我的资料
from businessView.page_检票口 import page_检票口
from businessView.page_添加行程 import page_添加行程
from businessView.page_玩转车站 import page_玩转车站
from businessView.page_登录12306 import page_登录12306
from businessView.page_站内商业 import page_站内商业
from businessView.page_行程 import page_行程
from businessView.page_车次详情 import page_车次详情
from businessView.page_车次途经站点 import page_车次途经站点
from businessView.page_车站大屏 import page_车站大屏
from businessView.page_车站天气 import page_车站天气
from businessView.page_车站头条 import page_车站头条
from businessView.page_车站流量 import page_车站流量
from businessView.page_选择城市 import Page_选择城市
from businessView.page_选择日期 import page_选择日期
from businessView.page_选择车次 import page_选择车次
from businessView.page_选择车次出发和到达 import page_选择车次出发和到达
from businessView.page_首页 import page_首页
from businessView.page_首页底部服务页面 import page_首页底部服务页面


class Page:

    def __init__(self, driver):
        self.driver = driver

    @property
    def 个人中心( self ):
        return page_个人中心(self.driver)

    @property
    def 优惠券( self ):
        return page_优惠券(self.driver)

    @property
    def 余票查询( self ):
        return page_余票查询(self.driver)

    @property
    def 公告详情( self ):
        return page_公告详情(self.driver)

    @property
    def 切换站点( self ):
        return page_切换站点(self.driver)

    @property
    def 取纸机( self ):
        return page_取纸机(self.driver)

    @property
    def 城市搜索( self ):
        return page_城市搜索(self.driver)

    @property
    def 填写评论( self ):
        return page_填写评论(self.driver)

    @property
    def 始发站选择( self ):
        return page_选择车次出发和到达(self.driver)

    @property
    def 店铺详情( self ):
        return page_店铺详情(self.driver)

    @property
    def 意见反馈( self ):
        return page_意见反馈(self.driver)

    @property
    def 我的( self ):
        return page_我的(self.driver)

    @property
    def 我的积分( self ):
        return page_我的积分(self.driver)

    @property
    def 我的资料( self ):
        return page_我的资料(self.driver)

    @property
    def 更多服务( self ):
        return page_更多服务(self.driver)

    @property
    def 检票口( self ):
        return page_检票口(self.driver)

    @property
    def 添加行程( self ):
        return page_添加行程(self.driver)

    @property
    def 玩转车站( self ):
        return page_玩转车站(self.driver)

    @property
    def 登录12306( self ):
        return page_登录12306(self.driver)

    @property
    def 站内商业( self ):
        return page_站内商业(self.driver)

    @property
    def 城市搜索( self ):
        return page_城市搜索(self.driver)

    @property
    def 行程( self ):
        return page_行程(self.driver)

    @property
    def 车次正点率( self ):
        return page_车次正点率(self.driver)

    @property
    def 车次详情( self ):
        return page_车次详情(self.driver)

    @property
    def 车次途经站点( self ):
        return page_车次途经站点(self.driver)

    @property
    def 车站大屏( self ):
        return page_车站大屏(self.driver)

    @property
    def 车站天气( self ):
        return page_车站天气(self.driver)

    @property
    def 车站头条( self ):
        return page_车站头条(self.driver)

    @property
    def 车站流量( self ):
        return page_车站流量(self.driver)

    @property
    def 选择城市( self ):
        return Page_选择城市(self.driver)

    @property
    def 选择日期( self ):
        return page_选择日期(self.driver)

    @property
    def 选择车次( self ):
        return page_选择车次(self.driver)

    @property
    def 首页( self ):
        return page_首页(self.driver)

    @property
    def 首页底部服务页面( self ):
        return page_首页底部服务页面(self.driver)

    @property
    def 选择车次出发和到达( self ):
        return page_选择车次出发和到达(self.driver)

