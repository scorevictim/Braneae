# Bilibili 视频数据排序

## 开发环境

Debian 10 + Python 3.7 + VSCodium 1.40.0(VS Code 衍生版本) 

## Python 依赖包

pandas
requests

## 排序原理

利用 Pandas 读取已经按照不同指标做好排序的数据库（此时无视频名），将排序后前 150 行的数据存入数据库，通过爬虫抓取视频名，并将视频名数据保存至 TXT 文件导入完成排序的数据库，利用[网络工具](http://www.tablesgenerator.com/markdown_tables)将 CSV 文件转为 Markdown 文件，便于后续网站展示，同时生成包含前 150 个视频名的文件，便于后续分词与数据可视化。
