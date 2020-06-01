#给定100个企业网站首页链接地址（用1中给出的URL地址）；请爬取每个页面上，企业介绍的链接地址；
#说明，满足企业介绍网址的条件是， 标题包含：企业介绍，关于我们，企业发展，发展历史，企业概况等关键字的URL地址；
#提示：要用到requests库，BeautifulSoup库

import requests
from bs4 import BeautifulSoup
import os
import re
from urllib.error import URLError,HTTPError
import time

count=0
introduce_list=[]
list2=[]
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'}
with open('/Users/maxiaoyu/Desktop/python/pythonprojects/url.txt','r') as f:
    for l in f.readlines():
        #print(type(l))
        count+=1
        try:
            r = requests.get(l, headers=headers,timeout=5,verify=False).content.decode('utf-8')
            ret = re.findall("http://[0-9a-zA-Z_\.\-]*\.[com,cn,net,html]{1,3}", r)
            for url1 in ret:
                list2.append(url1)
                print(rul1)
            if count>=100:
                break
        except:
            time.sleep(5)
            


for url1 in list2:
    r2 = requests.get(url1, headers=headers,timeout=5,verify=False).content.decode('utf-8')
    soup=BeautifulSoup(r2)
    if '企业介绍' in str(soup.title) or '关于我们' in str(soup.title) or '企业发展' in str(soup.title) or '发展历史' in str(soup.title) or'企业概况' in str(soup.title):
        introduce_list.append(url1)
        print('企业介绍地址为：',url1)
    else:
        print('没有这样的介绍网页')


with open('/Users/maxiaoyu/Desktop/python/pythonprojects/introduce_url.txt','w') as f2:
    f2.write(introduce_list)


