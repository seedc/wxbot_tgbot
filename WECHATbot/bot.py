#!/bin/python3
#QQ:188189858 by:kaer

import json
import WXinterlin

while True:
    c = open('config.json',encoding='utf-8') #打开‘product.json’的json文件
    dics = c.read()  #读文件
    d = json.loads(dics) #把json串变成python的数据类型：字典
    #print ("这里是d的数据：",d)
    #print (len(dics))
    IP = tuple (d)
    #print("这里是IP的数据：",IP)
    for i in IP:
        #print ("这里是i的数据:",i)
        dics1 = (d[i])
       # print("这里是dics1的数据:",dics1)
        for o in dics1:
          #  print("这里是o的数据:",o)
            dics2 = (dics1[o])
          #  print ("这里是dics2的数据：",dics2)
            WXinterlin.IP_PORT(i,dics2)
time.sleep(60)