

import re
from typing import Counter

origin = open("Grammer.txt","r",encoding="utf-8")
output = open("normalGrammer.txt","w",encoding="utf-8")
content = origin.readlines()
middle_content = []
final_content=[]
for i in content:
    i = re.sub("（","(",i)
    i = re.sub("）",")",i)
    #conver Chinese quotes to English quotes
    i = re.sub("::="," ::= ",i)
    i = re.sub("\|", " | ", i)
    #split the grammer
    i = re.sub("\s+"," ",i)
    #delete duplicate white space
    i = re.sub("\s*\d+\)\s*","",i)
    #delede the leading number of each line
    middle_content.append(i)

for i in middle_content:
    if re.search("::=",i):
        
        final_content.append(i)
    else:
        i = re.sub("^\s+"," ",i)
        final_content[-1] += i

for i in final_content:
    i = re.sub("\s+"," ",i)
    output.write(i+"\n")


