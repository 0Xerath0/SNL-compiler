

#Date: 2021-03-25 09:28:15
#LastEditors: Xerath
#LastEditTime: 2021-03-25 09:28:57
#FilePath: \SNLComlier\NormalGrammer.py

import re
from typing import Counter

origin = open("Grammer.txt","r",encoding="utf-8")
output = open("normalGrammer.txt","w",encoding="utf-8")
content = origin.readlines()
middle_content = []
final_content=[]
for i in content:
    i = re.sub("::="," ::= ",i)
    i = re.sub("\|", " | ", i)
    i = re.sub("\s+"," ",i)
    i = re.sub("\s*\d+\)\s*","",i)
    i = re.sub("\s*\d+\）\s*","",i)
    middle_content.append(i)

line_conut = -1

for i in middle_content:
    if re.search("::=",i):
        final_content.append(i)
        line_conut += 1
    else:
        i = re.sub("^\s+"," ",i)
        final_content[line_conut] += i

for i in final_content:
    output.write(i+"\n")


