import logging
import logging.config
import time
from time import sleep

import yaml
from appium import webdriver
from selenium.common.exceptions import TimeoutException,NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait

from function.function import path_项目路径

"配置文件的路径"
log_conf_file_path = path_项目路径() + r'config\log.conf'
logging.config.fileConfig(log_conf_file_path)
logger = logging.getLogger()


def appium_微信车站通():
    desired_caps = {}
    with open(path_项目路径() + r'config\czt_wx.yaml', 'r', encoding='utf-8') as file:
        data = yaml.load(file, Loader=yaml.FullLoader)
        desired_caps['platformName'] = data['platformName']

        desired_caps['platformVersion'] = data['platformVersion']
        desired_caps['deviceName'] = data['deviceName']
        desired_caps['udid'] = data['udid']

        desired_caps['noReset'] = data['noReset']
        # desired_caps['fullReset'] = data['fullReset']

        desired_caps['unicodeKeyboard'] = data['unicodeKeyboard']
        desired_caps['resetKeyboard'] = data['resetKeyboard']

        desired_caps['appPackage'] = data['appPackage']
        desired_caps['appActivity'] = data['appActivity']

        desired_caps['automationName'] = data['automationName']

        # desired_caps['chromeOptions'] = data['chromeOptions']
        logging.info('======启动微信======')

        driver = webdriver.Remote('http://' + str(data['ip']) + ':' + str(data['port']) + '/wd/hub', desired_caps)
        try:
            WebDriverWait(driver, 20).until(lambda x: x.find_element_by_android_uiautomator('new UiSelector().text("发现")'))
        except TimeoutException:
            logging.error("发现查找元素超时!")
        except NoSuchElementException:
            logging.error("发现按钮元素找到不到！")

        else:
            logging.info("点击发现！")
            driver.find_element_by_android_uiautomator('new UiSelector().text("发现")').click()
            logging.info("点击小程序！")
            driver.find_element_by_android_uiautomator('new UiSelector().text("小程序")').click()

            logging.info("点击我的小程序!")
            driver.find_element_by_android_uiautomator('new UiSelector().text("我的小程序")').click()

            # driver.find_element_by_android_uiautomator('new UiSelector().text("体验版")').click()



            logging.info("点击车站通小程序！")
            driver.find_element_by_android_uiautomator('new UiSelector().text("车站通")').click()
            try:
                WebDriverWait(driver, 20).until(lambda x: x.find_element_by_android_uiautomator('new UiSelector().text("更多服务")'))
            except TimeoutException:
                logging.error("没有-更多服务模块加载出来")
            except NoSuchElementException:
                logging.error("没有-更多服务模块加载出来")
            else:
                return driver


def appium_微信车站通_tmp():
    desired_caps = {}
    with open(path_项目路径() + r'config\czt_wx.yaml', 'r', encoding='utf-8') as file:
        data = yaml.load(file, Loader=yaml.FullLoader)
        desired_caps['platformName'] = data['platformName']

        desired_caps['platformVersion'] = data['platformVersion']
        desired_caps['deviceName'] = data['deviceName']
        desired_caps['udid'] = data['udid']

        desired_caps['noReset'] = data['noReset']
        # desired_caps['fullReset'] = data['fullReset']

        desired_caps['unicodeKeyboard'] = data['unicodeKeyboard']
        desired_caps['resetKeyboard'] = data['resetKeyboard']

        desired_caps['appPackage'] = data['appPackage']
        desired_caps['appActivity'] = data['appActivity']

        desired_caps['automationName'] = data['automationName']

        # desired_caps['chromeOptions'] = data['chromeOptions']
        logging.info('======启动微信======')

        driver = webdriver.Remote('http://' + str(data['ip']) + ':' + str(data['port']) + '/wd/hub', desired_caps)

        try:
            WebDriverWait(driver, 20).until(lambda x: x.find_element_by_android_uiautomator('new UiSelector().text("发现")'))
        except TimeoutException:
            logging.error("查找元素超时!")
        except NoSuchElementException:
            logging.error("微信登录后，标头元素找到不到！")

        else:
            sleep(1)
            logging.info("点击发现！")
            driver.find_element_by_android_uiautomator('new UiSelector().text("发现")').click()
            logging.info("点击小程序！")
            driver.find_element_by_android_uiautomator('new UiSelector().text("小程序")').click()





            logging.info("点击我的小程序!")
            driver.find_element_by_android_uiautomator('new UiSelector().text("我的小程序")').click()

            # driver.find_element_by_android_uiautomator('new UiSelector().text("开发版")').click()


            logging.info("点击车站通小程序！")
            driver.find_element_by_android_uiautomator('new UiSelector().text("车站通")').click()
            try:
                WebDriverWait(driver, 20).until(lambda x: x.find_element_by_id("com.tencent.mm:id/b1v"))
            except TimeoutException:
                logging.info("等待页面加载完毕\"车站头条\"")
                WebDriverWait(driver, 10).until(lambda x: x.find_element_by_android_uiautomator('new UiSelector().text("车站头条")'))
            except NoSuchElementException:
                logging.info("没有切换 站点提示!")
                logging.info("等待页面加载完毕\"车站头条\"")
                WebDriverWait(driver, 10).until(lambda x: x.find_element_by_android_uiautomator('new UiSelector().text("车站头条")'))
                return driver
            else:
                driver.find_element_by_id("com.tencent.mm:id/b1v").click()
                logging.info("等待页面加载完毕\"车站头条\"")
                WebDriverWait(driver, 10).until(lambda x: x.find_element_by_android_uiautomator('new UiSelector().text("车站头条")'))
                return driver

