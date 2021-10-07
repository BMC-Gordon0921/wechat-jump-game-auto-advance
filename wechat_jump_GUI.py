from tkinter import *
import os, sys

def run():
    os.system('python E:\LeiDian\LDPlayer4\wechat_jump_game-master\wechat_jump_auto_slim.py')

def install_requirements():
    pass


root = Tk()
root.geometry('480x250')
root.title('跳一跳全自动辅助脚本——白墨川原创')
lb1 = Label(root, text='请打开微信跳一跳小程序并点击开始游戏')
lb1.pack()
lb2 = Label(root, text='请将手机通过数据线与电脑连接')
lb2.pack()
lb3 = Label(root, text='请注意：若 AI 出现失误导致游戏结束，\n请手动按下 再来一局 按钮')
lb3.pack()
lb4 = Label(root, text='请将自己电脑中的wechat_jump_auto_slim.py的绝对路径写入os.system的路径中')
lb4.pack()

button_requirments = Button(root, text='按我安装必要的扩展', command=install_requirements )
button_requirments.pack()
button = Button(root, text='按我开始自动跳一跳 ：）', command=run )
button.pack()
root.mainloop()
