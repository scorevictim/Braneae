#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Bilibili-Video-Sort-Encode

import pandas as pd
import os

# 读取文件
path = os.getcwd()+'/result.csv' # MacOS / Linux
#path = os.getcwd()+'\\result.csv' # Windows
f = open(path, encoding='utf-8')
df = pd.read_csv(f)

# 检测数据格式
#print(type(df))

# 读取前 10000 条数据并输出成 GBK 编码，便于 Windows 用户在 Office Excel 中查看和处理数据
headdata = df.head(10000)
df = pd.DataFrame(headdata)
df.to_csv('encode_result.csv',encoding = 'gbk')
