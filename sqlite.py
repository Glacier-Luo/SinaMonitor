#!/usr/bin/python

import sqlite3
# try:
#     import cPickle as pickle
# except ImportError:
#     import pickle
import sys, json
sys.setrecursionlimit(10 ** 5)  # set the maximum depth as 10的10次方

def create_database():
    conn = sqlite3.connect('sina.db')
    print("Opened database successfully")
    c = conn.cursor()
    # c.execute('''CREATE TABLE realtimehot
    #        (ID INTEGER PRIMARY KEY    autoincrement,
    #        TIME           TIMESTAMP NOT NULL DEFAULT (datetime('now','localtime')),
    #        DATA           TEXT    NOT NULL);''')
    c.execute('''CREATE TABLE realtimehot
           (ID INTEGER PRIMARY KEY    autoincrement,
           TIME           TIMESTAMP NOT NULL DEFAULT (strftime('%s','now')),
           DATA           TEXT    NOT NULL);''')
    c.execute('''CREATE TABLE topic
               (ID INTEGER PRIMARY KEY    autoincrement,
               TIME           TIMESTAMP NOT NULL DEFAULT (strftime('%s','now')),
               DATA           TEXT    NOT NULL);''')
    c.execute('''CREATE TABLE relevant_topic
               (ID INTEGER PRIMARY KEY    autoincrement,
               TIME           TIMESTAMP NOT NULL DEFAULT (strftime('%s','now')),
               DATA           TEXT    NOT NULL);''')
    c.execute('''CREATE TABLE users
               (ID INTEGER PRIMARY KEY    autoincrement,
               TIME           TIMESTAMP NOT NULL DEFAULT (strftime('%s','now')),
               DATA           TEXT    NOT NULL);''')
    c.execute('''CREATE TABLE words
               (ID INTEGER PRIMARY KEY    autoincrement,
               TIME           TIMESTAMP NOT NULL DEFAULT (strftime('%s','now')),
               DATA           TEXT    NOT NULL);''')
    print("Table created successfully")
    conn.commit()
    conn.close()

def insert(realtimehot, topic, relevant_topic, users, words):
    conn = sqlite3.connect('sina.db')
    c = conn.cursor()
    print("Opened database successfully")

    c.execute("INSERT INTO realtimehot (DATA) \
          VALUES ('{data}')".format(data=json.dumps(realtimehot)))
    c.execute("INSERT INTO topic (DATA) \
              VALUES ('{data}')".format(data=json.dumps(topic)))
    c.execute("INSERT INTO relevant_topic (DATA) \
              VALUES ('{data}')".format(data=json.dumps(relevant_topic)))
    c.execute("INSERT INTO users (DATA) \
              VALUES ('{data}')".format(data=json.dumps(users)))
    c.execute("INSERT INTO words (DATA) \
              VALUES ('{data}')".format(data=json.dumps(words)))

    conn.commit()
    print("Records created successfully")
    conn.close()


def select(table):
    conn = sqlite3.connect('sina.db')
    c = conn.cursor()
    # print("Opened database successfully")
    data = {}
    cursor = c.execute("SELECT TIME, DATA  from {table}".format(table=table))
    for row in cursor:
        # print("TIME = ", row[0])
        # print("DATA = ", json.loads(row[1]), "\n")
        data[row[0]] = json.loads(row[1])

    # print("Operation done successfully")
    conn.close()
    return data

# create_database()
# insert('test')
select("realtimehot")