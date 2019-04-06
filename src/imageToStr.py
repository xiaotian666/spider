#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: xiaotian

from PIL import Image

# table1 = """$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,"^`''. """#这种方法好像不太好
table = '#8XOHLTI)i=+;:,. '  # 对于灰度图像效果不错
im = Image.open("./1.jpg")
if im.mode != "L":  # 如果不是灰度图像，转换为灰度图像
    im = im.convert("L")
a = im.size[0]
b = im.size[1]
im = im.resize((200, 266))  # 转换图像大小，这个大小是我随意设置的
f = open("./image.txt", 'w+')  # 目标文本文件

for i in range(1, b, 2):  # 每隔一行取一行像素，是为了保持视觉上的横纵比
    line = ''
    for j in range(a):
        line += table[int((float(im.getpixel((j, i))) / 256.0) * len(table))]  # 计算当前像素属于哪个字符
    line += "\n"  # 别忘了添加回车符
    f.write(line)
f.close()