#!/usr/bin/python
# -*- coding: UTF-8 -*-

import requests
from bs4 import BeautifulSoup

def get_topic(topic):
    url = "https://s.weibo.com/topic?q={topic}&pagetype=topic&Refer=index".format(topic=topic)
    result = requests.get(url)
    # print(result.text)
    soup = BeautifulSoup(result.text)
    result = soup.find_all("div", class_="info")
    topic = {}
    for div in result:
        # print(div.a.contents)
        # print(div.p.next_sibling.next_sibling.contents)
        topic[div.a.contents[0]] = div.p.next_sibling.next_sibling.contents[0]
        # for child in div.children:
        #     print(child)
    print(topic)
    return topic

# get_topic("南昌大学")
