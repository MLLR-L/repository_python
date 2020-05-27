#! python3
# 启动更新程序并输出当日的天气

import subprocess,time,win32api,win32con
from wea_output import *
print('我是天气提醒的哈(๑•̀ㅂ•́)و✧')

#subprocess.Popen(['天气_output.py'],shell=True)

time.sleep(5)

# 测试网络的连通性
while True:
      ping = open('判断.txt')
      ping_if = ping.read()
      ping.close()
      if ping_if =='1':
            break
      elif ping_if == '0':
            time.sleep(5)
            continue
      else:
            print('出错！！！请检查判断.txt文本的内容与脚本是否有误！')
            sys.exit()
      
show_weather(get_weather_data())
wea_file = open('weather.txt')
wea_list = list(eval(wea_file.read()))

wea_list_s = ''
for i in wea_list:
      wea_list_s +=i + '\n'
win32api.MessageBox(0,wea_list_s,'天气预报',win32con.MB_ICONASTERISK)

