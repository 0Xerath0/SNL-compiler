first_sets = {
	"DeclarePart": {'VAR', 'TYPE', 'PROCEDURE', 'ε'},
	"LoopStm": {'WHILE'},
	"ProcDecPart": {'VAR', 'TYPE', 'PROCEDURE', 'ε'},
	"StmMore": {';', 'ε'},
	"Low": {'INTC'},
	"ConditionalStm": {'IF'},
	"ReturnStm": {'RETURN'},
	"VariMore": {'.', '[', 'ε'},
	"FieldDecMore": {'ARRAY', 'INTEGER', 'CHAR', 'ε'},
	"ProcDecMore": {'PROCEDURE', 'ε'},
	"Term": {'(', 'INTC', 'ID'},
	"Factor": {'(', 'INTC', 'ID'},
	"AssignmentRest": {'.', ':=', '['},
	"TypeDecMore": {'ID', 'ε'},
	"StmList": {'WRITE', 'WHILE', 'READ', 'RETURN', 'IF', 'ID'},
	"FieldDecList": {'INTEGER', 'CHAR', 'ARRAY'},
	"OtherRelE": {'<', '='},
	"CmpOp": {'<', '='},
	"OtherFactor": {'/', '*', 'ε'},
	"ProcName": {'ID'},
	"AssCall": {'(', '[', '.', ':='},
	"Program": {'PROGRAM'},
	"TypeId": {'ID'},
	"InputStm": {'READ'},
	"Variable": {'ID'},
	"IdList": {'ID'},
	"TypeName": {'RECORD', 'ID', 'INTEGER', 'CHAR', 'ARRAY'},
	"CallStmRest": {'('},
	"ArrayType": {'ARRAY'},
	"StructureType": {'RECORD', 'ARRAY'},
	"ActParamList": {'(', 'INTC', 'ID', 'ε'},
	"ProcBody": {'BEGIN'},
	"AddOp": {'+', '-'},
	"VarDecMore": {'CHAR', 'RECORD', 'ID', 'ARRAY', 'INTEGER', 'ε'},
	"IdMore": {',', 'ε'},
	"VarIdList": {'ID'},
	"VarIdMore": {',', 'ε'},
	"VarDeclaration": {'VAR'},
	"FieldVar": {'ID'},
	"OutputStm": {'WRITE'},
	"OtherTerm": {'+', '-', 'ε'},
	"BaseType": {'INTEGER', 'CHAR'},
	"ParamMore": {';', 'ε'},
	"ParamList": {'VAR', 'CHAR', 'RECORD', 'ID', 'ARRAY', 'INTEGER', 'ε'},
	"FieldVarMore": {'[', 'ε'},
	"TypeDeclaration": {'TYPE'},
	"RecType": {'RECORD'},
	"ProcDec": {'PROCEDURE', 'ε'},
	"Stm": {'IF', 'WRITE', 'WHILE', 'ID', 'READ', 'RETURN'},
	"VarDec": {'ε', 'VAR'},
	"ProcDeclaration": {'PROCEDURE'},
	"RelExp": {'(', 'INTC', 'ID'},
	"ParamDecList": {'VAR', 'CHAR', 'RECORD', 'ID', 'INTEGER', 'ARRAY'},
	"ProgramHead": {'PROGRAM'},
	"Param": {'VAR', 'CHAR', 'RECORD', 'ID', 'INTEGER', 'ARRAY'},
	"ProgramBody": {'BEGIN'},
	"MultOp": {'/', '*'},
	"Top": {'INTC'},
	"Invar": {'ID'},
	"TypeDecList": {'ID'},
	"FidMore": {',', 'ε'},
	"Exp": {'(', 'INTC', 'ID'},
	"ActParamMore": {',', 'ε'},
	"FormList": {'ID'},
	"TypeDec": {'TYPE', 'ε'},
	"VarDecList": {'CHAR', 'RECORD', 'ID', 'INTEGER', 'ARRAY'},
	"ProgramName": {'ID'},
	"VAR": {'VAR'},
	"DO": {'DO'},
	"END": {'END'},
	"BEGIN": {'BEGIN'},
	"END.": {'END.'},
	"ε": {'ε'},
	"ARRAY": {'ARRAY'},
	"WRITE": {'WRITE'},
	"[": {'['},
	"OF": {'OF'},
	"TYPE": {'TYPE'},
	".": {'.'},
	"ENDWH": {'ENDWH'},
	"=": {'='},
	"ELSE": {'ELSE'},
	"+": {'+'},
	"INTC": {'INTC'},
	")": {')'},
	"PROGRAM": {'PROGRAM'},
	"*": {'*'},
	"id": {'id'},
	",": {','},
	"PROCEDURE": {'PROCEDURE'},
	"WHILE": {'WHILE'},
	"RETURN": {'RETURN'},
	"CHAR": {'CHAR'},
	"IF": {'IF'},
	"RECORD": {'RECORD'},
	"-": {'-'},
	"(": {'('},
	"/": {'/'},
	"]": {']'},
	"READ": {'READ'},
	"<": {'<'},
	"FI": {'FI'},
	"..": {'..'},
	"ID": {'ID'},
	"THEN": {'THEN'},
	"INTEGER": {'INTEGER'},
	":=": {':='},
	";": {';'},
}