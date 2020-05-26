#!/Users/maxiaoyu/Desktop/python/evns /py3/bin/python3
#encoding:utf-8
'''
@File    :   4.py
@Time    :   2020/05/26 23:43:37
@Author  :   DesignerA 
@Version :   1.0
@Contact :   DesignerA@qq.com
@WebSite :   www.cnblogs.com/DesignerA
'''
# Start typing your code from here
#设计一款能实现多人聊天的系统：使用socket和多线程技术，编写全多人聊天室

#还不太能写出来，所以试着把人家的代码读懂
import socket
import threading
import os
import datetime


def get_ip():
    """用来搞到IP"""
    host = socket.gethostname()#获取主机名
    ip = socket.gethostbyname(host)#用主机名获取IP地址
    return ip


def get_time():
    """得到发送时间"""
    now = datetime.datetime.now()
    send_time = now.strftime("%Y-%m-%d %H:%M:%S")
    return send_time



class ChatSever:

    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.addr = (get_ip(), 10000)#IP和端口
        self.users = {}

    def start_sever(self):
        self.sock.bind(self.addr)
        self.sock.listen(5)#listen函数把进程变为一个服务器
        print("服务器已开启，等待连接...")
        print("在空白处输入stop sever并回车，来关闭服务器")

        self.accept_cont()

    def accept_cont(self):
        while True:
            s, addr = self.sock.accept()
            self.users[addr] = s
            number = len(self.users)
            print("用户{}连接成功！现在共有{}位用户".format(addr, number))

            threading.Thread(target=self.recv_send, args=(s, addr)).start()
            
    def recv_send(self, sock, addr):
        while True:
            try:  # 测试后发现，当用户率先选择退出时，这边就会报ConnectionResetError
                response = sock.recv(4096).decode("gbk")
                msg = "{}用户{}发来消息：{}".format(get.get_time(), addr, response)

                for client in self.users.values():
                    client.send(msg.encode("gbk"))
            except ConnectionResetError:
                print("用户{}已经退出聊天！".format(addr))
                self.users.pop(addr)
                break

    def close_sever(self):
        for client in self.users.values():
            client.close()
        self.sock.close()
        os._exit(0)


if __name__ == "__main__":
    sever = ChatSever()
    sever.start_sever()
    while True:
        cmd = input()
        if cmd == "stop sever":
            sever.close_sever()
        else:
            print("输入命令无效，请重新输入！")


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = (get.get_ip(), 10000)#只有自己一台电脑做测试时，可以直接用左边的
s.connect(addr)


def recv_msg():  #
    print("连接成功！现在可以接收消息！\n")
    while True:
        try:  # 测试发现，当服务器率先关闭时，这边也会报ConnectionResetError
            response = s.recv(1024)
            print(response.decode("gbk"))
        except ConnectionResetError:
            print("服务器关闭，聊天已结束！")
            s.close()
            break
    os._exit(0)


def send_msg():
    print("连接成功！现在可以发送消息！\n")
    print("输入消息按回车来发送")
    print("输入esc来退出聊天")
    while True:
        msg = input()
        if msg == "esc":
            print("你退出了聊天")
            s.close()
            break
        s.send(msg.encode("gbk"))
    os._exit(0)


threads = [threading.Thread(target=recv_msg), threading.Thread(target=send_msg)]
for t in threads:
    t.start()

