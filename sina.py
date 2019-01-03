#!/usr/bin/python
# -*- coding: UTF-8 -*-

from topic import get_topic
from realtimehot import get_realtimehot
from relevantTopic import get_relevant_topic
from sqlite import insert, select
import time


def main():
    key = "南昌大学"
    realtimehot = get_realtimehot()
    topic = get_topic(key)
    users, relevant_topic, words = get_relevant_topic(key)
    print("-------------Get函数结束-------------")
    print("即时热榜"+str(realtimehot))
    print(key+"搜索到的话题"+str(topic))
    print(key+"话题内微博相关话题"+str(relevant_topic))
    print(key+"话题内活跃用户"+str(users))
    print(key+"话题内博文常见关键词"+str(words))
    insert(realtimehot, topic, relevant_topic, users, words)

if __name__ == '__main__':
  while True:
      main()
      time.sleep(60)
