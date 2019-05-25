import csv
import numpy as np
#from module2 import *
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import random
#print("請選擇要查詢的項目")
t=0
ccsv=4
data=[]
word=[]
while 1:
    str1=str(ccsv)+'r.csv'
    ccsv=str(ccsv)
    dt={0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0,11:0,12:0,13:0,14:0,15:0,16:0,17:0,18:0,19:0,20:0,21:0,22:0,23:0}
    with open(str1, newline='',encoding='utf-8') as csvfile:
        rows = csv.reader(csvfile)
        rows = csv.reader(csvfile, delimiter=',')
        for i in rows:
           if((i[1])=="Stop"):
                continue           
           if(int(i[7]) in dt and i[4]=="2015"):
                st=str(i[8])         
                st=st.replace(',','')
                i[8]=int(st)
                st2=str(i[7])         
                #st2=st2.replace(',','')
                i[7]=int(st2)            
                dt[i[7]]+=int(i[8])
    lists = sorted(dt.items())
    x, y = zip(*lists)
    print(lists)
    print()
    data.append(y)
    t+=1
    ccsv=int(ccsv)
    ccsv+=1
    if(ccsv==8):
        break
 
print(data)
print()
l1=len(data) #列長度 4
l2=len(data[0])#行長度 9
for i,j in sorted(dt.items()):
    word.append(i)
data3=[[0 for j in range(l1)] for i in range(l2)]
for i in range(l2):
    for j in range(l1):
        data3[i][j]=data[j][i]
print(data3)
n_groups = 4
fig, ax = plt.subplots()
index = np.arange(n_groups)
plt.figure(figsize=(10,10))
bar_width = 0.03
opacity = 0.8
rects=[i for i in range(l2)]
#word=["二專","五專","四技","學士","二年制","二技","博士","碩士","x+4x"]
for i in range(len(rects)):
    rects[i]=plt.bar(index+i*bar_width, data3[i], bar_width,
    alpha=opacity,
    color=(random.random(),random.random(),random.random(),random.random()),
    label=word[i])
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
plt.rcParams['axes.unicode_minus'] = False
plt.xlabel('車號')
plt.ylabel('人數')

plt.xticks(index + bar_width, ('108路','12路','55路','58路'))
plt.legend()
plt.tight_layout()
plt.grid()
plt.show()