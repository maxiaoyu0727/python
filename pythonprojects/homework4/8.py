#!/Users/maxiaoyu/Desktop/python/evns /py3/bin/python3
#encoding:utf-8
'''
@File    :   8.py
@Time    :   2020/04/26 23:26:02
@Author  :   DesignerA 
@Version :   1.0
@Contact :   DesignerA@qq.com
@WebSite :   www.cnblogs.com/DesignerA
'''
# Start typing your code from here
#1） 生成一个大文件ip.txt,要求1200行，每行随机为172.25.254.1---172.25.254.254之间的一个ip地址;
#2） 读取ip.txt文件统计这个文件中ip出现频率排前10的ip

import random

def create_ip(path):
    with open(path,'a+') as f:
        for i in range(1200):
            end_of_ip=random.randint(1,255)
            ip='172.25.254.'+str(end_of_ip)
            f.write(ip + '\n')
create_ip('/Users/maxiaoyu/Desktop/python/ip.txt')

def sorted_ip(path,count=10):
    ip_dict = dict()
    with open(path) as f:
        for ip in f:
            ip = ip.strip()
            if ip in ip_dict:
                ip_dict[ip] += 1
            else:
                ip_dict[ip] = 1
    sorted_ip = sorted(ip_dict.items(),key=lambda x:x[1],reverse=True)[:count]

    return sorted_ip

print(sorted_ip('/Users/maxiaoyu/Desktop/python/ip.txt'))

