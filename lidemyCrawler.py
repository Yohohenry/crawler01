import requests
import json
import ssl
from bs4 import BeautifulSoup
import os
import urllib
from urllib.request import urlopen, urlretrieve

ssl._create_default_https_context = ssl._create_unverified_context

# -*- coding: utf-8 -*-

url = 'https://api.hiskio.com/v1/courses/208/'
p = requests.get(url)
p.encoding = 'utf-8'
courses = json.loads(p.text)
chapters = courses['chapters']

#準備空序列
id_list = []
title_list = []

#取得lectures id and title
for i in chapters:
    for id in i['lectures']:
        id_list.append(id['id'])
        title_list.append(id['title'])
print(id_list, title_list)

#取得網址
# for id in range(len(id_list)):
#     try:
#         url2 = 'https://api.hiskio.com/v1/courses/208/lectures/' + str(id_list[id])
#         print('crawling:', url2)
#         lec = requests.get(url2)
#         lec.encoding = 'utf-8'
#         allJson = json.loads(lec.text)
#         title = allJson['title']
#         content = allJson['content']
#         sources = content['sources']
#         sourcesList = sources[0]
#         src = sourcesList['src']
#         filename = content['filename']
#         print(src)

        #存取影片
    #     dirname = 'onlineCourse/linux/'
    #     if not os.path.exists(dirname):
    #         os.mkdir(dirname)
    #     fileName2 = dirname + str(id) + '_' + title_list[id] + '.mp4'
    #     urlretrieve(src, fileName2)
    #     if '/' in title_list[id]:
    #         title = title_list[id].replace('/', '&')
    #         fileName2 = dirname + str(id) + '_' + title + '.mp4'
    #         urlretrieve(src, fileName2)
    #     print(fileName2, 'done')
    # except:
    #     print(src, 'fail')

#補下載(13, 21, 22)
dirname = 'onlineCourse/linux/'
url2 = 'https://api.hiskio.com/v1/courses/208/lectures/' + str(id_list[22])
print('crawling:', url2)
lec = requests.get(url2)
lec.encoding = 'utf-8'
allJson = json.loads(lec.text)
title = allJson['title']
content = allJson['content']
sources = content['sources']
sourcesList = sources[0]
src = sourcesList['src']
filename = content['filename']
print(src)

#存取影片
dirname = 'onlineCourse/linux/'
if not os.path.exists(dirname):
    os.mkdir(dirname)
title = title_list[22].replace('/', '&')
fileName2 = dirname + str(22) + '_' + title + '.mp4'
# fileName2 = dirname + str(21) + '_' + title_list[21] + '.mp4'
urlretrieve(src, fileName2)
if '/' in title_list[21]:
    title = title_list[21].replace('/', '&')
    fileName2 = dirname + str(21) + '_' + title + '.mp4'
    urlretrieve(src, fileName2)
# if '|' in title_list[13]:
#     title = title_list[13].replace('|', '&')
#     fileName2 = dirname + str(13) + '_' + title + '.mp4'
#     urlretrieve(src, fileName2)
print(fileName2, 'done')
# src = 'https://player.vimeo.com/external/382411711.hd.mp4?s=4cb6f0052511fc3359d3bd294585e5ec2ac879b1&profile_id=169'
# if not os.path.exists(dirname):
#     os.mkdir(dirname)
# fileName2 = dirname + '4' + '_' + 'Docker image & Docker hub的初步認識' + '.mp4'
# urlretrieve(src, fileName2)
# print(fileName2, 'done')