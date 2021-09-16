#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Bilibili-Video-Name-WordCloud

import jieba
import wordcloud
from imageio import imread

mask = imread("background.png")
#mask = imread("bilibili-tv.jpeg")
excludes = { }

f = open("output.txt", "r", encoding="utf-8")
t = f.read()
f.close()
print("File loaded")

print("Task Started")
ls = jieba.lcut(t)
txt = " ".join(ls)
w = wordcloud.WordCloud(\
    width = 1000, height = 563,\
    #width 400 and height 200 pixels by default
    background_color = "white",#black by default
    font_path = "sarasa-gothic-sc-semibold.ttf",
    #min_font_size = 10,#4 by default
    #max_font_size = 20,#adjust by height by default
    #font_step = 2,#1 by default
    max_words = 400,#200 by default
    mask = mask
    )
w.generate(txt)
w.to_file("Bilibili-video-name-wordcloud.png")
print("Task Ended")
