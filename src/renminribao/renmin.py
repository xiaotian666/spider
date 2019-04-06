#!/usr/bin/env python
# encoding: utf-8
'''
@author: baiganggang
@file: renmin.py
@time: 2019/3/21 9:58
'''
import os

import bs4
import requests
import chardet


class CrawlerRenmin():
    def __init__(self, url):
        self.url = url

    # 人民日报重要言论库子集
    # 49179 社论，49205 任中平，49217 评论员，49219 人民时评，385787 人民观点，54773 望海楼，49221 今日谈，49220 人民论坛，230317 宣言，
    # 114823 钟祖文，166121 来论，49222 国际论坛，49224 经济时评，69963 国际评，49223 国际随笔，80638 新语，49227 其他
    gb_list = [49179, 49219, 49205, 49217, 385787, 54773, 49221, 49220, 230317, 114823, 166121, 49222, 49224, 69963,
               49223, 80638, 49227]
    gb_url_list = []
    gb_text = []
    url_dict = {}

    # 获取网页信息
    def get_response(self, url):
        try:
            response = requests.get(url)
            # response.encoding = 'gb2312'
        except Exception:
            print('get URL failed！')

        return response.text.encode('iso-8859-1').decode('gbk')

    # 获取gb社论，人民时评等子网页地址
    def get_gb_url_all(self):
        for i in self.gb_list:
            s = ''.join([self.url, str(i), '/index.html'])
            self.gb_url_list.append(s)

        return self.gb_url_list

    # 获取gb每个子网页内容
    def get_gb_page_text(self):
        self.get_gb_url_all()
        for page in self.gb_url_list:
            self.gb_text.append(self.get_response(page))

    # 获取每个gb子网页中的有效url
    def get_url_all(self):
        self.get_gb_page_text()
        for gb_text in self.gb_text:
            try:
                soup = bs4.BeautifulSoup(gb_text, features="lxml")
            except:
                pass
            url_a = soup.find_all('a')
            for i in url_a:
                if str(i['href']).find('/n1/') == 0:
                    # print(i['href'])
                    # print(i.string)
                    self.url_dict[i['href']] = i.string

        return self.url_dict

    # 获取每个URL中的文本信息
    def get_all_url_text(self):
        url_set = self.get_url_all()
        for url, title in url_set.items():
            # print(url, title)
            url_all = 'http://opinion.people.com.cn' + url
            print(url_all)
            print(title)
            response = self.get_response(url_all)
            soup = bs4.BeautifulSoup(response, features="lxml")
            p = soup.find_all('p')
            for i in self.gb_list:
                if os.path.exists('./files/' + str(i)):
                    pass
                else:
                    os.mkdir('./files/' + str(i))
                with open('./files/' + str(i) + '/' + title + '.txt', 'w+') as result:
                    for pi in p:
                        if pi.string != None and pi.string != '忘记密码？':
                            # print(pi.string)
                            try:
                                result.write(str(pi.string))
                            except:
                                print('写入文本失败')
                # print(pi.string)


if __name__ == '__main__':
    url = 'http://opinion.people.com.cn/GB/8213/49160/'
    renmin = CrawlerRenmin(url)
    renmin.get_all_url_text()
