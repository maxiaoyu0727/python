#!/Users/maxiaoyu/Desktop/python/evns /py3/bin/python3
#encoding:utf-8
'''
@File    :   1.py
@Time    :   2020/03/12 01:02:15
@Author  :   DesignerA 
@Version :   1.0
@Contact :   DesignerA@qq.com
@WebSite :   www.cnblogs.com/DesignerA
'''
# Start typing your code from here
#第一次作业
#元素输出和查找：  请输出0-50之间的奇数，偶数，质数；能同时被2和3整除的数；
list1=list(range(51))
print('0-50之间的奇数有:')
for x in list1:
    if x % 2!=0:
        print(x)
print("0-50之间的偶数有:")
for x in list1:
    if x %2 ==0:
        print(x)
print("0-50之间的质数有：")
num=[]
for i in range(2,100):
   j=2
   for j in range(2,i):
      if(i%j==0):
         break
   else:
      num.append(i)
print(num)
print("0-50之间能同时被2和3整除的有：")
for x in list1:
    if(x%2==0):
        if(x%3==0):
            print(x)