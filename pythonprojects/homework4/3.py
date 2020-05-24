#!/Users/maxiaoyu/Desktop/python/evns /py3/bin/python3
#encoding:utf-8
'''
@File    :   3.py
@Time    :   2020/04/23 22:48:49
@Author  :   DesignerA 
@Version :   1.0
@Contact :   DesignerA@qq.com
@WebSite :   www.cnblogs.com/DesignerA
'''
# Start typing your code from here
#从键盘输入5个同学的账号和密码,然后将他们的姓名,账号和密码(密码需要加密)保存到一个文件中;
#Tom   admin   XXXXX
#Jack   root   XXXXX   
list1=[]
for i in range(0,5):
    i=str(i)
    name=input('第'+i+'名学生的姓名为：')
    number=input('第'+i+'名学生的账号为：')
    password=input('第'+i+'名学生的密码为：')
    dic1={'name':name,'number':number,'password':password}
    list1.append(dic1)
import json
list2=json.dumps(list1)
with open('/Users/maxiaoyu/Desktop/python/name_num_password.txt','w') as f:
    f.writelines(list2)