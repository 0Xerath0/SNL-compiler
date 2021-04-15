

#Date: 2021-04-14 09:00:12
#LastEditors: Xerath
#LastEditTime: 2021-04-15 07:52:17
#FilePath: \SNLComlier\NewSyntax.py

#Date: 2021-04-14 09:00:12
#LastEditors: Xerath
#LastEditTime: 2021-04-14 09:00:13
#FilePath: \SNLComlier\NewSyntax.py


from os import readlink
from T_and_NT import T,NT
import re

symbols = list()

productions = list()

first_sets = dict()
follow_sets = dict()
predict_sets = dict()

def sets_init():
    for symbol in NT:
            first_sets[symbol] = set()
            follow_sets[symbol] = set()
            predict_sets[symbol] = set()
    for i in T:
        first_sets[i] = set()
        first_sets[i].add(i)

    follow_sets['Program'].add('#')
sets_init()

f = open("splitedGrammer.txt","r",encoding="utf-8")
productions = f.readlines()
f.close()


def getFirstSet():
    changed = True
    while changed:
        changed = False
        tmpSet = first_sets.copy()

        for production in productions:
            
            head = production.split(" -> ")[0]
            #head即为产生式左部
            body = production.split(" -> ")[1].strip("\n").split(" ")
            #body为产生式右部符号组成的list

            if body[0] in T and body[0] != 'ε':
                first_sets[head].add(body[0])
                continue
            #若不为空且为终极符，则此条产生式已找到终极符，进入下一条产生式即可
            else:
                count = 0
                while(count < len(body)):
                    tmp = first_sets[body[count]]
                    first_sets[head] = first_sets[head].union(tmp-first_sets['ε'])
                    #先把除空以外的部分加入first集中
                    count += 1
                    if 'ε' in tmp :
                        #若其中有空则证明还需要找下一个符号
                        if count == len(body):
                            first_sets[head].add('ε')
                            #若已经是最后一项则证明此产生式可以产生空，将空加入其first集中 
                        continue
                    else:
                        break
                        #否则若不能产生空，则已找到第一个非终极符，将其加入first集中即可。
        if(tmpSet != first_sets):
            changed = True
        #迭代至不发生变化
                    

getFirstSet()
f = open("FirstSet3.txt","w",encoding='utf-8')
SNT =list(NT)
SNT.sort()
for nt in SNT:
    tmp = list(first_sets[nt])
    tmp.sort()
    f.write(nt+"\t"+str(tmp)+"\n")
f.close()

             
