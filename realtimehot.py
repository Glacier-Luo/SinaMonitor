#!/usr/bin/python
# -*- coding: UTF-8 -*-

import requests
from bs4 import BeautifulSoup

def get_realtimehot():
    realtimehot = {}
    url = 'https://s.weibo.com/top/summary?cate=realtimehot'
    result = requests.get(url)
    # print(result.text)
    soup = BeautifulSoup(result.text)
    result = soup.find_all("td", class_="td-02")
    for td in result:
        # print(td.a.contents)
        if td.span == None:
            # print("置顶信息")
            realtimehot[td.a.contents[0]] = "置顶信息"
        else:
            # print(td.span.contents)
            realtimehot[td.a.contents[0]] = td.span.contents[0]
    print(realtimehot)
    return realtimehot
    # print(result)


# get_realtimehot()

