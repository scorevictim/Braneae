# Bilibili 视频数据可视化

## 开发环境

Debian 10 + Python 3.7 + VSCodium 1.40.0(VS Code 衍生版本)

## Python 依赖包

pandas
matplotlib

## 可视化原理

利用 pandas 读取指定列的数据并将数据转换成 DataFrame，便于后续数据可视化，利用 matplotlib 根据不同视频数据进行绘图，示例中给出了三张图的源码，实际中可以很方便地通过调整读取的视频数据和需要的图表格式进行拓展。
