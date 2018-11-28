from wxpy import *

# 在初始化时便会执行登陆操作，需要手机扫描登陆。
# bot = Bot()
# 自动保存登录信息，就不需要每次扫二维码
bot = Bot(cache_path=True)
# 在Web微信中把自己加为好友
# bot.self.add()
# bot.self.accept()
#
# # 发送消息给自己
# bot.self.send(" 520，我爱你!")
# '''
# 指定聊天对象，大胆进行表白吧
# '''
# # 指定聊天对象，并发送你想说的话
# # 还可以发送图片，视频，文件或者动图等。可以试一下
# exit()
my_friend = bot.friends().search('胡晨雨')[0]
# found = ensure_one(my_friend) //确保找到的是唯一，避免重复
my_friend.send("亲，在干嘛呢")


# 如何指定聊天回复你了，聊天机器人自动回复设置好的消息。

@bot.register(my_friend)
def reply_my_friend(msg):
    return '{} ，收到你的消息了, 我爱你🌶'.format(msg.text, msg.type)

import time

time.sleep(10000000)

# '''
# 指定聊天对象，聊天机器人拒绝回复他的消息
# '''
# ignore_friend = bot.friends().search('简爱')[0]
#
#
# @bot.register(ignore_friend)
# def ignore(msg):
#     return
