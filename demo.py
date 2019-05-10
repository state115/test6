# coding=utf-8
import csv
import random
import io
from urllib import request,parse,error
import http.cookiejar
import urllib

# coding:utf-8
# 引入解析模块BS4
# from bs4 import BeautifulSoup
import re
from bs4 import BeautifulSoup

if __name__=="__main__":
    def GetWebPageSource(url,values):
        # url = "https://www.incnjp.com/thread-4578658-1-1.html"
        data = parse.urlencode(values).encode('utf-8')

        # header
        user_agent = ""#这里可以为空(但只是发送给服务器请求-服务器没有反爬虫机智前提下可以跑通)；如果服务器有反爬虫，那么我们这里需要写浏览器相关的代理信息（即反反爬虫机制）
        headers = {'User-Agent': user_agent, 'Connection': 'keep-alive'}

        # 声明cookie 声明opener
        cookie_filename = 'cookie.txt'
        cookie = http.cookiejar.MozillaCookieJar(cookie_filename)
        handler = urllib.request.HTTPCookieProcessor(cookie)
        opener = urllib.request.build_opener(handler)

        # 声明request
        request = urllib.request.Request(url, data, headers)
        # 得到响应
        response = opener.open(request)
        html = response.read().decode('utf-8')
        # 保存cookie
        cookie.save(ignore_discard=True, ignore_expires=True)

        return html


    url = "http://demo.pingnanlearning.com/test/login/index.php"

    values = {"username": "sasa",
            "password": "123",
            "phone2": ""
            }
    html = GetWebPageSource(url,values)

    # 判断登陆成功与否
    isLogin = False

    soup = BeautifulSoup(html, "lxml")
    hrefList = soup.select('a[target="_blank"]')
    for m in hrefList:
        if m.text == "个人中心":
            isLogin = True
    if isLogin:
        print("小sasa登陆成功!")
    else:
        print("小sasa登陆失败!")
    # print(html)