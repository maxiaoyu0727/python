#!/Users/maxiaoyu/Desktop/python/evns /py3/bin/python3
#encoding:utf-8
'''
@File    :   2.py
@Time    :   2020/05/26 23:05:39
@Author  :   DesignerA 
@Version :   1.0
@Contact :   DesignerA@qq.com
@WebSite :   www.cnblogs.com/DesignerA
'''
# Start typing your code from here
#编写一个接收数据的网络程序，由“网络调试工具”发送数据，你的程序接收数据并打印输出；
from socket import *

def main():
    udp_socket=socket(AF_INET,SOCK_DGRAM)
    
    local_addr=('127.0.0.1',9999)

    udp_socket.bind(local_addr)
   
    recv_data = udp_socket.recvfrom(1024) 

    print(recv_data)

    udp_socket.close()

if __name__ == "__main__":
    main()