import urllib.request
import gzip
import json
import pprint, os, time, sys, subprocess

# 测试网络的连通性
ping = open('判断.txt','w')
ping.write('0')
ping.close()

subprocess.Popen(['start','测试网络连通性.py'],shell=True)
while True:
    ping_n = open('判断.txt')
    ping_if = ping_n.read()
    ping_n.close()
    if ping_if =='1':
        break
    elif ping_if == '0':
        time.sleep(5)
        continue
    else:
        print('出错！！！')
        sys.exit()

def get_weather_data() :
    city_name = input('请输入要查询的城市名称：')
    url1 = 'http://wthrcdn.etouch.cn/weather_mini?city='+urllib.parse.quote(city_name)
    url2 = 'http://wthrcdn.etouch.cn/weather_mini?citykey=101010100'
    #网址1只需要输入城市名，网址2需要输入城市代码
    #print(url1)
    weather_data = urllib.request.urlopen(url1).read()
    #读取网页数据
    weather_data = gzip.decompress(weather_data).decode('utf-8')
    #解压网页数据
    weather_dict = json.loads(weather_data)
    #将json数据转换为dict数据
    return weather_dict

def show_weather(weather_data):
    weather_dict = weather_data 
    #将json数据转换为dict数据
    if weather_dict.get('desc') == 'invilad-citykey':
        print('你输入的城市名有误，或者天气中心未收录你所在城市')
    elif weather_dict.get('desc') =='OK':
        forecast = weather_dict.get('data').get('forecast')
        
        wea_list = [
            '感冒：' + weather_dict.get('data').get('ganmao'),
            '温度：' + weather_dict.get('data').get('wendu') + '℃ ',
            '城市：' + weather_dict.get('data').get('city'),
            '天气：' + forecast[0].get('type'),
            '高温：' + forecast[0].get('high'),
            '低温：' + forecast[0].get('low'),
            '风向：' + forecast[0].get('fengxiang'),
            '风级：' + forecast[0].get('fengli')
        ]

        file_wea = open('today_wea.py','w')
        file_wea.write('wea_list = '+pprint.pformat(wea_list)+' \n')
        file_wea.close()
        list_txt = open('weather.txt','w')
        list_txt.write(str(wea_list[:]))
        list_txt.close()


        
'''
        print('城市：',weather_dict.get('data').get('city'))
        print('温度：',weather_dict.get('data').get('wendu')+'℃ ')
        print('感冒：',weather_dict.get('data').get('ganmao'))
        print('风向：',forecast[0].get('fengxiang'))
        print('风级：',forecast[0].get('fengli'))
        print('高温：',forecast[0].get('high'))
        print('低温：',forecast[0].get('low'))
        print('天气：',forecast[0].get('type'))
        print('日期：',forecast[0].get('date'))
                print('--------------------------')
    print('***********************************')
    input('回车以退出！')
'''
if __name__ == '__main__':
    show_weather(get_weather_data())
    with open('weather.txt') as f:
        print(f.read())
