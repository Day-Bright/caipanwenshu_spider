
#-*- coding : utf-8 -*-
# coding: utf-8
import json
import os


lll = []
files = os.listdir('C:/Users/Me/Desktop/18_wenshu/src')
for l in files:
    with open('C:/Users/Me/Desktop/18_wenshu/src/'+l, 'r', encoding='unicode_escape') as fp:
        for x in fp:
            x = x[:-1].split('\t')[-2:]
            if x[1] == "\"\"" or x == [] or len(x) != 2:
                continue
            tmp = json.loads(x[0])
            tr = json.loads(x[1]).split('\n')
            try:
                for z in tr:
                    if z.split('(')[1][-1] != ')':
                        print(z)
                tr = [(z.split('(')[0], int(z.split('(')[1][:-1])) for z in tr]
            except Exception as e:
                print(tr)
                print(x)
            tmp["裁判年份"] = tr
            lll.append(tmp)
with open('C:/Users/Me/Desktop/18_wenshu/src/12.json', 'w', encoding='unicode_escape') as fp:
    json.dump(lll, fp)