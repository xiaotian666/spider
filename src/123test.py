#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: xiaotian

import os


def replace_colon():
    with open('./123.txt', 'r+') as data:
        with open('./result.txt', 'w+') as result:
            for data1 in data.readlines():
                # str_data = data.read()
                data1 = data1.decode('gbk').encode('utf-8')
                result.write(data1.replace('：', ':').decode('utf-8').encode('gbk'))
                # print(str_data)


def root_sum(n):
    return (n - 1) % 9 + 1


if __name__ == '__main__':
    # replace_colon()
    print(root_sum(4))
