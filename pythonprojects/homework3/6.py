#!/Users/maxiaoyu/Desktop/python/evns /py3/bin/python3
#encoding:utf-8
'''
@File    :   6.py
@Time    :   2020/04/15 00:29:57
@Author  :   DesignerA 
@Version :   1.0
@Contact :   DesignerA@qq.com
@WebSite :   www.cnblogs.com/DesignerA
'''
# Start typing your code from here
#在2个文件中存放了英文计算机技术文章, 请读取文章内容,进行词频的统计;并分别输出统计结果到另外的文件存放;
#比较这2篇文章的相似度(如果词频最高的前10个词,重复了5个,相似度就是50%;重复了6个,相似度就是60% 

with open("/Users/maxiaoyu/Desktop/python/pythonprojects/passage1.txt", 'r') as f:
    lines = f.read()
cptj = {}
#将词频统计的结果存放到一个字典中
for line in lines:
    if line in cptj:
        cptj[line] += 1
    else:
        cptj[line] = 1
#将字典转化为类表方便进行后续的处理
lcptj = list(cptj.items())
#对生成的结果进行排序，按照每个元祖下标为1的数进行排序
lcptj.sort(key=lambda x: x[1], reverse=True)
count=0
#将结果进行输出
for i in lcptj:
    print(i,"\t",end='')
    count+=1
    #对结果输出做出美化，使其每行打印出五个元素
    for j in range(int(len(lcptj)/5)+1):
        if count== 5*j:
            print()
        else:
            pass
print('\n')


with open("/Users/maxiaoyu/Desktop/python/pythonprojects/passage2.txt", 'r') as f1:
    lines1 = f1.read()
cptj1 = {}
#将词频统计的结果存放到一个字典中
for line1 in lines1:
    if line1 in cptj1:
        cptj1[line1] += 1
    else:
        cptj1[line1] = 1
#将字典转化为类表方便进行后续的处理
lcptj1 = list(cptj1.items())
#对生成的结果进行排序，按照每个元祖下标为1的数进行排序
lcptj1.sort(key=lambda x: x[1], reverse=True)
count1=0
#将结果进行输出
for j in lcptj1:
    print(j,"\t",end='')
    count1+=1
    #对结果输出做出美化，使其每行打印出五个元素
    for k in range(int(len(lcptj1)/5)+1):
        if count1== 5*k:
            print()
        else:
            pass
print('\n')

dlcptj=dict(lcptj)
dlcptj1=dict(lcptj1)
a=list(dlcptj.keys())
b=list(dlcptj1.keys())


flag=0
for m in range(0,9):
    if(a[m]==b[m]):
        flag+=1    
flag1=flag * 10
print('相似度为：',flag1,'%')
