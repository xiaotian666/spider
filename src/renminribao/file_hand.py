#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: xiaotian

import os

# import sys
# reload(sys)
import re


def file_hand(file_path):
    file_path_list = os.listdir(file_path)
    # print(file_path_list)
    string_files = ''
    for i in list(file_path_list):
        # print(i)
        file_name_list = os.listdir(file_path + '/' + i)
        for file_name in file_name_list:
            with open(file_path + '/' + i + '/' + file_name, 'r+') as files:
                # print(files.readlines())
                string_file = files.read()
                string_files += string_file
                string_hand(string_files)


def string_hand(strings):
    # s = strings
    s = re.sub("[\s+\.\!\/_,$%^*(+\"\']+|[+——！，。？、~@#￥%……&*（）]+", "", strings)
    file_str = ''
    # 创建一个字典用来保存字符的个数
    d = {}
    for ch in s:
        # 先判断这个字符以前是否出现过
        if ch not in d:  # 第一次出现
            d[ch] = 1  # 将次数设置为1，创建 键值对
        else:  # 不是第一次出现，更新值，即次数
            d[ch] += 1

    # 打印字符和出现过的次数，键为字符，值为对应的次数
    for k in d:
        file_str += str(k) + ':\t' + str(d[k]) + '\n'
        print(k, ':\t', d[k])

    # 将结果写入到文件
    with open('result.txt', 'w+', encoding='utf-8') as result:
        result.write(file_str)


if __name__ == '__main__':
    file_hand('./files')
