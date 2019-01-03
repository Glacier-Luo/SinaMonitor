#!/usr/bin/python
# -*- coding: UTF-8 -*-

import requests, re, jieba, operator
from bs4 import BeautifulSoup
from htmlRe import filter_tags
import jieba.posseg as pseg

def get_relevant_topic(topic):
    url = ["https://s.weibo.com/weibo?q=%23{topic}%23&page={page}",
           "https://s.weibo.com/realtime?q=%23{topic}%23&rd=realtime&tw=realtime&page={page}",
           # "https://s.weibo.com/hot?q=%23{topic}%23&xsort=hot&suball=1&tw=hotweibo&page={page}",
           # "https://s.weibo.com/video?q=%23{topic}%23&xsort=hot&hasvideo=1&tw=video&page={page}"
           ]
    users = {}
    relevant_topic = {}
    words = {}
    stop_words = set(line.strip() for line in open('stopwords.txt', encoding='utf-8'))
    for u in url:
        for num in range(1, 50):
            print("正在爬取第{num}页".format(num=num))
            result = requests.get(u.format(topic=topic, page=num))
            soup = BeautifulSoup(result.text)
            result = soup.find_all("p", class_="txt")
            for text in result:
                # print(text)
                try:
                    users[text['nick-name']] += 1
                except KeyError:
                    try:
                        users[text['nick-name']] = 1
                    except KeyError:
                        pass
                else:
                    pass

                text = filter_tags(str(text))
                topics = re.findall("#.*?#", text)
                for top in topics:
                    try:
                        relevant_topic[top] += 1
                    except KeyError:
                        relevant_topic[top] = 1
                word_list = pseg.cut(''.join(text))
                for word, flag in word_list:
                    if not word in stop_words and flag == 'n':
                        try:
                            words[word] += 1
                        except KeyError:
                            try:
                                words[word] = 1
                            except KeyError:
                                pass
                        else:
                            pass

                # print(relevant_topic)
                # print(text)
                # print("----------------分割线----------------")
        # print("下一栏目！")
    # users = sorted(users.items(), key=operator.itemgetter(1))
    # relevant_topic = sorted(relevant_topic.items(), key=operator.itemgetter(1))
    # words = sorted(words.items(), key=operator.itemgetter(1))
    # print(dict(users))
    # print(dict(relevant_topic))
    # print(dict(words))
    print(users)
    print(relevant_topic)
    print(words)
    return users, relevant_topic, words

# get_relevant_topic("南昌大学")