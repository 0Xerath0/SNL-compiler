

#Date: 2021-03-25 10:29:57
#LastEditors: Xerath
#LastEditTime: 2021-03-25 10:31:21
#FilePath: \SNLComlier\getTerminalSymbols.py

import re

grammers = open("normalGrammer.txt","r",encoding="utf-8").readlines()

left_exprs = set()
right_exprs = set()

for grammer in grammers:
    grammer = re.sub("\|"," ",grammer)
    grammer = re.sub("\s+"," ",grammer)
    #此处只寻找终极符，空格和|符号都只起间隔作用，可以不做区分
    expr = grammer.split("::=")
    left_exprs.add(expr[0].strip(" "))#左部只有一个表达式
    # print(expr[1].strip(" "))
    # print(expr[1].split(" "))
    right_exprs.update(set(expr[1].strip(" ").split(" ")))

# for left_expr in left_exprs:
#     if left_expr in right_exprs:
#         right_exprs.remove(left_expr)

right_exprs -= left_exprs

T = open("T_and_NT.py","w",encoding='utf-8')
T.write("NT = {")
for left_expr in left_exprs:
    T.write("\""+left_expr+"\", ")

T.write("}\n")

T.write("T = {")
for right_expr in right_exprs:
    T.write("\""+right_expr+"\", ")

T.write("}\n")