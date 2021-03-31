from io import StringIO
from T_and_NT import T,NT
import re

symbols = list()



# class Production:
#     def __init__(self, production:str) -> None:
#         self.right_expr = []
#         production = production.split("::=")
#         self.left_expr = production[0].strip(" ")
#         for i in production[1].strip(" ").split("|"):
#             self.right_expr.append(i)



productions = dict()

first_sets = dict()
follow_sets = dict()
predict_sets = dict()



f = open("normalGrammer.txt","r").readlines()
for grammer in f:
    grammer = grammer.strip("\n").split("::=")
    left = grammer[0].strip(" ")
    right = grammer[1].strip(" ").split(" | ")
    productions[left] = right


# print(productions)

#用于获得产生式右部第一个符号
def getFirstSymbol(right_expr:str):
    curSymbol = right_expr.split(" ")[0].strip(" ")
    return curSymbol

    

def getFirstSet(symbol:str):
    right_exprs = productions[symbol]
    l = len(right)
    first_count = 0
    first = set()
    for right_expr in right_exprs:
        curSymbol = getFirstSymbol(right_expr)
        if curSymbol not in T:
            first = first.union(getFirstSet(curSymbol))
        else:
            first.add(curSymbol)
        #不断展开直到找出终极符
        first_count += 1
    return first

f = open("FirstSet.txt","w")

for i in NT:
    sample_first = getFirstSet(i)
    f.write(i+"\t"+str(sample_first)+"\n")

f.close()
        




# class Symbol:
#     def __init__(self, name,isTerminal:bool) -> None:
#         self.name = name
#         self.isTerminal = isTerminal

        