#!/Users/maxiaoyu/Desktop/python/evns /py3/bin/python3
#encoding:utf-8
'''
@File    :   3.py
@Time    :   2020/05/26 23:12:28
@Author  :   DesignerA 
@Version :   1.0
@Contact :   DesignerA@qq.com
@WebSite :   www.cnblogs.com/DesignerA
'''
# Start typing your code from here
#编写一个UDP的聊天程序，客户端和服务器端能互相聊天应答；

#仿照多任务中的示例
import socket
import threading

def send_msg(udp_socket):
    """获取键盘数据，并将其发送给对方"""
    while True:
        msg = input("\n请输入要发送的数据:")
        dest_ip = input("\n请输入对方的ip地址:")
        dest_port = int(input("\n请输入对方的port:"))
        udp_socket.sendto(msg.encode("utf-8"), (dest_ip, dest_port))


def recv_msg(udp_socket):
    """接收数据并显示"""
    while True:
        recv_msg = udp_socket.recvfrom(1024)
        recv_ip = recv_msg[1]
        recv_msg = recv_msg[0].decode("utf-8")
        print(">>>%s:%s" % (str(recv_ip), recv_msg))


def main():
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.bind(("", 9999))
    t = threading.Thread(target=recv_msg, args=(udp_socket,))
    t.start()
    send_msg(udp_socket)

if __name__ == "__main__":
    main()