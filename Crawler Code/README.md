# Bilibili 视频信息爬虫

## 开发环境

Debian 10 + Chromium + Python 3.7 + VSCodium 1.40.0 (VS Code 衍生版本) 

## Python 依赖包

requests

## 获取 Bilibili API

使用浏览器打开 Bilibili 网站，点开任意视频，以 [共青团中央这个视频](https://www.bilibili.com/video/av57423406) 为例，打开开发者工具，选择 Network 选项，勾选 JS，刷新页面，通过对 Header 的分析可以得到 API 的上一级域名 https://api.bilibili.com/x/web-interface/archive/ ， 再通过对 tags, show, locs 等 JS 的分析结合猜测，得出 API 的网址 https://api.bilibili.com/x/web-interface/archive/stat?aid=57423406 ，由于 aid 即 Bilibili 视频的 av 号，判断可以通过枚举抓取视频信息。

## 爬虫原理

通过得到的 API，利用多线程，通过 requests 不断获取数据，爬取后利用 Python 自带的 SQLite 将数据存入数据库，方便后续处理。
