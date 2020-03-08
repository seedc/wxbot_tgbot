#!/bin/python3
#QQ:188189858 by:kaer
#pip install itchat
import itchat
import sys
import socket
import time
class IP_PORT:
    def __init__(self,a, b):
        # self.a = a
        # self.b = b
        #print(self.a)
        #print(self.b)
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
            chatroomName = 'test1'  # 群名需要修改
            itchat.get_chatrooms(update=True)
            chatrooms = itchat.search_chatrooms(name=chatroomName)
            if len(chatrooms) == 0:
                print('没有找到群聊：' + chatroomName)
            else:
                print(chatrooms[0]['UserName'])  # 输出群聊标识符
                fasong = 'The current time is:' + ticks + ' ' + a + ' ' + b + ' ' + 'DOWN'
                print(fasong)
                itchat.send_msg(fasong, toUserName=chatrooms[0]['UserName'])  # 发送消息