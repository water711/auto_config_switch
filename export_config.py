# -*- coding : utf-8 -*-

'''
批量导出交换机配置
'''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import time


UserName = 'admin'
Password = 'admin@huawei.com'

def open_browser(ip):
    #新建options
    options = webdriver.ChromeOptions()

    #添加选项，禁止在控制台打印日志
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    #添加选项，忽略网站SSL证书错误
    options.add_argument('--ignore-certificate-errors')

    #设置浏览器下载文件默认保存路径
    path = 'F:\\config\\' + ip
    prefs = {'profile.default_content_settings.popups': 0, 'download.default_directory': path}
    options.add_experimental_option('prefs', prefs)

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
 
def export_config(ip,driver):
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

    #输入密码
    submit = WebDriverWait(driver,999).until(lambda driver: driver.find_element_by_id('goBtn'))
    submit.click()

    time.sleep(7)

    #点击维护
    maintenance = WebDriverWait(driver,999).until(lambda driver: driver.find_element_by_id('maintenance'))
    maintenance.click()

    time.sleep(7)

    #点击系统管理
    lswSysManager = WebDriverWait(driver,999).until(lambda driver: driver.find_element_by_id('lswSysManager'))
    lswSysManager.click()
    
    time.sleep(9)

    #搜索文件
    uinp_searchFileComboInput = WebDriverWait(driver,999).until(lambda driver: driver.find_element_by_id('uinp_searchFileComboInput'))
    uinp_searchFileComboInput.send_keys("vrpcfg")

    #模拟键盘回车按键
    ActionChains(driver).send_keys(Keys.ENTER).perform()
    
    time.sleep(1)

    #点击下载
    tableTDContentfileOperate_0 = WebDriverWait(driver,999).until(lambda driver: driver.find_element_by_xpath('//*[@id="tableTDContentfileOperate_0"]/img'))
    tableTDContentfileOperate_0.click()
    
    time.sleep(3)

    print("保存成功")
    driver.quit()


with open('ip.txt','r') as f:
    while 1:
        ip = f.readline().strip('\n')
        if not ip:
            break
        driver = open_browser(ip)
        export_config(ip,driver)