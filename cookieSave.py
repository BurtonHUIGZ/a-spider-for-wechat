# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from selenium import webdriver
import time
import json

driver = webdriver.Chrome()
driver.get('https://mp.weixin.qq.com/')
#清空账号栏
driver.find_element_by_xpath('//*[@id="header"]/div[2]/div/div/form/div[1]/div[1]/div/span/input').clear()
driver.find_element_by_xpath('//*[@id="header"]/div[2]/div/div/form/div[1]/div[1]/div/span/input').send_keys('1454914075@qq.com')
time.sleep(2)
#清空密码框，输入密码
driver.find_element_by_xpath('//*[@id="header"]/div[2]/div/div/form/div[1]/div[2]/div/span/input').clear()
driver.find_element_by_xpath('//*[@id="header"]/div[2]/div/div/form/div[1]/div[2]/div/span/input').send_keys('thisisnotlove@.')
#点击记住密码
time.sleep(2)
driver.find_element_by_xpath('//*[@id="header"]/div[2]/div/div/form/div[3]/label/i').click()
#点击登陆
driver.find_element_by_xpath('//*[@id="header"]/div[2]/div/div/form/div[4]/a').click()
#让程序睡眠10秒
time.sleep(15)
#获取登陆后的cookies
cookies = driver.get_cookies()

cookie = {}

for items in cookies:
    cookie[items.get('name')] = items.get('value')

with open('cookies.txt','w') as file:
    file.write(json.dumps(cookie))

driver.close()
driver.quit()





