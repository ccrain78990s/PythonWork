#0316  自主練習 題目:

import tkinter as tk
from tkinter import StringVar
from PIL import ImageTk, Image
from tkinter import ttk
#


win = tk.Tk()

def event1():
    global entry1
    global label3Str
    t1=entry1.get()
    print(t1)
    comStr=comboExample.get()
    if comStr=="109年11-12月":
        if t1 in "801" or "820" or "234":
            t1="恭喜中 六獎 200元，請重新輸入末4碼，查詢是否獲得更高獎項"
        elif t1=="8801" or t1=="3820" or t1=="6234":
            t1="恭喜中 五獎 1,000元，請重新輸入末5碼，查詢是否獲得更高獎項"
        elif t1 == "28801" or t1 == "13820" or t1 == "96234":
            t1 = "恭喜中 四獎 4,000元，請重新輸入末6碼，查詢是否獲得更高獎項"
        elif t1 == "028801" or t1 == "813820" or t1 == "896234":
            t1 = "恭喜中 三獎 10,000元，請重新輸入末7碼，查詢是否獲得更高獎項"
        elif t1 == "9028801" or t1 == "2813820" or t1 == "6896234":
            t1 = "恭喜中 二獎 40,000元，請重新輸入末8碼，查詢是否獲得更高獎項"
        elif t1 == "59028801" or t1 == "2813820" or t1 == "6896234":
            t1 = "恭喜中 頭獎 200,000元"
        elif t1=="011" or t1=="427" :
            t1="恭喜中 增開獎 200元"
        elif t1 == "838" or t1 == "297":
            t1 = "請輸入完整8碼 確認是否中獎"
        elif t1 == "39993297" :
            t1 = "恭喜中 特獎 2,000,000 元"
        elif t1 == "77815838":
            t1 = "恭喜中 特別獎 10,000,000 元"
        else:
            t1="無中獎"

        label3Str.set(t1)

    elif  comStr=="109年9-10月":
        if t1 == "826" or t1 == "124" or t1 == "810":
            t1 = "恭喜中 六獎 200元，請重新輸入末4碼，查詢是否獲得更高獎項"
        elif t1 == "0826" or t1 == "3124" or t1 == "5810":
            t1 = "恭喜中 五獎 1,000元，請重新輸入末5碼，查詢是否獲得更高獎項"
        elif t1 == "50826" or t1 == "43124" or t1 == "65810":
            t1 = "恭喜中 四獎 4,000元，請重新輸入末6碼，查詢是否獲得更高獎項"
        elif t1 == "550826" or t1 == "643124" or t1 == "665810":
            t1 = "恭喜中 三獎 10,000元，請重新輸入末7碼，查詢是否獲得更高獎項"
        elif t1 == "8550826" or t1 == "4643124" or t1 == "6665810":
            t1 = "恭喜中 二獎 40,000元，請重新輸入末8碼，查詢是否獲得更高獎項"
        elif t1 == "68550826" or t1 == "84643124" or t1 == "46665810":
            t1 = "恭喜中 頭獎 200,000元"
        elif t1 == "651" or t1 == "341":
            t1 = "恭喜中 增開獎 200元"
        elif t1 == "723" or t1 == "858":
            t1 = "請輸入完整8碼 確認是否中獎"
        elif t1 == "64157858":
            t1 = "恭喜中 特獎 2,000,000 元"
        elif t1 == "42024723":
            t1 = "恭喜中 特別獎 10,000,000 元"
        else:
            t1 = "無中獎"

        label3Str.set(t1)

#視窗調整
win.wm_title("Hello，祝您中獎!!!")     #設定視窗標題
win.minsize(width=600, height=400)                      #視窗最小尺寸
win.maxsize(width=600, height=400)                      #視窗最大尺寸
win.resizable(width=False, height=False)                #是否可調整視窗大小

#背景
backgroundImg = ImageTk.PhotoImage(Image.open("backgroud2.png"))
backgroundLabel =tk.Label(win,image=backgroundImg)
backgroundLabel.place(x=0,y=0)

#下拉式選單
labelTop = tk.Label(win,text = "↓↓↓ 請選擇 兌獎月份 ↓↓↓")
labelTop.place(x=200, y=15)

comboExample = ttk.Combobox(win,            #ttk 要安裝函式庫
                            values=[
                                    "109年11-12月",
                                    "109年9-10月"])
print(dict(comboExample))                   #<----dict?
comboExample.place(x=205, y=50)
comboExample.current(0)
print(comboExample.current(), comboExample.get())


label1 =tk.Label(win,text="請輸入發票末3碼:",font=20)     #放上啥文字 顏色
label1.place(x=30, y=90)                                            #位置

entry1=tk.Entry(win)
entry1.place(x=212,y=90)

img = ImageTk.PhotoImage(Image.open("button3.png"))
btn1 =tk.Button(win,text="轉換",image=img,command=event1)
btn1.place(x=200,y=150)

label2 =tk.Label(win,text="兌獎結果:",font=20)
label2.place(x=30, y=290)


label3Str=StringVar()
label3=tk.Label(win,textvariable=label3Str,font=25)
label3.place(x=140,y=290)



win.mainloop()




