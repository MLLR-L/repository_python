import configparser
# 写入
config = configparser.ConfigParser()
# 第一种方法
config['说明'] = {"[CONFIG]":"里面的东西叫做节点",
                 "我叫OPTION":"我是值"}
# 第二种方法
config['CONFIG'] = {}
config['CONFIG']['配置1'] = '我是路径1'
config['CONFIG']['配置2'] = '我是路径2'
# 第三种方法
config['第三种方法'] = {}
topsecret = config['第三种方法']
topsecret['ini1'] = '内容'
topsecret['ini2'] = '123456'

with open('配置文件示例.ini', 'w', encoding='utf-8') as f:
    config.write(f)

# 读取
config.read('配置文件示例.ini', encoding='utf-8')
print("输出元组，包括option的key和value",config.items('CONFIG'))
print("所有节点==>", config.sections())
print("CONFIG节点下所有option的key，包括默认option==>",config.options("CONFIG"))
# 获取值
# 方式1
print("CONFIG下配置1的值==>",config["CONFIG"]["配置1"])
topsecret = config['CONFIG']
# 方法2
print("bitbucket.org下user的值==>",topsecret["配置1"])

# 方法3
print("获取CONFIG下配置1的值==>", config.get("CONFIG", "配置1"))
print("获取第三种方法值为数字的:ini2=", config.getint("第三种方法", "ini2"))

print("包含实例范围默认值的词典==>", config.defaults())

for item in config["说明"]:
    print("循环节点说明下所有option==>",item)

print("判断CONFIG节点是否存在==>",'CONFIG' in config)

