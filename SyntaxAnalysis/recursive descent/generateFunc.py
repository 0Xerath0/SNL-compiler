from  PredictSet import predict_sets
from T_and_NT import T, NT
import  os
os.chdir(os.path.realpath(__file__)+"\\..")

functions = dict()
T.remove('ε')
for nt in NT:
    functions[nt] = "def RD_{}():\n".format(nt)
    functions[nt]+="\tpass\n"
# for t in T:
#     functions[t] = list()
#     functions[t] = "def MATCH_{}():\n".format(t)

f = open("functions.py","w",encoding='utf-8')
for i in functions:
    f.write(functions[i])


