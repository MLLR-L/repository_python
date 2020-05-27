#! python3
"""
MSendV1.0 - M
转发指定search_group的search消息，如果出现search的内容则发送给send_To群
定点17:00发送send_mess的消息到send_TO群
注意事项：
    1.请保持网络通畅，电脑没有定时休眠或关机！
    2.建议使用小号登录！若出了问题后果自负
    3.这是辅助工具！基于网页版
参考网站：https://wxpy.readthedocs.io/zh/latest/
"""

from wxpy import *
from time import strftime
from threading import Timer
import os

print('search为要转发消息的内容永恒不变一部分，内容越多越精准,回车则是全部转发')
search = input('请输入需要转发的内容：')

search_group = input('要查找转发内容的群名：')
send_To = input('被转发发消息、定点发送消息的群：')
# 定点发送消息的内容
send_mess_time = input('是否需要定点发送消息 【17】下午五点，回车以略过：')
if len(send_mess_time):
    send_mess = input('请输入要发送的内容：')

# 扫码登录
bot = Bot(cache_path=True)
# 用户登录之后，用户信息保存在同路径下的wxpy.pkl的文件中
bot.enable_puid()

# 定义一个函数用来发送消息给指定的人
def send_f():
    print(bot.friends())
    person = input('请选择一个人的名字：')
    message = input('请选择要发送的内容：')
    bot.friends().search(keywords=person)[0].send(message)

# 定义一个函数用来发送信息给指定的群
def send_who_g():
    print(bot.groups())
    group_name = input('请选择要发送的群名')
    message = input('请选择要发送的内容：')
    try:
        bot.groups().search(keywords=group_name)[0].send(message)
    except:
        print('我找不到这个群QAQ！')
        bot.groups()

# 定义一个函数来发送信息给确切知道信息的指定群
def send_g(group_name, message):
    try:
        bot.groups().search(keywords=group_name)[0].send(message)
    except:
        print('我找不到这个群QAQ')
        bot.groups()

# 定义一个函数来找到指定的消息内容并调用send_g来发送指定消息群
def search_code():
    if msg_l[0] == search_group and search in msg_l[1][1]:
        message = msg_l[1][1]
        send_g(send_To, message)


# 接受响应信息并执行处理
@bot.register()
def bb(msg):
    global msg_l
    msg = str(msg)
    # 如果是群消息就会有' › '的符号，那就执行这个
    if ' › ' in msg:
        msg_l = msg.split(' › ')
        msg_l[1] = msg_l[1].split(' : ')
        msg_l[1].append(msg_l[1][1][:msg_l[1][1].rfind('(')])
        msg_l[1].append(msg_l[1][1][msg_l[1][1].rfind('('):])
        del msg_l[1][1]
        print('群 %s-成员 %s：%s ' % (msg_l[0], msg_l[1][0], msg_l[1][1]))  # msg_l[1][2])为传输的类型
    # 如果是个人消息就没有' › '则直接处理    
    else:
        msg_l = msg.split(' : ')
        msg_l.append(msg_l[1][:msg_l[1].rfind('(')])
        msg_l.append(msg_l[1][msg_l[1].rfind('('):])
        del msg_l[1]
        print('%s：%s %s' % (msg_l[0], msg_l[1], msg_l[2]))
    search_code()

# 定义一个定点发送消息的函数
def t_time():
    # 定点发送消息，用当前时间的指定时间的小时分钟秒-(小时*120-1+分钟*60-1+秒-1)
    # 减去的结果是秒数，利用多线程的threading的Timer来阻塞到指定时间来执行函数
    if int(strftime('%H')) < send_mess_time:
        ding_time = ((send_mess_time - int(strftime('%H')) - 1) * 60 * 60) + ((60 - int(strftime('%M')) - 1) * 60) + (
                60 - int(strftime('%S')) - 1)
    # 如果是下午五点前则直接减，如果过了是第二天的时间则用24小时减去当前时间到了00点后再加上17个小时就到了下午五点
    elif int(strftime('%H')) > send_mess_time:
        ding_time = (((24-int(strftime('%H'))) + send_mess_time * 60 * 60) + (60 - int(strftime('%M'))) * 60 + (
                60 - int(strftime('%S'))))
    print('还有%s秒定时发送' % (round(int(ding_time), 2)))
    Timer(int(ding_time), send_g, (send_To, send_mess,)).start()



print('\n\n已登录成功\n')
print(f'【任务】:要转发内容`{search}`从群`{search_group}`到群`{send_To}`')
if len(send_mess_time):
    print(f'【定点任务】:{send_mess_time}发送消息{send_mess}')
print('\n支持的函数：\n\t【1】发送给好友：send_f()\n\t【2】发送消息给指定的群：send_who_g()')
if len(send_mess_time):
    t_time()
embed(banner='开始运行...', shell='ipython')
