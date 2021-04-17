

#Date: 2021-04-14 09:00:12
#LastEditors: Xerath
#LastEditTime: 2021-04-15 07:52:17
#FilePath: \SNLComlier\NewSyntax.py


from T_and_NT import T,NT

symbols = list()

productions = list()

first_sets = dict()
follow_sets = dict()
predict_sets = dict()
LL1_table = dict()

def sets_init():
    for symbol in NT:
            first_sets[symbol] = set()
            follow_sets[symbol] = set()
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
                    
    
def getFirstFromString(s:str):
    first_set = set()
    if s == "":
        return set('ε')
    #该字符串的first集
    body = s.strip("\n").split(" ")
    count = 0
    while count < len(body):
        tmp = first_sets[body[count]]
        first_set = first_set.union(tmp - first_sets['ε'])
        count += 1
        if 'ε' in tmp :
            # 若其中有空则证明还需要找下一个符号
            if count == len(body):
                first_set.add('ε')
                # 若已经是最后一项则证明此产生式可以产生空，将空加入其first集中
            continue
        else:
            break
            # 否则若不能产生空，则已找到第一个非终极符，将其加入first集中即可。

    return first_set


def getFollowSet():
    changed = True
    
    while changed :
        tmp_sets = follow_sets.copy()
        changed = False
        for nt in NT:
            for production in productions:
                head = production.split(" -> ")[0]
                body = production.split(" -> ")[1].strip("\n").split(" ")

                l = len(body)

                if nt in body:
                    if body.count(nt) == 1:
                        indexes=[body.index(nt)]
                    elif body.count(nt) == 2:
                        indexes=[body.index(nt),l-1-body[::-1].index(nt)]
                    else:
                        print("Opps!")
                    
                    for index in indexes:
                        
                        tmp = getFirstFromString(" ".join(body[index+1:l]))
                        if 'ε' in tmp:
                            follow_sets[nt] = follow_sets[nt].union(tmp-set('ε'))
                            follow_sets[nt] = follow_sets[nt].union(follow_sets[head])
                            #该串中有空则应加入产生该串的产生式的follow集
                        else:
                            follow_sets[nt] = follow_sets[nt].union(tmp)
        if(tmp_sets != follow_sets):
            changed = True


def getPredictSet():
    for production in productions:
        production = production.strip("\n")
        head = production.split(" -> ")[0]
        body = production.split(" -> ")[1]
        tmp = getFirstFromString(body)
        if 'ε' not in tmp:
            predict_sets[production] = tmp
        else:
            predict_sets[production] = (tmp -set('ε')).union(follow_sets[head])


def getLL1Table():
    for production in productions:
        production = production.strip("\n")
        head = production.split(" -> ")[0]
        body = production.split(" -> ")[1].strip(" ")
        for t in predict_sets[production]:
            LL1_table[(t, head)] = body


getFirstSet()
# f = open("FirstSet3.txt","w",encoding='utf-8')
# SNT =list(NT)
# SNT.sort()
# for nt in SNT:
#     tmp = list(first_sets[nt])
#     tmp.sort()
#     f.write(nt+"\t"+str(tmp)+"\n")
# f.close()

getFollowSet()
# f = open("FollowSet3.txt","w",encoding='utf-8')
# SNT =list(NT)
# SNT.sort()
# for nt in SNT:
#     tmp = list(follow_sets[nt])
#     tmp.sort()
#     f.write(nt+"\t"+str(tmp)+"\n")
# f.close()

getPredictSet()
f = open("PredictSet.txt", "w", encoding='utf-8')
for i in predict_sets:

    f.write(i.strip("\n") + "\t"+str(predict_sets[i])+"\n")
f.close()

getLL1Table()
f = open("LL(1)Table.txt", "w", encoding='utf-8')
for i in LL1_table:

    f.write(i[1]+" -> "+i[0]+" : "+i[1]+" -> "+LL1_table[i]+"\n")
f.close()


for production in productions:
    production = production.strip("\n")
    head = production.split(" -> ")[0]
    body = production.split(" -> ")[1].strip(" ").split(" ")
    l = len(body)
    for element in body:
        # if body.index(element) + body[::-1].index(element) != l-1:
        #     print("Opps!")
        #     print(production+"\t"+element)
        if body.count(element) > 2:
            print("Opps!")
            print(production+"\t"+element)


class Token:
    def __init__(self,token: str, info: str, line: int) -> None:
        self.token = token
        self.info = info
        self.line = line


f = open("TokenList.txt", "r", encoding='utf-8')
raw_tokens = f.readlines()
f.close()
TokenList = []
for raw_token in raw_tokens:
    content = raw_token.strip("\n").split("\t")
    token = content[0]
    info = content[1]
    line = content[2]
    TokenList.append(Token(token, info, line))

for token in TokenList:
    if token.token not in T:
        print(token.token)


class SyntaxTreeNode:
    def __init__(self, token, info):
        self.token = token
        self.info = info
        self.children = []
        self.father = None

    def insertChild(self,node):
        self.children.append(node)
        node.father = self

    def step(self):
        tmp_node = self
        while(tmp_node.father.children[::-1].index(tmp_node) == 0):
            tmp_node = tmp_node.father
        tmp_node = tmp_node.father.children[tmp_node.father.children.index(tmp_node)+1]
        return tmp_node




root = SyntaxTreeNode("Program","ROOT")
cur_node = root

symbol_stack = []
symbol_stack.append("Program")

def generateSyntaxTree():
    global symbol_stack
    global cur_node
    for token in TokenList:
        while token.token != symbol_stack[0]:
            try:
                body = LL1_table[(token.token,symbol_stack[0])].strip("").split(" ")
                # 得到能产生该终极符的产生式右部
                symbol_stack.pop(0)
                # 弹出原先的非终极符
                symbol_stack = body + symbol_stack
                # 加入产生的右部
                for element in body:
                    cur_node.insertChild(SyntaxTreeNode(token=element,info = ""))
                cur_node = cur_node.children[0]

            except KeyError:
                print(token.token+"\t"+symbol_stack[0])
                return

        print(str(symbol_stack)+" "+cur_node.token)
        symbol_stack.pop(0)
        cur_node.info = token.info
        cur_node.token = token.token
        cur_node = cur_node.step()
        # 若成功匹配，则语法树回退到上一级



generateSyntaxTree()