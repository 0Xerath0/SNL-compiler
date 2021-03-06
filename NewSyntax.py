

#Date: 2021-04-14 09:00:12
#LastEditors: Xerath
#LastEditTime: 2021-04-15 07:52:17
#FilePath: \SNLComlier\NewSyntax.py


from T_and_NT import T, NT
import  os
os.chdir(os.path.realpath(__file__)+"\\..")

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
        # if 'ε' not in tmp:
        #     predict_sets[production] = tmp
        # else:
        #     predict_sets[production] = (tmp -set('ε')).union(follow_sets[head])
        if 'ε' not in tmp:
            predict_sets[(head,body)] = tmp
        else:
            predict_sets[(head,body)] = (tmp -set('ε')).union(follow_sets[head])


def getLL1Table():
    for production in productions:
        production = production.strip("\n")
        head = production.split(" -> ")[0]
        body = production.split(" -> ")[1].strip(" ")
        for t in predict_sets[(head,body)]:
            LL1_table[(t,head)] = body


def writeFirstSet():
    f = open("SyntaxAnalysis\essentials\FirstSet.py", "w", encoding='utf-8')
    f.write("first_sets = {\n")
    # SNT = list(NT)
    # SNT.sort()
    # for nt in SNT:
    #     tmp = list(first_sets[nt])
    #     tmp.sort()
    #     f.write(nt + "\t" + str(tmp) + "\n")
    for i in first_sets:
        f.write("\t\""+i.strip("\n") + "\": " + str(first_sets[i]) + ","+"\n")
    f.write("}")
    f.close()

def writeFollowSet():
    f = open("SyntaxAnalysis\essentials\FollowSet.py", "w", encoding='utf-8')
    # SNT = list(NT)
    # SNT.sort()
    f.write("follow_sets = {\n")
    # for nt in SNT:
    for i in follow_sets:
        f.write("\t\""+i.strip("\n") + "\": " + str(follow_sets[i]) + ","+"\n")
    f.write("}")
    f.close()

def writePredictSet():
    f = open("SyntaxAnalysis\essentials\PredictSet.py", "w", encoding='utf-8')
    f.write("predict_sets = {\n")
    for i in predict_sets:
        f.write("\t"+str(i).strip("\n") + ": " + str(predict_sets[i]) + ","+"\n")
    f.write("}")
    f.close()

def writeLL1Table():
    f = open("LL(1)Table.txt", "w", encoding='utf-8')
    for i in LL1_table:
        f.write(i[1] + " -> " + i[0] + " : " + i[1] + " -> " + LL1_table[i] + "\n")
    f.close()

getFirstSet()

getFollowSet()

getPredictSet()

getLL1Table()

writeFirstSet()

writeFollowSet()

writePredictSet()



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
raw_tokens.append("#\tENDING\t-1")
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

node_count = (x for x in range(100000))
class SyntaxTreeNode:
    def __init__(self, token, info):
        self.token = token
        self.info = info
        self.children = []
        self.father = None
        self.sibling = None
        self.id = next(node_count)

    def insertChild(self, node):
        self.children.append(node)
        node.father = self
        node.sibling = self.children

    def step(self):
        global LL1_root
        tmp_node = self

        while tmp_node.id != 0 and tmp_node.sibling[::-1].index(tmp_node) == 0:
            tmp_node = tmp_node.father
            #print(tmp_node.id)
        if tmp_node.id != 0:
            tmp_node = tmp_node.sibling[tmp_node.sibling.index(tmp_node)+1]
        return tmp_node





LL1_root = SyntaxTreeNode("Program", "ROOT")
recursive_descent_root = SyntaxTreeNode("Program", "ROOT")



def generateLL1SyntaxTree():
    global  LL1_root
    symbol_stack = []
    symbol_stack.append("Program")
    symbol_stack.append('#')
    cur_node = LL1_root
    for token in TokenList:
        while token.token != symbol_stack[0]:
            try:
                body = LL1_table[(token.token, symbol_stack[0])].strip("").split(" ")
                # 得到能产生该终极符的产生式右部
                symbol_stack.pop(0)
                # 弹出原先的非终极符
                symbol_stack = body + symbol_stack
                if symbol_stack[0] == 'ε':
                    symbol_stack.pop(0)
                    cur_node.insertChild(SyntaxTreeNode(token='ε', info = "empty"))
                    cur_node = cur_node.step()
                # 加入产生的右部
                else:
                    for element in body:
                        cur_node.insertChild(SyntaxTreeNode(token=element, info = ""))
                    cur_node = cur_node.children[0]

            except KeyError:
                print(token.token+"\t"+symbol_stack[0])
                return

        if token.token == "#":
            print("LL(1) Syntax analysis competed")
            return


        print(str(symbol_stack)+" "+cur_node.token)
        symbol_stack.pop(0)
        cur_node.info = token.info
        cur_node.token = token.token
        cur_node = cur_node.step()
        # 若成功匹配，则语法树回退到上一级

def generateRDSyntaxTree():
    global recursive_descent_root
    node_stack = []
    symbol_stack = []
    symbol_stack.append("Program")
    symbol_stack.append('#')
    cur_node = recursive_descent_root
    node_stack.append(cur_node)
    node_stack.append(SyntaxTreeNode("#","end"))

generateLL1SyntaxTree()

def outputLL1SyntaxTree():
    f = open("LL1.dot", "w", encoding='utf-8')
    count = 0
    node_stack = []
    node_stack.append(LL1_root)
    graphviz_file = []
    dot_relation = []
    graphviz_file.append("digraph g {\n")
    graphviz_file.append("\tnode [shape = record,height=.1];\n")
    while node_stack:
        tmp = node_stack.pop(0)
        if tmp.token == 'ε':
            color = "[color=yellow]"
        elif tmp.token in T:
            color = "[color=red]"
        else:
            color = ""

        graphviz_file.append("\tnode"+str(tmp.id)+"[label = \""+tmp.token+"\\n"+tmp.info+"\"]"+ color+ ";\n")
        # graphviz_file.append("\tnode" + str(tmp.id) + "[label = \"" + tmp.token + "\"];\n")

        for child in tmp.children:
            node_stack.append(child)

            dot_relation.append("\tnode{}".format(tmp.id)+" -> node{};\n".format(child.id))
    for i in graphviz_file:
        f.write(i)

    for i in dot_relation:
        f.write(i)

    f.write("}")
    f.close()

outputLL1SyntaxTree()