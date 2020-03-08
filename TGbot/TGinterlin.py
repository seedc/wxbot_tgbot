#!/bin/python3
#QQ:188189858 by:kaer

from telegram import Bot
import sys
import socket
import time
class IP_PORT:
    def __init__(self,a, b):
        bot = Bot('1002016449:AAFyq0-W64-zyfePHDe7nycS00kVx1Lo-gc') #改成你的
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print('服务器:', a, b, '连接测试')
        sa = s.connect_ex((a, int(b)))
        s.close()
        # print(sa)
        if sa == 0:
            print('Server', a, b, 'OK!')
        else:
            print('Server', a, b, 'not open')
            ticks = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            msg_1= 'The current time is:' + ticks + ' ' + a + ' ' + b + ' ' + 'DOWN'
            print(msg_1)
            bot.send_message("-230654961", msg_1)  # 发送消息