# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
import datetime
import time

def njupt_suffix(d):
    return '%s'%d

def fdu_suffix(d):
    return '&paged=%s'%d

def thu_suffix(d):
    if d==0:
        return ''
    else:
        return '_%d'%d
def ucas_suffix(d):
    return 'pn=%s'%d

url_thu = {
    'url': 'http://www.cs.tsinghua.edu.cn/publish/cs/4853/',
    # 'url': 'http://www.cs.tsinghua.edu.cn/publish/cs/4844/',
    'mid': 'index',
    'ext': '.html',
    'suffix': thu_suffix,
    'table': u'div[class="box_list"] > ul > li',
    'a': u'a',
    'date': u'p',
    }
url_njupt = {
    'url': 'http://jwc.njupt.edu.cn/1594/',
    'mid': 'list',
    'ext': '.htm',
    'suffix': njupt_suffix,
    'table': u'div[frag="窗口4"] > table > tr ',
    'a': u'a',
    'date': u'div'
    }
url_fdu = {
    'url': 'http://www.cs.fudan.edu.cn/',
    'mid': '?cat=55',
    'ext': '',
    'suffix': fdu_suffix,
    'table': u'div[class="ui-list"] > dl ',
    'a': u'dd > p[class="tit"] > a',
    'date': u'dd > p:nth-of-type(2)'
    }

url_fdu2 = {
    'url': 'http://www.gsao.fudan.edu.cn/1659/',
    'mid': 'list',
    'ext': '.htm',
    'suffix': njupt_suffix,
    'table': u'div[id="wp_news_w10"]  > table > tr > td:nth-of-type(2)',
    'a': u'a',
    'date': u'div'
}
url_ucas = {
    'url' : 'http://www.ucas.ac.cn/site/157',
    'mid' : '?',
    'ext' : '',
    'suffix' : ucas_suffix,
    'table' :u'div[class="sc_q"] > p',
    'a': u'a',
    'date' : u'span'
}

configs = [url_thu, url_njupt, url_fdu, url_fdu2, url_ucas]
#configs = [url_ucas]
#------main------
if __name__=='__main__':
    for url in configs:
    # url = url_thu # choose config dict
        print('\n\n\n###########\nsearching for %s\n\n\n'%str(url))
        headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.167 Safari/537.36'}
        ONE_DAY = 86400
        limitday = datetime.datetime.fromtimestamp(time.time()-ONE_DAY*365).date() # find within 200d
        keys = [u'硕士', u'成绩', u'推免', u'研究生',u'夏令营',u'保研']
        cnt = 0

        print('limitday:',str(limitday))
        print('searching keywords:', keys)

        for page in range(15): # search 15 pages

            ind = url['suffix'](page+1)
            r = requests.get(url['url'] + url['mid'] + ind + url['ext'],headers=headers)
            r.encoding = 'utf-8'
            soup = BeautifulSoup(r.text,'lxml')

            for tr in soup.select(url['table']):
                a = tr.select_one(url['a'])
                title = a.text
                dstring = tr.select_one(url['date']).text
                dstring = dstring.strip()
                ymd = datetime.datetime.strptime(dstring, '%Y-%m-%d')
                # print title, dstring
                keywordFlag = False
                for k in keys:
                    keywordFlag = keywordFlag or (k in title)
                if not keywordFlag:
                    continue
                date = ymd.date()
                if date < limitday: # newer than limitday
                    continue
                print(title)
                print(date)
                if u'http' in a['href']:
                    print(a['href'])
                else:
                    print('http://'+url['url'].split('/')[2]+a['href'])
                cnt += 1
        print('\n%d items found'%cnt)
