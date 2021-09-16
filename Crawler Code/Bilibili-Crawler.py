#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Bilibili-Crawler

import threading
import time
import sqlite3
import requests
from concurrent import futures

counter = 1
result = []
lock = threading.Lock()
conn = None
flag = None
header = {
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36'
                  '(KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'
}

def run(url):
    # 启动爬虫
    global counter
    req = requests.get(url, headers = header, timeout = 5).json()
    time.sleep(0.5) # 适当延时，防止爬虫过早被反爬
    try:
        data = req['bilibili']
        video = (
            counter,
            data['aid'],        # 视频序号
            data['view'],       # 播放数
            data['danmaku'],    # 弹幕数
            data['reply'],      # 评论数
            data['favorite'],   # 收藏数
            data['coin'],       # 投币数
            data['share'],      # 分享数
            ""                  # 视频名称功能尚未实现
        )
        with lock:
            result.append(video)
            if counter % 250 == 0:
                global time0
                time1 = time.time()
                print("目前已完成网页爬取{0}个 ，总时间:{1:.2f}s".format(
                    counter, time1-time0))
        counter += 1
    except:
        pass

def create():
    # 创建数据库
    global conn
    conn = sqlite3.connect('bilibili-video.db')
    conn.execute("""create table if not exists bilibili
                    (id int prinmary key autocrement,
                    aid int,
                    view int,
                    danmaku int,
                    reply int,
                    favorite int,
                    coin int,
                    share int,
                    name str)"""
    )

def save():
    # 写入数据库
    global result, conn, flag, counter
    sqlwrite = "insert into bilibili \
             values(?,?,?,?,?,?,?,?,?);"
    for row in result:
        try:
            conn.execute(sqlwrite, row)
        except:
            conn.rollback()
            flag = "Error occurs in number "+str(counter)
            pass
    conn.commit()
    result = []

if __name__ == "__main__":
    create()
    time0 = time.time()
    print("爬虫启动，开始抓取数据")
    for i in range(0, 2800):
        begin = 10000*i
        urls = [
        	"http://api.bilibili.com/archive_stat/stat?aid={}".format(j)
            # 因未知原因网页控制台获取的 API(http://api.bilibili.com/x/web-interface/archive/stat?aid={}) 抓取效率过低，改用网友提供的 API
                for j in range(begin, begin+10000)
        ]
        with futures.ThreadPoolExecutor(64) as executor:
            executor.map(run,urls)
        # 多线程抓取，提高爬虫效率
        save()
    if flag != None:
        print(flag)
        flag = None
    else:
    	print("爬虫结束，共抓取了{}条数据".format(counter))
    conn.close()
