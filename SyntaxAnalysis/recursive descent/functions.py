class RDParser:
	def __init__(self):
		self.symbol_stack = []
		self.token_list = []


	def Match(self,t:str) -> bool:
		if self.token_list[0] == t:
			self.token_list.pop(0)
			print("Matched {}".format(t))
		else:
			print("Err")
	def Top(self):
		if self.token_list[0] in {'INTC'}:
			self.Match('INTC')
			return
	def VarDec(self):
		if self.token_list[0] in {'BEGIN', 'PROCEDURE'}:
			pass
			return
		if self.token_list[0] in {'VAR'}:
			self.VarDeclaration()
			return
	def VarDeclaration(self):
		if self.token_list[0] in {'VAR'}:
			self.Match('VAR')
			self.VarDecList()
			return
	def CmpOp(self):
		if self.token_list[0] in {'<'}:
			self.Match('<')
			return
		if self.token_list[0] in {'='}:
			self.Match('=')
			return
	def FidMore(self):
		if self.token_list[0] in {')', ';'}:
			pass
			return
		if self.token_list[0] in {','}:
			self.Match(',')
			self.FormList()
			return
	def OtherTerm(self):
		if self.token_list[0] in {')', 'FI', ',', ']', 'THEN', '<', 'ELSE', 'ENDWH', 'END', ';', 'DO', '='}:
			pass
			return
		if self.token_list[0] in {'+', '-'}:
			self.AddOp()
			self.Exp()
			return
	def Exp(self):
		if self.token_list[0] in {'ID', '(', 'INTC'}:
			self.Term()
			self.OtherTerm()
			return
	def ProgramName(self):
		if self.token_list[0] in {'ID'}:
			self.Match('ID')
			return
	def DeclarePart(self):
		if self.token_list[0] in {'VAR', 'BEGIN', 'PROCEDURE', 'TYPE'}:
			self.TypeDec()
			self.VarDec()
			self.ProcDec()
			return
	def RelExp(self):
		if self.token_list[0] in {'ID', '(', 'INTC'}:
			self.Exp()
			self.OtherRelE()
			return
	def VarDecList(self):
		if self.token_list[0] in {'ARRAY', 'INTEGER', 'RECORD', 'ID', 'CHAR'}:
			self.TypeName()
			self.VarIdList()
			self.Match(';')
			self.VarDecMore()
			return
	def TypeName(self):
		if self.token_list[0] in {'CHAR', 'INTEGER'}:
			self.BaseType()
			return
		if self.token_list[0] in {'ARRAY', 'RECORD'}:
			self.StructureType()
			return
		if self.token_list[0] in {'ID'}:
			self.Match('ID')
			return
	def Term(self):
		if self.token_list[0] in {'ID', '(', 'INTC'}:
			self.Factor()
			self.OtherFactor()
			return
	def IdMore(self):
		if self.token_list[0] in {';'}:
			pass
			return
		if self.token_list[0] in {','}:
			self.Match(',')
			self.IdList()
			return
	def BaseType(self):
		if self.token_list[0] in {'INTEGER'}:
			self.Match('INTEGER')
			return
		if self.token_list[0] in {'CHAR'}:
			self.Match('CHAR')
			return
	def ReturnStm(self):
		if self.token_list[0] in {'RETURN'}:
			self.Match('RETURN')
			self.Match('(')
			self.Exp()
			self.Match(')')
			return
	def ProcDecMore(self):
		if self.token_list[0] in {'BEGIN'}:
			pass
			return
		if self.token_list[0] in {'PROCEDURE'}:
			self.ProcDeclaration()
			return
	def ActParamMore(self):
		if self.token_list[0] in {')'}:
			pass
			return
		if self.token_list[0] in {','}:
			self.Match(',')
			self.ActParamList()
			return
	def TypeDecMore(self):
		if self.token_list[0] in {'VAR', 'BEGIN', 'PROCEDURE'}:
			pass
			return
		if self.token_list[0] in {'ID'}:
			self.TypeDecList()
			return
	def CallStmRest(self):
		if self.token_list[0] in {'('}:
			self.Match('(')
			self.ActParamList()
			self.Match(')')
			return
	def AssignmentRest(self):
		if self.token_list[0] in {'[', '.', ':='}:
			self.VariMore()
			self.Match(':=')
			self.Exp()
			return
	def ProcDecPart(self):
		if self.token_list[0] in {'VAR', 'BEGIN', 'PROCEDURE', 'TYPE'}:
			self.DeclarePart()
			return
	def ProcDec(self):
		if self.token_list[0] in {'BEGIN'}:
			pass
			return
		if self.token_list[0] in {'PROCEDURE'}:
			self.ProcDeclaration()
			return
	def Variable(self):
		if self.token_list[0] in {'ID'}:
			self.Match('ID')
			self.VariMore()
			return
	def VariMore(self):
		if self.token_list[0] in {'/', ',', ']', '-', 'ELSE', 'END', ';', 'DO', ')', 'FI', 'THEN', '<', '+', 'ENDWH', '*', ':=', '='}:
			pass
			return
		if self.token_list[0] in {'['}:
			self.Match('[')
			self.Exp()
			self.Match(']')
			return
		if self.token_list[0] in {'.'}:
			self.Match('.')
			self.FieldVar()
			return
	def ParamList(self):
		if self.token_list[0] in {')'}:
			pass
			return
		if self.token_list[0] in {'ARRAY', 'INTEGER', 'RECORD', 'VAR', 'ID', 'CHAR'}:
			self.ParamDecList()
			return
	def FieldDecList(self):
		if self.token_list[0] in {'CHAR', 'INTEGER'}:
			self.BaseType()
			self.IdList()
			self.Match(';')
			self.FieldDecMore()
			return
		if self.token_list[0] in {'ARRAY'}:
			self.ArrayType()
			self.IdList()
			self.Match(';')
			self.FieldDecMore()
			return
	def TypeDec(self):
		if self.token_list[0] in {'VAR', 'BEGIN', 'PROCEDURE'}:
			pass
			return
		if self.token_list[0] in {'TYPE'}:
			self.TypeDeclaration()
			return
	def ProgramBody(self):
		if self.token_list[0] in {'BEGIN'}:
			self.Match('BEGIN')
			self.StmList()
			self.Match('END')
			return
	def ConditionalStm(self):
		if self.token_list[0] in {'IF'}:
			self.Match('IF')
			self.RelExp()
			self.Match('THEN')
			self.StmList()
			self.Match('ELSE')
			self.StmList()
			self.Match('FI')
			return
	def RecType(self):
		if self.token_list[0] in {'RECORD'}:
			self.Match('RECORD')
			self.FieldDecList()
			self.Match('END')
			return
	def Invar(self):
		if self.token_list[0] in {'ID'}:
			self.Match('ID')
			return
	def TypeDecList(self):
		if self.token_list[0] in {'ID'}:
			self.TypeId()
			self.Match('=')
			self.TypeName()
			self.Match(';')
			self.TypeDecMore()
			return
	def VarIdMore(self):
		if self.token_list[0] in {';'}:
			pass
			return
		if self.token_list[0] in {','}:
			self.Match(',')
			self.VarIdList()
			return
	def OtherFactor(self):
		if self.token_list[0] in {')', 'FI', ',', ']', 'THEN', '-', '<', 'ELSE', '+', 'END', 'ENDWH', ';', 'DO', '='}:
			pass
			return
		if self.token_list[0] in {'/', '*'}:
			self.MultOp()
			self.Term()
			return
	def OutputStm(self):
		if self.token_list[0] in {'WRITE'}:
			self.Match('WRITE')
			self.Match('(')
			self.Exp()
			self.Match(')')
			return
	def ProgramHead(self):
		if self.token_list[0] in {'PROGRAM'}:
			self.Match('PROGRAM')
			self.ProgramName()
			return
	def MultOp(self):
		if self.token_list[0] in {'*'}:
			self.Match('*')
			return
		if self.token_list[0] in {'/'}:
			self.Match('/')
			return
	def AssCall(self):
		if self.token_list[0] in {'[', '.', ':='}:
			self.AssignmentRest()
			return
		if self.token_list[0] in {'('}:
			self.CallStmRest()
			return
	def ActParamList(self):
		if self.token_list[0] in {')'}:
			pass
			return
		if self.token_list[0] in {'ID', '(', 'INTC'}:
			self.Exp()
			self.ActParamMore()
			return
	def IdList(self):
		if self.token_list[0] in {'ID'}:
			self.Match('ID')
			self.IdMore()
			return
	def OtherRelE(self):
		if self.token_list[0] in {'<', '='}:
			self.CmpOp()
			self.Exp()
			return
	def ParamMore(self):
		if self.token_list[0] in {')'}:
			pass
			return
		if self.token_list[0] in {';'}:
			self.Match(';')
			self.ParamDecList()
			return
	def FormList(self):
		if self.token_list[0] in {'ID'}:
			self.Match('ID')
			self.FidMore()
			return
	def VarIdList(self):
		if self.token_list[0] in {'ID'}:
			self.Match('ID')
			self.VarIdMore()
			return
	def FieldDecMore(self):
		if self.token_list[0] in {'END'}:
			pass
			return
		if self.token_list[0] in {'CHAR', 'INTEGER', 'ARRAY'}:
			self.FieldDecList()
			return
	def ArrayType(self):
		if self.token_list[0] in {'ARRAY'}:
			self.Match('ARRAY')
			self.Match('[')
			self.Low()
			self.Match('..')
			self.Top()
			self.Match(']')
			self.Match('OF')
			self.BaseType()
			return
	def ParamDecList(self):
		if self.token_list[0] in {'ARRAY', 'INTEGER', 'RECORD', 'VAR', 'ID', 'CHAR'}:
			self.Param()
			self.ParamMore()
			return
	def StmList(self):
		if self.token_list[0] in {'WRITE', 'READ', 'IF', 'ID', 'WHILE', 'RETURN'}:
			self.Stm()
			self.StmMore()
			return
	def FieldVar(self):
		if self.token_list[0] in {'ID'}:
			self.Match('ID')
			self.FieldVarMore()
			return
	def Param(self):
		if self.token_list[0] in {'ARRAY', 'INTEGER', 'RECORD', 'ID', 'CHAR'}:
			self.TypeName()
			self.FormList()
			return
		if self.token_list[0] in {'VAR'}:
			self.Match('VAR')
			self.TypeName()
			self.FormList()
			return
	def ProcDeclaration(self):
		if self.token_list[0] in {'PROCEDURE'}:
			self.Match('PROCEDURE')
			self.ProcName()
			self.Match('(')
			self.ParamList()
			self.Match(')')
			self.Match(';')
			self.ProcDecPart()
			self.ProcBody()
			self.ProcDecMore()
			return
	def LoopStm(self):
		if self.token_list[0] in {'WHILE'}:
			self.Match('WHILE')
			self.RelExp()
			self.Match('DO')
			self.StmList()
			self.Match('ENDWH')
			return
	def ProcName(self):
		if self.token_list[0] in {'ID'}:
			self.Match('ID')
			return
	def Program(self):
		if self.token_list[0] in {'PROGRAM'}:
			self.ProgramHead()
			self.DeclarePart()
			self.ProgramBody()
			self.Match('.')
			return
	def FieldVarMore(self):
		if self.token_list[0] in {'/', ',', ']', '-', 'ELSE', 'END', ';', 'DO', ')', 'FI', 'THEN', '<', '+', 'ENDWH', '*', ':=', '='}:
			pass
			return
		if self.token_list[0] in {'['}:
			self.Match('[')
			self.Exp()
			self.Match(']')
			return
	def Stm(self):
		if self.token_list[0] in {'IF'}:
			self.ConditionalStm()
			return
		if self.token_list[0] in {'WHILE'}:
			self.LoopStm()
			return
		if self.token_list[0] in {'READ'}:
			self.InputStm()
			return
		if self.token_list[0] in {'WRITE'}:
			self.OutputStm()
			return
		if self.token_list[0] in {'RETURN'}:
			self.ReturnStm()
			return
		if self.token_list[0] in {'ID'}:
			self.Match('ID')
			self.AssCall()
			return
	def TypeId(self):
		if self.token_list[0] in {'ID'}:
			self.Match('ID')
			return
	def VarDecMore(self):
		if self.token_list[0] in {'BEGIN', 'PROCEDURE'}:
			pass
			return
		if self.token_list[0] in {'ARRAY', 'INTEGER', 'RECORD', 'ID', 'CHAR'}:
			self.VarDecList()
			return
	def StmMore(self):
		if self.token_list[0] in {'ENDWH', 'FI', 'ELSE', 'END'}:
			pass
			return
		if self.token_list[0] in {';'}:
			self.Match(';')
			self.StmList()
			return
	def InputStm(self):
		if self.token_list[0] in {'READ'}:
			self.Match('READ')
			self.Match('(')
			self.Invar()
			self.Match(')')
			return
	def ProcBody(self):
		if self.token_list[0] in {'BEGIN'}:
			self.ProgramBody()
			return
	def Low(self):
		if self.token_list[0] in {'INTC'}:
			self.Match('INTC')
			return
	def Factor(self):
		if self.token_list[0] in {'('}:
			self.Match('(')
			self.Exp()
			self.Match(')')
			return
		if self.token_list[0] in {'INTC'}:
			self.Match('INTC')
			return
		if self.token_list[0] in {'ID'}:
			self.Variable()
			return
	def AddOp(self):
		if self.token_list[0] in {'+'}:
			self.Match('+')
			return
		if self.token_list[0] in {'-'}:
			self.Match('-')
			return
	def TypeDeclaration(self):
		if self.token_list[0] in {'TYPE'}:
			self.Match('TYPE')
			self.TypeDecList()
			return
	def StructureType(self):
		if self.token_list[0] in {'ARRAY'}:
			self.ArrayType()
			return
		if self.token_list[0] in {'RECORD'}:
			self.RecType()
			return
Paser = RDParser()


class Token:
	def __init__(self, token: str, info: str, line: int) -> None:
		self.token = token
		self.info = info
		self.line = line


f = open("TokenList.txt", "r", encoding='utf-8')
raw_tokens = f.readlines()
f.close()
# raw_tokens.append("#\tENDING\t-1")
TokenList = []

for raw_token in raw_tokens:
	content = raw_token.strip("\n").split("\t")
	token = content[0]
	info = content[1]
	line = content[2]
	Paser.token_list.append(token)
	TokenList.append(Token(token, info, line))
Paser.Program()
