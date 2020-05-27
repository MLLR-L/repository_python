"""
    * 时间: Sun May 10 21:47:03 2020
    * 功能：方便的打开已编写好的文件/文件夹
    * 目的：
        1. 有一个文本文件放置着各类需求方便后期更改
        2. 承接class_deploy的GUI
        3. 打开对应的路径文件与文件夹
        4. 在系统环境路径指向此路径，支持运行时参数的输入

"""
from configparser import ConfigParser
from os.path import exists
from os import popen
from PyQt5 import QtWidgets
import sys

# 配置文件，基本信息获取
config = ConfigParser()
if not exists('tool-box.ini'):
    config['说明'] = {"显示的文本": "文件夹或文件名",
                    "我是示例": '指定的绝对路径', }
    config['CONFIG'] = {"示例：C盘": "C:",
                    "示例：github": 'https://github.com',}
    with open('tool-box.ini', 'w', encoding='utf-8') as f:
        config.write(f)

config.read('tool-box.ini', encoding='utf-8')
config_ini = config.options("CONFIG")

for i in range(len(config_ini)):
    config_ini[i] = config_ini[i].capitalize()

# GUI设置
# print the GUI
window_width = 250  # 宽度：按钮150  +留白100
window_height = len(config_ini) * 50 + 200  # 高度：数量 * 按钮高度50 + 自动取消按钮50 + 留白100
app = QtWidgets.QApplication([])  # 声明主程序
# main window setting
main_window = QtWidgets.QWidget()  # 声明主窗口
main_window.resize(window_width, window_height)  # 定义窗口大小
main_window.setWindowTitle('工具集合中心')

# 自动退出按钮 默认自动退出，按下取消
autoquit_code = 0


# 自动退出按钮的动作
def judgment_autoquit():
    # 设置全局autoquit_code，如果为0则自动退出反则否之
    global autoquit_code
    if autoquit_code == 0:
        # 如果为0则变1，取消自动退出
        autoquit_code = 1
        autoquit1.setText('自动退出')  # 改变按钮的文字
    elif autoquit_code == 1:
        # 如果为1则变0，变成自动退出
        autoquit_code = 0
        autoquit1.setText('取消自动退出')  # 改变按钮的文字


# 取消自动退出的按钮设置
autoquit1 = QtWidgets.QPushButton('取消自动退出', main_window)
autoquit1.move(50, len(config_ini) * 50 + 50)  # 按钮在窗口的位置宽高，+40是为了上面有留白
autoquit1.resize(150, 50)  # 按钮大小
autoquit1.clicked.connect(judgment_autoquit)  # 这里绑定了按钮的事件


# 指定打开ini配置文件的动作
def open_inifile():
    popen('start tool-box.ini')


# 打开配置文件的按钮设置
autoquit2 = QtWidgets.QPushButton('打开配置文件', main_window)
autoquit2.move(50, len(config_ini) * 50 + 100)  # 按钮在窗口的位置宽高，+40是为了上面有留白
autoquit2.resize(150, 50)  # 按钮大小
autoquit2.clicked.connect(open_inifile)  # 这里绑定了按钮的事件

# 执行指定操作
def running(run_path):
    # 执行打开动作
    print('running...')
    running_path = config.get("CONFIG", run_path)
    popen("start " + running_path)
    if autoquit_code == 0:
        sys.exit()

# 初始化一个执行代码，轮番查看输入的参数是否在列表中，匹配成功则赋值给run_code
run_code = 0
if len(sys.argv) == 2:
    argv_lower = sys.argv[1].lower()
    for i in range(len(config_ini)):
        if argv_lower in config_ini[i].lower():
            run_code = config_ini[i]

def white_button(button_ini, button_size_w, button_size_h, button_w, button_h, button_click):
    """
    按钮空白通用模板
    :param button_ini: 按钮显示的内容
    :param button_size_w: 按钮所在窗口的位置 - 宽
    :param button_size_h: 按钮所在窗口的位置 - 高
    :param button_w: 按钮的宽度
    :param button_h: 按钮的高度
    :param button_click: 按钮输出的文字
    :return: button_click，作为子文件目录输出以便后续操作
    """

    # 配置点击动作，点击则获取点击的动作并指定对应的路径
    def quick_clicked():
        # 执行运行动作
        running(button_click)

    # 设置按钮的位置
    btn = QtWidgets.QPushButton(button_ini, main_window)
    # 按钮在窗口的位置宽高，+40是为了上面有留白
    btn.move(button_size_w, button_size_h + 40)
    # 按钮大小
    btn.resize(button_w, button_h)
    # 这里绑定了按钮的事件
    btn.clicked.connect(quick_clicked)


for i in range(len(config_ini)):
    white_button(config_ini[i], 50, 50 * i, 150, 50, config_ini[i])
if __name__ == '__main__':
    if run_code:
        running(run_code)
    else:
        # 显示窗体
        main_window.show()
        # 退出程序，也可以写sys.exit(app.exec())
        sys.exit(app.exec())
