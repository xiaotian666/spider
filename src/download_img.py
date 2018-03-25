# -*- coding: utf-8 -*-
'''
@author: jerry
@file: download_img.py
@time: 2018-02-27 15:14
'''
import requests
from bs4 import BeautifulSoup
import re
import os
import time


def get_page_num(url):
    html = requests.get(url, headers=headers)
    soup = BeautifulSoup(html.text, 'lxml')
    page_list = list(soup.find_all('div', id='wp_page_numbers'))
    tmp_list = []
    for i in page_list:
        tmp_list.append(i.get_text())
    tmp_2 = str(tmp_list[0]).strip().split('\n')
    return tmp_2[-3]


def get_page(url, page=1):
    html = requests.get(url.format(page), headers=headers)
    html.encoding = 'gbk'
    soup = BeautifulSoup(html.text, 'lxml')
    data = list(soup.find_all('div', id='picture'))
    url_list = []
    j = 0
    for i in data:
        tmp_list = [i.a.get('href'), i.a.get('title')]
        url_list.append(tmp_list)
    print('共找到', len(url_list), '个URL')
    find_img(url_list)
    return 1


def find_img(url_list):
    j = 0
    for i, k in url_list:
        html = requests.get(i, headers=headers)
        soup = BeautifulSoup(html.text, 'lxml')
        data = str(soup.find('div', {'id': 'picture'}))
        soup_1 = BeautifulSoup(data, 'lxml')
        img_data = soup_1.find_all('img')
        j += 1
        print('第%s个URL' % j)
        img_j = 0
        folder = ['OOXX', k]
        folder_create(folder)
        for img_i in img_data:
            img_j += 1
            print('第%s张图片' % img_j, end=': ')
            save_img(folder, img_url=img_i.get('src'))
        time.sleep(3)
    return 1


def folder_create(folder):
    if not os.path.exists(folder[0]):
        try:
            os.mkdir(folder[0])
        except OSError:
            print('创建失败')
    else:
        if not os.path.exists(folder[0] + '/' + folder[1]):
            try:
                os.mkdir(folder[0] + '/' + folder[1])
            except OSError:
                print('创建失败')
        else:
            print('目录已存在')


def save_img(folder, img_url):
    html = requests.get(img_url, headers=headers)
    file_name = re.match(r'^https?://[^/]+/.+?/([^/]+)$', img_url)
    print(folder[0] + '/' + folder[1] + '/' + file_name.group(1), end=' -> ')
    with open('{}/{}/{}'.format(folder[0], folder[1], file_name.group(1)), 'wb') as file:
        file.write(html.content)
        print('保存成功')
    return 1


if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36'}
    url = 'http://www.meizitu.com/'
    print('共有%s页' % get_page_num(url))
    page = int(input('请输入获取页数: '))
    if page >= 1:
        page += 1
        for i in range(1, page):
            get_page(url, i)
    else:
        page = input('输入有误, 请重新输入页号: ')
        get_page(url, page)
    print('运行完毕')
