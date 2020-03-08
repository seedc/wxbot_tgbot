#!/bin/python3
#QQ:188189858 by:kaer
#pip install itchat
import itchat
import sys
import socket
import time

#itchat.auto_login(hotReload=True) #产生图片登录适合web
itchat.auto_login(enableCmdQR = 2,hotReload = True) #终端输出二维码
itchat.send("机器人成功登录",toUserName="filehelper") #发送登录成功