# -*- coding : utf-8 -*-

'''
批量保存交换机配置
'''

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time,datetime


UserName = 'admin'
Password = 'admin@huawei.com'

def open_broswer():
    #新建options
    options = webdriver.ChromeOptions()

    #添加选项，禁止在控制台打印日志
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    #添加选项，忽略网站SSL证书错误
    options.add_argument('--ignore-certificate-errors')

    #载入options并启动浏览器
    driver=webdriver.Chrome(options=options)
    return driver

def alert_confirm():
    '''
        解决以下页面弹框提示
        Web网管支持的Chrome浏览器版本范围为:Chrome 54 ~ Chrome 66,为了更好的浏览体验,建议您使用Chrome 66版本浏览器
    '''
    try:
        alert = driver.switch_to.alert   #切换到弹框窗口
        alert.text
        driver.switch_to.alert.accept()  #确认弹框
    except:
        pass
 
def save_config(ip):
    print(ip)
    driver.get("http://" + ip)

    alert_confirm()  #确认弹框

    driver.maximize_window() #窗口最大化

    #输入账号
    username = WebDriverWait(driver,999).until(lambda driver: driver.find_element_by_id('UserName'))
    username.send_keys(UserName)

    #输入密码
    pwd = WebDriverWait(driver,999).until(lambda driver: driver.find_element_by_id('userPassword'))
    pwd.send_keys(Password)

    #点击登录
    submit = WebDriverWait(driver,999).until(lambda driver: driver.find_element_by_id('goBtn'))
    submit.click()

    time.sleep(10)   #登录完成后，需要等待7-8秒，才能保存，否则会提示系统正在加载，请稍后再试

    #点击保存配置(交接机系统有两个版本，保存按钮的id不同，使用异常处理兼容两个版本)
    try:
        save = WebDriverWait(driver,3).until(lambda driver: driver.find_element_by_id('save'))
        save.click()
    except:
        sysSaveDiv_uBtn = WebDriverWait(driver,999).until(lambda driver: driver.find_element_by_id('sysSaveDiv_uBtn'))
        sysSaveDiv_uBtn.click()

    time.sleep(1)

    #点击确认保存配置
    wconfirmBtn = WebDriverWait(driver,999).until(lambda driver: driver.find_element_by_id('wconfirmBtn'))
    wconfirmBtn.click()

    #等待保存完成
    wconfirmBtn = WebDriverWait(driver,9999).until(lambda driver: driver.find_element_by_id('tipBtn'))
    wconfirmBtn.click()

    print("保存成功")

#打开浏览器
driver = open_broswer()

#遍历txt文件的ip地址
with open('ip.txt','r') as f:
    while 1:
        ip = f.readline().strip('\n')
        if not ip:
            break
        save_config(ip)   #执行函数，保存交换机配置