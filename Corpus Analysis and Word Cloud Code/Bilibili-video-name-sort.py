#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Bilibili-Video-Name-Sort

import jieba

# 读取文件
f = open("output.txt","r",encoding='utf-8')
txt = f.read()
f.close()

ls = jieba.lcut(txt)
count = {}
excludes = { }

for word in ls:
    if len(word) == 1:
        continue
    #elif word == "诸葛亮" or word == "孔明曰":
        #rword = "孔明"
    else:
        rword = word
    count[rword] = count.get(rword,0) + 1
for word in excludes:
    del count[word]
items = list(count.items())
items.sort(key=lambda x:x[1], reverse=True) 
for i in range(50):
    word, count = items[i]
    print ("{0:<50}{1:>5}".format(word, count))
