
# 个人微信bot远程监控端口报警和TG远程监控端口报警
windows图形化后续开发-主要用于运维端口监控

BY：kaer

TG：@anonymousxxxxxx #长期在线

配置格式config.json

```
{
  "14.215.177.39": {
          "http": "80",
          "https": "443",
          "mongodb": "27017"
  },
  "113.96.232.215": {
          "http": "80",
          "https": "443",
          "mongodb": "27018"
  }
}
```
一个IP可以配置多个不同端口，多个IP可以自行根据格式增加，使用json格式一致。

微信报警修改：
WXinterlin.py ：内修改你的微信报警群名字

微信运行后终端会出现二维码，扫码登录即可。



Telegram 报警修改:
TGinterlin.py ：修改你的bot ID如下
```
1002016449:AAFyq0-W64-zyfePHDe7nycS00kVx1Lo-gc
```
```
bot.send_message("-230654961", msg_1) #这里修改TG报警群，只用机器人去掉群ID
```
有一起研究学习python3 和共同开发项目的请联系我TG，希望在这方面长足进步！
