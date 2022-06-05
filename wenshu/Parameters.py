# {'案件类型':'民事案件','法院名称':'北京市石景山区人民法院','裁判日期':['2014-05-02','2014-05-03']}
# {'案件类型':'民事案件','法院名称':'北京市第一中级人民法院','裁判日期':['2014-05-02','2014-05-03']}
import pandas as pd
dt1 = pd.date_range(start="2015-01-01", end="2015-12-31", freq="D")  # freq="D"表示频率为每一天
k = 0
dt = []
for i in dt1:
    dt.append(str(i)[:10])

all = []
k = 1
x = 100 #时间间隔
for i in range(len(dt)):
    if k == 1:
        all.append(dt[i])
    if k == x:
        all.append(dt[i])
        k = 0
    if i == (len(dt) - 1) and k != (len(dt)-1):
        all.append(dt[i])
    k += 1


if len(all) % 2 == 1:
    del all[-1]


s = 0
f = open('参数.txt', 'a',encoding='utf-8')
for i in range(len(all)):
    if s == 0:
        f.write("{'案件类型':'民事案件','法院名称':'北京市石景山区人民法院','裁判日期':['"+str(all[i]))
        s = 1
    else:
        f.write("','"+str(all[i])+"']} ")
        s = 0

