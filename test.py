

#Date: 2021-04-14 10:32:30
#LastEditors: Xerath
#LastEditTime: 2021-04-14 10:32:31
#FilePath: \SNLComlier\test.py

f = open("generatedSets.txt","r",encoding='utf-8').readlines()
f.sort()
fo = open("generatedSets2.txt","w",encoding='utf-8')
for i in f:
    fo.write(i)
fo.close()