#给定一个文件，请用正则表达式，逐行匹配提取其中的URL链接信息，并保存到另外一个文件中；
#提示，文件有1000行，注意控制每次读取的行数；

import os
import re

urllist=[]
with open('/Users/maxiaoyu/Desktop/python/pythonprojects/webspiderUrl.txt','r',encoding='utf-8') as f:
    for l in f.readlines():
        url = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', l)
        for url1 in url:
            urllist.append(url1)

with open('/Users/maxiaoyu/Desktop/python/pythonprojects/url.txt','w') as f2:
    for l in urllist:
        #print(url1)
        f2.write(l+'\n')
