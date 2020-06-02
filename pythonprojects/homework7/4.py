#爬取这个网址上https://www.programcreek.com/python/，
#搜索request的范例代码；保存到txt文件中（只保留文字）；

from bs4 import BeautifulSoup
import requests

url = 'https://www.programcreek.com/python/index/221/requests'
headers = {
	'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'
}
r = requests.get(url,headers=headers).content.decode('utf-8')
 
#解析html文档
soup = BeautifulSoup(r,'html.parser')
 
#查找每个练习的a链接href属性获取对应的链接地址
re_a = soup.find(id='api-list').find_all('a')

#创建一个列表保存url
list = []
for i in re_a:
	list.append(i.attrs['href'])
#print(list)

for x in list:
    dict1 = {}
    # 请求详细页面
    test = requests.get(x, headers=headers).content.decode('utf-8')
    # print(test)

    # 解析html文档
    soup_test = BeautifulSoup(test, 'html.parser')
    #print(type(soup_test))

    dict1['example'] = soup_test.find(id='main').h1.text
    
    list1=[]
    for i in soup_test.find_all('pre', class_='prettyprint'):
        list1.append(i.text)
    dict1['ans']=list1

#保存文件
    with open('/Users/maxiaoyu/Desktop/python/pythonprojects/request_code.txt','a+',encoding='utf-8') as file:
        file.write(dict1['example']+'\n')
        for i in dict1['ans']:
            file.write("**************************************")
            file.write('\n')
            file.write(i+'\n')
            