#!/Users/maxiaoyu/Desktop/python/evns /py3/bin/python3
#encoding:utf-8
'''
@File    :   4.py
@Time    :   2020/05/26 19:48:28
@Author  :   DesignerA 
@Version :   1.0
@Contact :   DesignerA@qq.com
@WebSite :   www.cnblogs.com/DesignerA
'''
# Start typing your code from here
#编写一个简单的聊天程序；
#其中一个进程发送文字聊天消息（从键盘输入文字消息）；  
#另外一个进程接收并打印消息；



from multiprocessing import Process,Queue
import time

def write(q,sentence):
    q.put(sentence)

def read(q):
    while(True):
        sentence = q.get(True)
        print(sentence)

def main():
    q=Queue()
    sentence=input('请输入聊天内容：')
    A=Process(target=write,args=(q,sentence,))
    B=Process(target=read,args=(q,))
    A.start()
    B.start()
    A.join()
    B.terminate()

main()