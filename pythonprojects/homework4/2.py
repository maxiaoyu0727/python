#!/Users/maxiaoyu/Desktop/python/evns /py3/bin/python3
#encoding:utf-8
'''
@File    :   2.py
@Time    :   2020/04/23 00:08:34
@Author  :   DesignerA 
@Version :   1.0
@Contact :   DesignerA@qq.com
@WebSite :   www.cnblogs.com/DesignerA
'''
# Start typing your code from here
#定义一个函数，判断一个输入的日期，是当年的第几周，周几？  
#将程序改写一下，能针对我们学校的校历时间进行计算（校历第1周，2月17-2月23；校历第27周，8月17-8月23；）
import datetime

def time_judgement(date_str):
    date = datetime.datetime.strptime(date_str, '%Y/%m/%d')
    print('该日期是当年的第',date.isocalendar()[1],'周')
    print('该日期是星期：',date.isocalendar()[2])


def schoolweek(startDateStr,searchDateStr):
    startDate=datetime.datetime.strptime(startDateStr,'%Y/%m/%d')
    searchDate=datetime.datetime.strptime(searchDateStr,'%Y/%m/%d')
    week=int(searchDate.strftime('%W'))-int(startDate.strftime('%W'))+1
    print('该日期是校历的第',week,'周')
date_str =input('请输入日期（2000/01/01）：')
startDateStr='2020/02/17'
time_judgement(date_str)
schoolweek(startDateStr,date_str)