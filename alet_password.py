# -*- coding : utf-8 -*-

'''
批量修改交换机密码
'''

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time


UserName = 'admin'
OldPassword = 'admin@huawei.com'
NewPassword = 'newpassword123'


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
 
def change_password(ip):
    print(ip)
    driver.get("http://" + ip)

    alert_confirm()  #确认弹框

    #窗口最大化
    driver.maximize_window() 

    #输入账号
    username = WebDriverWait(driver,999).until(lambda driver: driver.find_element_by_id('UserName'))
    username.send_keys(UserName)

    #输入密码
    pwd = WebDriverWait(driver,999).until(lambda driver: driver.find_element_by_id('userPassword'))
    pwd.send_keys(OldPassword)

    #点击登录
    submit = WebDriverWait(driver,999).until(lambda driver: driver.find_element_by_id('goBtn'))
    submit.click()

    time.sleep(6)

    #点击维护
    maintenance = WebDriverWait(driver,999).until(lambda driver: driver.find_element_by_id('maintenance'))
    maintenance.click()

    time.sleep(6)

    #点击管理员
    lswUser = WebDriverWait(driver,999).until(lambda driver: driver.find_element_by_id('lswUser'))
    lswUser.click()

    time.sleep(2)

    #点击第1个账号
    tableTDContentuserName_0 = WebDriverWait(driver,999).until(lambda driver: driver.find_element_by_id('tableTDContentuserName_0'))
    tableTDContentuserName_0.click()

    time.sleep(2)

    #输入旧密码
    uinp_oldPassword = WebDriverWait(driver,999).until(lambda driver: driver.find_element_by_id('uinp_oldPassword'))
    uinp_oldPassword.send_keys(OldPassword)

    #输入新密码
    uinp_newPassword = WebDriverWait(driver,999).until(lambda driver: driver.find_element_by_id('uinp_newPassword'))
    uinp_newPassword.send_keys(NewPassword)

    #再次输入新密码
    uinp_confirmPassword = WebDriverWait(driver,999).until(lambda driver: driver.find_element_by_id('uinp_confirmPassword'))
    uinp_confirmPassword.send_keys(NewPassword)

    #保存密码修改
    btn_okDiv_uBtn = WebDriverWait(driver,999).until(lambda driver: driver.find_element_by_id('btn_okDiv_uBtn'))
    btn_okDiv_uBtn.click()

    time.sleep(1)

#打开浏览器
driver = open_broswer()

#遍历txt文件的ip地址
with open('ip.txt','r') as f:
    while 1:
        ip = f.readline().strip('\n')
        if not ip:
            break
        change_password(ip)  #执行函数，修改交换机密码