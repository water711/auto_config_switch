# -*- coding : utf-8 -*-

'''
批量修改交换机密码
'''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import time


UserName = 'admin'
Password = 'admin@huawei.com'
log_host_ip = '192.168.1.225'  #日志主机IP

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
 
def add_log_host(ip):
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

    time.sleep(7)

    #点击维护
    maintenance = WebDriverWait(driver,999).until(lambda driver: driver.find_element_by_id('maintenance'))
    maintenance.click()

    time.sleep(5)

    #点击日志
    lswLogManager = WebDriverWait(driver,999).until(lambda driver: driver.find_element_by_id('lswLogManager'))
    lswLogManager.click()
    
    time.sleep(2)

    #点击参数配置
    parameterConfig_tab = WebDriverWait(driver,999).until(lambda driver: driver.find_element_by_id('parameterConfig_tab'))
    parameterConfig_tab.click()

    #点击添加日志主机
    add_btn_uBtn = WebDriverWait(driver,999).until(lambda driver: driver.find_element_by_id('add_btn_uBtn'))
    add_btn_uBtn.click()

    time.sleep(1)
    ActionChains(driver).send_keys(log_host_ip).perform()

    #点击确定
    btnObj_1 = WebDriverWait(driver,999).until(lambda driver: driver.find_element_by_id('btnObj_1'))
    btnObj_1.click()

    time.sleep(1)

    #再次点击确定
    tipBtn = WebDriverWait(driver,999).until(lambda driver: driver.find_element_by_id('tipBtn'))
    tipBtn.click()
    
    time.sleep(1)

    #点击保存配置
    try:
        save = WebDriverWait(driver,3).until(lambda driver: driver.find_element_by_id('save'))
        save.click()
    except:
        sysSaveDiv_uBtn = WebDriverWait(driver,999).until(lambda driver: driver.find_element_by_id('sysSaveDiv_uBtn'))
        sysSaveDiv_uBtn.click()

    time.sleep(1)

    #确认保存配置
    wconfirmBtn = WebDriverWait(driver,999).until(lambda driver: driver.find_element_by_id('wconfirmBtn'))
    wconfirmBtn.click()

    time.sleep(3)

#打开浏览器
driver = open_broswer()

#遍历txt文件的ip地址
with open('ip.txt','r') as f:
    while 1:
        ip = f.readline().strip('\n')
        if not ip:
            break
        add_log_host(ip)