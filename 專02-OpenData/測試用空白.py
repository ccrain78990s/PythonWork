"""
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import matplotlib
import math

def updateGraph():
    #Example function triggered by Tkinter GUI to change matplotlib graphs.
    global currentGraph
    # Clear all graphs drawn in figure
    plt.clf()
    y = []
    if currentGraph == "sin":
        for i in x:
            y.append(math.cos(i))
        currentGraph = "cos"
    else:
        for i in x:
            y.append(math.sin(i))
        currentGraph = "sin"
    plt.plot(x,y)
    fig.canvas.draw()

# 這定義了用於matplotlib的Python GUI後端
matplotlib.use('TkAgg')

# 初始化Tk的實例
root = tk.Tk()
root.title("測試 - matplotlib in TK")

# 初始化matplotlib圖以進行繪圖
fig = plt.figure(1)

# 特殊類型的“畫布”，允許進行matplotlib繪圖
canvas = FigureCanvasTkAgg(fig, master=root)
plot_widget = canvas.get_tk_widget()

# 示例數據（注意：角度的默認計算以弧度為單位）
x = []
for i in range(0, 500):
    x.append(i/10)
y = []
for i in x:
    y.append(math.sin(i))
plt.plot(x, y)

currentGraph = "sin"

# 將圖添加到tkinter小部件
plot_widget.grid(row=0, column=0)
# 在窗口底部創建一個tkinter按鈕，並將其與updateGraph函數鏈接
tk.Button(root,text="Update",command=updateGraph).grid(row=1, column=0)

root.mainloop()
"""
import tkinter
from tkinter import ttk


def go(*args):  # 處理事件，*args表示可變引數
    print(comboxlist.get())  # 列印選中的值


win = tkinter.Tk()  # 構造窗體
comvalue = tkinter.StringVar()  # 窗體自帶的文字，新建一個值
comboxlist = ttk.Combobox(win, textvariable=comvalue)  # 初始化
comboxlist["values"] = ("1", "2", "3", "4")
comboxlist.current(0)  # 選擇第一個
comboxlist.bind("<<ComboboxSelected>>", go)  # 繫結事件,(下拉列表框被選中時，繫結go()函式)
comboxlist.pack()

win.mainloop()  # 進入訊息迴圈
"""
# coding=utf-8
import sys
import tkinter as Tk
import matplotlib
from numpy import arange, sin, pi
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg,NavigationToolbar2Tk
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
matplotlib.use('TkAgg')
root =Tk.Tk()
root.title("指令碼之家測試 - matplotlib in TK")
#設定圖形尺寸與質量
f =Figure(figsize=(5,4), dpi=100)
a = f.add_subplot(111)
t = arange(0.0,3,0.01)
s = sin(2*pi*t)
#繪製圖形
a.plot(t, s)
#把繪製的圖形顯示到tkinter視窗上
canvas =FigureCanvasTkAgg(f, master=root)

canvas.get_tk_widget().pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)
#把matplotlib繪製圖形的導航工具欄顯示到tkinter視窗上
toolbar =NavigationToolbar2Tk(canvas, root)
toolbar.update()
canvas._tkcanvas.pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)
#定義並繫結鍵盤事件處理函式
def on_key_event(event):
    print('you pressed %s'% event.key)
    key_press_handler(event, canvas, toolbar)
    canvas.mpl_connect('key_press_event', on_key_event)
    #按鈕單擊事件處理函式
def _quit():
    #結束事件主迴圈，並銷燬應用程式視窗
    root.quit()
    root.destroy()
    button =Tk.Button(master=root, text='Quit', command=_quit)
    button.pack(side=Tk.BOTTOM)
Tk.mainloop()
"""
import tkinter as tk

class Scrollbar_Example:
    def __init__(self):
        self.window = tk.Tk()

        self.scrollbar = tk.Scrollbar(self.window)
        self.scrollbar.pack(side="right", fill="y")

        self.listbox = tk.Listbox(self.window, yscrollcommand=self.scrollbar.set)
        for i in range(100):
            self.listbox.insert("end", str(i))
        self.listbox.pack(side="left", fill="both")

        self.scrollbar.config(command=self.listbox.yview)

        self.window.mainloop()

if __name__ == '__main__':
    app = Scrollbar_Example()