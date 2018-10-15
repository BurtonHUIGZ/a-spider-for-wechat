# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 21:17:31 2018

@author: Administrator
"""

import requests
import re
import random
import json
import time
from fake_useragent import UserAgent


query = input('请输入要搜索的公众号:')
ua =UserAgent()
with open('cookies.txt','r') as f:
    cookie = f.read()

url = 'https://mp.weixin.qq.com'
headers = {
        'User-Agent':ua.random,
        'Referer':'https://mp.weixin.qq.com/cgi-bin/appmsg?t=media/appmsg_edit_v2&action=edit&isNew=1&type=10&share=1&token=1269703924&lang=zh_CN',
        'Host':'mp.weixin.qq.com',
        }
cookies = json.loads(cookie)
#使用get请求访问页面，参数为登陆后的参数
response = requests.get(url,cookies = cookies)


token = re.findall(r'token=(\d+)',str(response.url))[0]

data = {
        'token': token,
        'lang': 'zh_CN',
        'f': 'json',
        'ajax': '1',
        'random': random.random(),#返回o-1之间的随机数
        'url': query,
        'begin': '0',
        'count': '3',
        }
#文本输入开框的请求地址
search_url = 'https://mp.weixin.qq.com/cgi-bin/operate_appmsg?sub=check_appmsg_copyright_stat'
search_response = requests.post(search_url,cookies = cookies, data = data, headers = headers)
print(search_response.text)
content = search_response.json().get('list')
print(content)
count = search_response.json().get('total')
print(count)
#计算出总页数
num = int(count/3)
print('一共有',num,'页')
begin = 3
for i in range(num):
    print('第',i+1,'页')
    data = {
        'token': token,
        'lang': 'zh_CN',
        'f': 'json',
        'ajax': '1',
        'random': random.random(),#返回o-1之间的随机数
        'url': query,
        'begin': begin*i,
        'count': '3',
        }
    search_response = requests.post(search_url,cookies = cookies, data = data, headers = headers) 
    try:
        content = search_response.json().get('list')
    except Exception as e:
        print(e,':没有取到数据')
        continue
    for body in content:
        dict = {
                '文章标题':body.get('title'),
                '所属公众号':body.get('nickname'),
                '文章作者':body.get('author'),
                '文章所属类型':body.get('article_type'),
                '文章链接地址':body.get('url'),
                }
        #将数据存入本地文件
        with open('json.txt','a',encoding='utf-8') as f:
            f.write(json.dumps(dict,ensure_ascii=False)+'\n')
    time.sleep(1)
















