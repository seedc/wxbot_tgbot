#!/bin/python3
#QQ:188189858 by:kaer

import json
import TGinterlin

while True:
    c = open('config.json',encoding='utf-8')
    dics = c.read()  #读文件
    d = json.loads(dics)
    IP = tuple (d)
    for i in IP:
        dics1 = (d[i])
        for o in dics1:
            dics2 = (dics1[o])
            TGinterlin.IP_PORT(i, dics2)
time.sleep(60)
