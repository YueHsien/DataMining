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

while 1:
    str1='10'+str(ccsv)+'_sdata.csv'
    ccsv=str(ccsv)
    dt={}
    with open(str1, newline='',encoding='utf-8') as csvfile:
        rows = csv.reader(csvfile)
        rows = csv.reader(csvfile, delimiter=',')
        for i in rows:
           if(i[1]=="學校名稱"):
                continue
           if(i[5] not in dt ):
                st=str(i[6])         
                st=st.replace(',','')
                i[6]=int(st)
                dt.setdefault(i[5],int(i[6]))            
           elif(i[5] in dt ):
                st=str(i[6])         
                st=st.replace(',','')
                i[6]=int(st)
                dt[i[5]]+=int(i[6])
    dt.pop('', None)
    lists = sorted(dt.items())
    x, y = zip(*lists)
    data.append(y)
    t+=1
    ccsv=int(ccsv)
    ccsv+=1
    if(ccsv==8):
        break
 
print(data)
l1=len(data) #列長度 4
l2=len(data[0])#行長度 9
data3=[[0 for j in range(l1)] for i in range(l2)]
for i in range(l2):
    for j in range(l1):
        data3[i][j]=data[j][i]
n_groups = 4
fig, ax = plt.subplots()
index = np.arange(n_groups)
plt.figure(figsize=(10,10))
bar_width = 0.05
opacity = 0.8
rects=[1,2,3,4,5,6,7,8,9]
word=["二專","五專","四技","學士","二年制","二技","博士","碩士","x+4x"]
for i in range(len(rects)):
    rects[i]=plt.bar(index+i*bar_width, data3[i], bar_width,
    alpha=opacity,
    color=(random.random(),random.random(),random.random(),random.random()),
    label=word[i])
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
plt.rcParams['axes.unicode_minus'] = False
plt.xlabel('年度')
plt.ylabel('人數')

plt.xticks(index + bar_width, ('104','105','106','107'))
plt.legend()
plt.tight_layout()
plt.grid()
plt.show()