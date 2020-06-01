#给定一个网址（包含了优质的英语学习音频文件），http://www.listeningexpress.com/studioclassroom/ad/；  
#请大家写一个爬虫，将里面的英语节目MP3，都下载下来；
#这些音频文件 在网页的html文件内容都是以mp3结尾的，如下图所示：
#要求大家使用Requests库获取这个网页html文本内容，
#并且使用正则表达式获取里面所有的mp3文件的网址；并进行下载；

import requests
import os
import re
from urllib.parse import quote
import urllib

list1=[]
headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'}
url='http://www.listeningexpress.com/studioclassroom/ad/'
r = requests.get(url, headers=headers).content.decode('GBK')
ret = re.findall(r"sc-ad.*?\.mp3", r)
headurl='http://www.listeningexpress.com/studioclassroom/ad/'
i=1
for url in ret:
    list1.append(url)

for url in list1[1:]:
    filename=str(i) + '.mp3'
    #print(filename)
    #print(type(url))
    download_url=headurl + quote(url)
    #print(download_url)
    path='/Users/maxiaoyu/Desktop/python/pythonprojects/mp3_file/'+filename
    urllib.request.urlretrieve( download_url,path)
    i+=1
 