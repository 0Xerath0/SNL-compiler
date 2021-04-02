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

def sets_init():
    for symbol in NT:
            first_sets[symbol] = set()
            follow_sets[symbol] = set()
            predict_sets[symbol] = set()

    follow_sets['Program'].add('#')
sets_init()
f = open("normalGrammer.txt","r").readlines()
for grammer in f:
    grammer = grammer.strip("\n").split("::=")
    left = grammer[0].strip(" ")
    right = grammer[1].strip(" ").split(" | ")
    productions[left] = right


# for production in productions:
#     print(production+"\t",productions[production])

#用于获得产生式右部第一个符号
def getFirstSymbol(right_expr:str):
    curSymbol = right_expr.split(" ")[0].strip(" ")
    return curSymbol

    

def getFirstSet(symbol:str):
    right_exprs = productions[symbol]
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


for i in NT:
    sample_first = getFirstSet(i)
    first_sets[i] = sample_first


for i in T:
    first_sets[i] = set(i)


# def getFollowSet():
#     index = 0
#     next = 'a'
#     modified = 1
#     while modified == 1:
#         print("233")
#         modified = 0
#         for symbol in NT:
#         #遍历所有非终极符
#             for leftSymbol in NT:
#                 #此处遍历非终极符目的是为了在遍历所有产生式
#                 right_exprs = productions[leftSymbol]
#                 for right_expr in right_exprs:
#                     symbol_list = right_expr.strip(" ").split(" ")
#                     #将产生式右部拆分为list，便于寻找下一个元素
#                     if symbol in symbol_list:
#                         index = symbol_list.index(symbol)
#                         preFollow_set = follow_sets[symbol]
#                         #找到当前需要找follow集的符号的索引
#                         if index == len(symbol_list) - 1:
#                             follow_sets[symbol] = follow_sets[symbol].union(follow_sets[leftSymbol])

#                         else:
#                             next = symbol_list[index+1]
#                             #其必须拥有下一个元素时才适用此种分析方法
                            
#                             if 'ε' not in first_sets[next]:
#                                 follow_sets[symbol] = first_sets[next]
#                             else:
#                                 follow_sets[symbol] = (first_sets[next]-set('ε')).union(follow_sets[leftSymbol])
#                         if len(follow_sets[symbol].intersection(preFollow_set)) == len(follow_sets[symbol]) == len(preFollow_set):
#                             modified = 0
#                         else:
#                             modified = 1

# getFollowSet()               
# print(type(first_sets['ε']-set('ε')))
# f = open("FollowSet.txt","w")
# for nt in NT:
#     f.write(nt+"\t"+str(follow_sets[nt])+"\n")






            
            








# class Symbol:
#     def __init__(self, name,isTerminal:bool) -> None:
#         self.name = name
#         self.isTerminal = isTerminal

        