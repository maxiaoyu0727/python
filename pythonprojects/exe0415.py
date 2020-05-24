#!/Users/maxiaoyu/Desktop/python/evns /py3/bin/python3
#encoding:utf-8
'''
@File    :   exe0415.py
@Time    :   2020/05/17 01:27:49
@Author  :   DesignerA 
@Version :   1.0
@Contact :   DesignerA@qq.com
@WebSite :   www.cnblogs.com/DesignerA
'''
# Start typing your code from here
#正则表达式
#匹配出163的邮箱地址，且@符号之前有4到20位英文或者数字字符，例如hello@163.com

import re
print(re.match("[a-zA-Z0-9]{4,20}@163.com","hello@163.com").group())