def appium_支付宝车站通():
    desired_caps = {}
    with open(path_项目路径() + r'config\czt_zfb.yaml', 'r', encoding='utf-8') as file:
        data = yaml.load(file, Loader=yaml.FullLoader)
        desired_caps['platformName'] = data['platformName']

        desired_caps['platformVersion'] = data['platformVersion']
        desired_caps['deviceName'] = data['deviceName']
        desired_caps['udid'] = data['udid']
        print(desired_caps)
        desired_caps['noReset'] = data['noReset']
        # desired_caps['fullReset'] = data['fullReset']


        desired_caps['unicodeKeyboard'] = data['unicodeKeyboard']
        desired_caps['resetKeyboard'] = data['resetKeyboard']

        desired_caps['appPackage'] = data['appPackage']
        desired_caps['appActivity'] = data['appActivity']

        desired_caps['automationName'] = data['automationName']

        # desired_caps['chromeOptions'] = data['chromeOptions']
        logging.info('======启动支付宝======')

        driver = webdriver.Remote('http://' + str(data['ip']) + ':' + str(data['port']) + '/wd/hub', desired_caps)

        try:
            WebDriverWait(driver, 20).until(lambda x: x.find_element_by_android_uiautomator('new UiSelector().text("我的小程序")'))
        except TimeoutException:
            logging.error("发现查找元素超时!")
        except NoSuchElementException:
            logging.error("发现按钮元素找到不到！")

        else:
            # logging.info("点击发现！")
            # driver.find_element_by_android_uiautomator('new UiSelector().text("发现")').click()
            # logging.info("点击小程序！")
            # driver.find_element_by_android_uiautomator('new UiSelector().text("小程序")').click()

            logging.info("点击我的小程序!")
            driver.find_element_by_android_uiautomator('new UiSelector().text("我的小程序")').click()
            time.sleep(6)
            # WebDriverWait(driver, 20).until(
            #     lambda x: x.find_element_by_android_uiautomator('new UiSelector().text("我的小程序")'))

            # driver.find_element_by_android_uiautomator('new UiSelector().text("体验版")').click()

            logging.info("点击车站通小程序！")
            driver.find_element_by_android_uiautomator('new UiSelector().text("车站通")').click()
            # WebDriverWait(driver, 20).until(
            #     lambda x: x.find_element_by_android_uiautomator('new UiSelector().text("车站通")'))
            try:
                WebDriverWait(driver, 20).until(lambda x: x.find_element_by_android_uiautomator('new UiSelector().text("更多服务")'))
            except TimeoutException:
                logging.error("没有-更多服务模块加载出来")
            except NoSuchElementException:
                logging.error("没有-更多服务模块加载出来")
            else:
                return driver


if __name__ == '__main__':
    driver = appium_支付宝车站通()
    # driver = appium_微信车站通()
    driver.find_element_by_id()