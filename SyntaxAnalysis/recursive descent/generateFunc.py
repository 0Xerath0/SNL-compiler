from PredictSet import predict_sets
from T_and_NT import T, NT
import os
os.chdir(os.path.realpath(__file__)+"\\..")

class_define = "class RDParser:\n\tdef __init__(self):\n\t\tself.symbol_stack = []\n\t\tself.token_list = []\n\n\n"
functions = dict()
T.remove('ε')
for nt in NT:
    functions[nt] = "\tdef {}(self):\n".format(nt)


for i in predict_sets:
    head = i[0]
    body = i[1].split(" ")
    functions[head] += "\t\tif self.token_list[0] in {}:\n".format(str(predict_sets[i]))
    for element in body:
        if element in NT:
            functions[head] += "\t\t\tself.{}()\n".format(element)
        elif element in T:
            functions[head] += "\t\t\tself.Match(\'{}\')\n".format(element)
        elif element == 'ε':
            functions[head] += "\t\t\tpass\n"
        else:
            print("keyErr")
    functions[head] +="\t\t\treturn\n"

Match = "\tdef Match(self,t:str) -> bool:\n\t\tif self.token_list[0] == t:\n\t\t\tself.token_list.pop(0)\n\t\telse:\n\t\t\tprint(\"Err\")\n"

tail = """Paser = RDParser()


class Token:
	def __init__(self, token: str, info: str, line: int) -> None:
		self.token = token
		self.info = info
		self.line = line


f = open("TokenList.txt", "r", encoding='utf-8')
raw_tokens = f.readlines()
f.close()
# raw_tokens.append("#\\tENDING\\t-1")
TokenList = []

for raw_token in raw_tokens:
	content = raw_token.strip("\\n").split("\\t")
	token = content[0]
	info = content[1]
	line = content[2]
	TokenList.append(Token(token, info, line))
Paser.Program()
"""
f = open("functions.py", "w", encoding='utf-8')
f.write(class_define)
f.write(Match)
for i in functions:
    f.write(functions[i]+"")
f.write(tail)

