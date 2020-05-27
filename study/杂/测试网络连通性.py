#! python3
# 检测网络连通性--ping百度的ip

import os, time

while True:
      ping = os.system(u"ping 14.215.177.39 -n 1")
      if ping == 0:
            file_if = open('判断.txt','w')
            file_if.write('1')
            file_if.close()
            break
      else:
            file_if = open('判断.txt','w')
            file_if.write('0')
            file_if.close()
            time.sleep(5)
            continue
