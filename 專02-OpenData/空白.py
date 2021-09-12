import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties # 步驟一
"""
def fun1(x):
        t2=float(t2[x])
        t3=float(t3[x])/t2
        t4=float(t4[x])/t2
        t5=float(t5[x])/t2
        t6=float(t6[x])/t2
        t7=float(t7[x])/t2
        t8=float(t8[x])/t2
        t9=float(t9[x])/t2
        t10=float(t10[x])/t2
        t11=float(t11[x])/t2
        
        labels = '民意代表及主管及經理人員', '專業人員','技術員及助理專業人員',
                 '事務支援人員','服務及銷售工作人員', '農林漁牧業生產人員',
                 '技藝有關工作人員', '機械設備操作及組裝人員','基層技術工及勞力工', 
                 '其他'
        sizes = [t3,t4,t5,t7,t8,t9,t10,t11,t12]
        explode = (0.1, 0.1, 0.1, 0.1,0.1,
                   0.1,0.1,0.1,0.1,0.1)  

        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
                shadow=True, startangle=90)
        ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        
        plt.show()
        
"""


#中文化


plt.rcParams['font.sans-serif'] = ['SimSun'] # 步驟一（替換sans-serif字型）
plt.rcParams['axes.unicode_minus'] = False  # 步驟二（解決座標軸負數的負號顯示問題）





#Plotting categorical variables類別變數


data = {'apple': 10, 'orange': 15, 'lemon': 5, 'lime': 20}
names = list(data.keys())
values = list(data.values())

fig, axs = plt.subplots(1, 3, figsize=(9, 3), sharey=True)
axs[0].bar(names, values)
axs[1].scatter(names, values)
axs[2].plot(names, values)
fig.suptitle('Categorical Plotting')

plt.show()