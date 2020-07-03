import requests
import json
import ssl
import os
import urllib
from urllib.request import urlopen, urlretrieve

ssl._create_default_https_context = ssl._create_unverified_context

# -*- coding: utf-8 -*-

#找到request的url
#像是https://api.tibame.com/learningCenter/user/stagelistTrial/484 最後的數字會不同
url = 'https://api.tibame.com/learningCenter/user/stagelistTrial/484'
p = requests.get(url)
p.encoding = 'utf-8'
r = json.loads(p.text)
data = r['data']
stage = data['stageList']
urllist = []
missionName = []

# mission = stage['missions']

for s in range(8):
    for m in stage[s]['missions']:
        print(m['missionName'], m['filePath'])
        try:
            urli = m['filePath']
            b = b'/:?='
            urli = urllib.parse.quote(urli, b)
            urllist.append(urli)
            missionName.append(m['missionName'])
            # dirname = 'tibame/postgreSQL/'
            # if not os.path.exists(dirname):
            #     os.mkdir(dirname)
            # fileName = dirname + m['missionName'] + '.mp4'
            # urlretrieve(urli, fileName)
            # print(m['missionName'], 'done')
        except:
            print('no file')
# for i in urllist:
#     print(urllist.index(i), i)

# 存取影片
for i in range(len(urllist)):
    try:
        #選擇要存取的資料夾
        dirname = 'tibame/'
        if not os.path.exists(dirname):
            os.mkdir(dirname)
        fileName = dirname + str(i) + '_' + missionName[i] + '.mp4'
        urlretrieve(urllist[i], fileName)
        if '/' in missionName[i]:
            missionName = missionName[i].replace('/', '&')
            fileName = dirname + str(i) + '_' + missionName + '.mp4'
            urlretrieve(urllist[i], fileName)
        print(i, missionName[i], 'done')
    except:
        #顯示未下載到的
        print(i, missionName[i], 'fail')