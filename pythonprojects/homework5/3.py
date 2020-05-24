#!/Users/maxiaoyu/Desktop/python/evns /py3/bin/python3
#encoding:utf-8
'''
@File    :   3.py
@Time    :   2020/05/12 17:35:04
@Author  :   DesignerA 
@Version :   1.0
@Contact :   DesignerA@qq.com
@WebSite :   www.cnblogs.com/DesignerA
'''
# Start typing your code from here
# 编写一个装饰器，为多个函数加上认证的功能（必须输入用户的账号密码，才能调用这个函数）

def decorator(func):
    def login():
        user_dic={}
        with open('/Users/maxiaoyu/Desktop/python/pythonprojects/5.3login.txt','r') as f:
            for line in f:
                name,password=line.split()
                user_dic.setdefault(name,password)
            name1=input('请输入用户姓名：')
            password1=input('请输入密码：')
            if user_dic.__contains__(name1) and user_dic[name1] == password1:
                print("登录成功")
                func()#执行传入的函数
            else:
                print('账号密码不匹配')
    return login


@decorator
def printfunc1():
    print('账户密码正确，成功调用第一个输出函数')

@decorator
def printfunc2():
    print('账户密码正确，成功调用第二个输出函数')

@decorator
def printfunc3():
    print('账户密码正确，成功调用第三个输出函数')

printfunc1()
printfunc2()
printfunc3()
