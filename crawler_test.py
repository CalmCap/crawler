# -*- coding:utf-8 -*-

#njupt
'''
import requests
from bs4 import BeautifulSoup
headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.167 Safari/537.36'}
r = requests.get('http://jwc.njupt.edu.cn/1594/list.htm',headers=headers)
r.encoding = 'utf-8'
soup = BeautifulSoup(r.text,'lxml')
for tr in soup.select('div[frag="窗口4"]  > table > tr '):
    print(tr.text)
    a = tr.select_one('td > table > tr > td > a')
    print(a['href'])
'''

#other
import requests
from bs4 import BeautifulSoup
headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.167 Safari/537.36'}
r = requests.get('http://www.ucas.ac.cn/site/157?pn=1',headers=headers)
r.encoding = 'utf-8'
soup = BeautifulSoup(r.text,'lxml')
for tr in soup.select('div[class="sc_q"] > p'):
    #print(tr.text)
    #print (tr)
    a = tr.select_one('span')
#    print(a['href'])
    print(a.text)
