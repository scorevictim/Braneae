#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Bilibili-Video-Name-Crawler

import pandas as pd
import os
import requests
import pyquery

# 读取文件
path = os.getcwd()+'/Coin_Descending.csv' # MacOS / Linux
#path = os.getcwd()+'\\Coin_Descending.csv' # Windows
f = open(path, encoding='utf-8')
df = pd.read_csv(f)

# 检测数据格式
#print(type(df))

counter = 0
content = ""
aids = 0
name = ""
flag = None
header = {
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36'
                  '(KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'
}

# 创建文件用于保存视频名，便于后续分词
f = open('name_output.txt','a')
f.write('name')
f.close()

# 获取视频名并存入 TXT 文件
for counter in range(150):
    video_aid = df.loc[df.index[counter],'aid']
    url = "https://www.bilibili.com/video/av" + str(video_aid)
    req = requests.get(url.format(video_aid), headers=header, timeout=5).text
    q = pyquery.PyQuery(req)
    video_name =  q("h1[title]").text()
    #print(video_name) # 测试输出
    f = open('name_output.txt','a')
    content = '\n' + video_name
    f.write(content)
    f.close()

print("Task ended.")