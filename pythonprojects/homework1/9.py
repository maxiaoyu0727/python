#!/Users/maxiaoyu/Desktop/python/evns /py3/bin/python3
#encoding:utf-8
'''
@File    :   9.py
@Time    :   2020/03/12 13:26:32
@Author  :   DesignerA 
@Version :   1.0
@Contact :   DesignerA@qq.com
@WebSite :   www.cnblogs.com/DesignerA
'''
# Start typing your code from here
#设计一个猜数字 游戏；最多只能猜测N次，在N次之内猜不出，就退出程序，提示猜测失败
import random

number=random.randint(0,100)
guess=-1
flag=0
print("欢迎来到猜数字游戏！")

while(guess!=number):
    guess1=input("请输入你猜的数字:")
    guess=int(guess1)
    if(guess==number):
        print("恭喜你猜对了")
    elif(guess<number):
        print("猜的数字小了")
    elif(guess>number):
        print("猜的数字大了")
    flag+=1
    if(flag==7):
        break
if(guess!=number):
    print("猜测失败")
  



