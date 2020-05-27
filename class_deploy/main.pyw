'''
    时间：2020/04/23 23:10
    版本：V0.1
    功能：快速打开information.py所指定的文件或目录
    目的：
        1. 初衷是为了上网课的时候可以有gui选择上的课
        2. 自动打开笔记文件、课程目录、网页，如果是特定的课则打开指定软件
    不足：不能实现通用化，大多数参数需要自己设置
'''
import sys
from PyQt5 import QtWidgets
from webbrowser import open as open_web
from os import popen
# 导入information.py的列表
from information import *

# print the GUI
# 宽度：按钮150  +留白100
window_width = 250  
# 高度：数量 * 按钮高度50 + 自动取消按钮50 + 留白100
window_height = len(sec_dir) * 50 + 150  
# 声明主程序
app = QtWidgets.QApplication([])  
# 声明主窗口
main_window = QtWidgets.QWidget()  
main_window.resize(window_width, window_height)  # 定义窗口大小
main_window.setWindowTitle('课时环境部署')

# 自动退出按钮 默认自动退出，按下取消
autoquit_code = 0


def judgment_autoquit():
    global autoquit_code
    if autoquit_code == 0:
        # 如果为0则变1，取消自动退出
        autoquit_code = 1
        # 改变按钮的文字
        autoquit.setText('自动退出')  
    elif autoquit_code == 1:
        # 如果为1则变0，变成自动退出
        autoquit_code = 0
        # 改变按钮的文字
        autoquit.setText('取消自动退出')  


autoquit = QtWidgets.QPushButton('取消自动退出', main_window)
# 按钮在窗口的位置宽高，+40是为了上面有留白
autoquit.move(50, len(sec_dir) * 50 + 50)  
# 按钮大小
autoquit.resize(150, 50) 
# 这里绑定了按钮的事件
autoquit.clicked.connect(judgment_autoquit) 


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

    def test_clicked():
        # 根据内容打开对应的次文件夹、笔记、职教云登录界面
        popen("start " + main_dir + button_click)
        popen("start " + main_dir + button_click + "\\笔记\\笔记.md")
        open_web("https://zjy2.icve.com.cn/portal/login.html")
        # 特殊的两门课还需要额外的打开vmware应用
        if button_click in ("linux基础及应用", "虚拟化技术与应用"):
            popen("start F:\\ruanjian\\VM\\vmware.exe")
        if autoquit_code == 0:
            sys.exit()

    btn = QtWidgets.QPushButton(button_ini, main_window)
    # 按钮在窗口的位置宽高，+40是为了上面有留白
    btn.move(button_size_w, button_size_h + 40)  
    # 按钮大小
    btn.resize(button_w, button_h)  
    # 这里绑定了按钮的事件
    btn.clicked.connect(test_clicked)  


for i in range(len(sec_dir)):
    white_button(sec_dir[i], 50, 50 * i, 150, 50, sec_dir[i])

if __name__ == '__main__':
    # 显示窗体
    main_window.show() 
    # 退出程序，也可以写sys.exit(app.exec()) 
    app.exec()  
