#!/bin/python3
#QQ:188189858 by:kaer
#pip install itchat
import itchat
import sys
import socket
import time

itchat.auto_login(enableCmdQR = 2,hotReload = True)
itchat.send("机器人成功登录",toUserName="filehelper")
