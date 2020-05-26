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


#仿照课件写的
import socket
import threading


def send_msg(udp_socket):
    """获取键盘数据，并将其发送给对方"""
    while True:
        msg = input("\n请输入要发送的内容:")
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
    udp_socket.bind(("", 7890))
    t = threading.Thread(target=recv_msg, args=(udp_socket,))
    t.start()
    send_msg(udp_socket)

if __name__ == "__main__":
    main()