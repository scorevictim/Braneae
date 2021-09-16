#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Bilibili-Video-Data-Visualization

import pandas as pd
import os
import matplotlib.pyplot as plt

#path = os.getcwd()+'/Aid_Ascending.csv' # MacOS / Linux
path = os.getcwd()+'/result.csv' # MacOS / Linux
#path = os.getcwd()+'\\result.csv' # Windows
f = open(path, encoding='utf-8')
print("File loaded")

#print(type(df))

# 制作视频序号与播放量关系的折线图
col = ['aid','view']
df0 = pd.DataFrame(pd.read_csv(f),columns = col)
#print(df0)
print("Task Started")
df0.plot(x = 'aid',y = 'view',title = 'Bilibili Video Aid x View Relationship')
plt.xlabel('aid')
plt.ylabel('view')
print("Task Ended")
plt.show()

# 制作视频收藏数与播放量关系的散点图(点的大小随数据大小变化)
col = ['favorite','view','share']
df1 = pd.DataFrame(pd.read_csv(f),columns = col)
#print(df1)
print("Task Started")
df1.plot.scatter(x='favorite',y='view',color='grey',s=df1['share']/20,title='Bilibili Video Favotite x View Relationship')
print("Task Ended")
plt.show()

# 制作视频收藏数、分享数与播放量关系的叠加散点图
col = ['favorite','view','share']
df2 = pd.DataFrame(pd.read_csv(f),columns = col)
#print(df2)
print("Task Started")
ax = df2.plot.scatter(x='favorite',y='view',color='grey',label='favorite',title='Bilibili Video Favotite & Share x View Relationship')
df2.plot.scatter(x='share',y='view',color='blue',label='share',ax=ax)
print("Task Ended")
plt.show()
