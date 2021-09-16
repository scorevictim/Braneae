# Bilibili 视频名分词与词云制作

## 开发环境

Debian 10 + Python 3.7 + VSCodium 1.40.0(VS Code 衍生版本) + GIMP(开源图像编辑软件)

## Python 依赖包

jieba
wordcloud
imageio
matplotlib

## 分词原理

利用 Jieba 进行分词，便于后续制作词云和数据可视化图表。

## 词云原理

利用 WordCloud 制作词云，同时利用 GIMP 在生成的词云图上方叠加一层 15% 透明度的原图，增强视觉效果。
