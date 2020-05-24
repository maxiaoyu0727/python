#!/Users/maxiaoyu/Desktop/python/evns /py3/bin/python3
#encoding:utf-8
'''
@File    :   4.py
@Time    :   2020/04/24 21:05:48
@Author  :   DesignerA 
@Version :   1.0
@Contact :   DesignerA@qq.com
@WebSite :   www.cnblogs.com/DesignerA
'''
# Start typing your code from here
# 5个同学的姓名,账号和密码(加密后的),保存在一个文件上;   
# 系统提示,请输入登录同学姓名, 正确后,请输入账号, 正确后,提示请输入密码（输入明文）;  
# 如果都正确,打印提示, 您登录成功(失败);

import os
import json
with open('/Users/maxiaoyu/Desktop/python/name_num_password.txt','r') as f:
    list1=f.read()
    list2=json.loads(list1)
    
name=input('请输入学生姓名：')
for i in range(0,5):
    dic1=list2[i]
    if(name==dic1['name']):
        print('姓名正确')
        stu_dic=dic1
        break
number=input('请输入学生账号：')
if(number==stu_dic['number']):
    password=input('请输入密码：')
    if(password==stu_dic['password']):
        print('登录成功')
    else:
        print('密码错误，登录失败')
else:
    print('账号错误，登录失败')