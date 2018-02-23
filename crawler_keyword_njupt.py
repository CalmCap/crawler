# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
import datetime
import time

headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.167 Safari/537.36'}
ONE_DAY = 86400
limitday = datetime.datetime.fromtimestamp(time.time()-ONE_DAY*100).date() # find within 100d
keys = [u'考试', u'成绩']

print('limitday:',str(limitday))
print('searching keywords:', keys)

for page in range(5): # search 5 pages

    ind = '%d'%(page+1)
    r = requests.get('http://jwc.njupt.edu.cn/1594/list%s.htm'%ind,headers=headers)
    r.encoding = 'utf-8'
    soup = BeautifulSoup(r.text,'lxml')

    for tr in soup.select(u'div[frag="窗口4"] > table > tr '):
        arr = tr.text.split('\n')#!!!!!!!!!!!
        title = arr[5]
        ymd = datetime.datetime.strptime(arr[6], '%Y-%m-%d')
        keywordFlag = False
        for k in keys:
            keywordFlag = keywordFlag or (k in title)
        if not keywordFlag:
            continue
        date = ymd.date()
        if date < limitday: # newer than limitday
            continue
        print(title, date)
        td = tr.select('td')
        a = td[1].select_one('table > tr > td > a')
        print(a['href'])
