# -*- coding: utf-8 -*-
"""
Created on Sunday May 2019.05.26


"""

f = open('D:\BaiduNetdiskDownload\资料01_商铺数据.csv','r',encoding='utf8')
print(f)
f.seek(0) #readlines时将光标移到开头，默认是在每行结尾
for i in f.readlines()[:2]:
    print(i.split(','))

def fcm(s):
    if '条' in s:
        return int(s.split(' ')[0])
    else:
        return '缺失数据'

def fcl(s):

f.seek(0)
for i in f.readlines()[:10]:
    data = i.split(',')
    comment_count = data[2]
    print(comment_count)
    com2 = fcm(comment_count)
    print(com2)

df = pd.read_csv('D:\BaiduNetdiskDownload\资料01_商铺数据.csv')

