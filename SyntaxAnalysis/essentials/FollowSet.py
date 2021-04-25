follow_sets = {
	"DeclarePart": {'BEGIN'},
	"LoopStm": {'ENDWH', 'ELSE', 'END', 'FI', ';'},
	"ProcDecPart": {'BEGIN'},
	"StmMore": {'ENDWH', 'ELSE', 'END', 'FI'},
	"Low": {'..'},
	"ConditionalStm": {'ENDWH', 'ELSE', 'END', 'FI', ';'},
	"ReturnStm": {'ENDWH', 'ELSE', 'END', 'FI', ';'},
	"VariMore": {'DO', 'END', '*', ';', '-', '/', ']', '<', 'ENDWH', '=', 'ELSE', '+', 'FI', 'THEN', ')', ':=', ','},
	"FieldDecMore": {'END'},
	"ProcDecMore": {'BEGIN'},
	"Term": {'DO', 'END', ';', '-', ']', '<', 'ENDWH', '=', 'ELSE', '+', 'FI', 'THEN', ')', ','},
	"Factor": {'DO', 'END', '*', ';', '-', '/', ']', '<', 'ENDWH', '=', 'ELSE', '+', 'FI', 'THEN', ')', ','},
	"AssignmentRest": {'ENDWH', 'ELSE', 'END', 'FI', ';'},
	"TypeDecMore": {'BEGIN', 'VAR', 'PROCEDURE'},
	"StmList": {'END', 'FI', 'ENDWH', 'ELSE'},
	"FieldDecList": {'END'},
	"OtherRelE": {'THEN', 'DO'},
	"CmpOp": {'(', 'INTC', 'ID'},
	"OtherFactor": {'DO', 'END', ';', '-', ']', '<', 'ENDWH', '=', 'ELSE', '+', 'FI', 'THEN', ')', ','},
	"ProcName": {'('},
	"AssCall": {'ENDWH', 'ELSE', 'END', 'FI', ';'},
	"Program": {'#'},
	"TypeId": {'='},
	"InputStm": {'ENDWH', 'ELSE', 'END', 'FI', ';'},
	"Variable": {'DO', 'END', '*', ';', '-', '/', ']', '<', 'ENDWH', '=', 'ELSE', '+', 'FI', 'THEN', ')', ','},
	"IdList": {';'},
	"TypeName": {';', 'ID'},
	"CallStmRest": {'ENDWH', 'ELSE', 'END', 'FI', ';'},
	"ArrayType": {';', 'ID'},
	"StructureType": {';', 'ID'},
	"ActParamList": {')'},
	"ProcBody": {'PROCEDURE', 'BEGIN'},
	"AddOp": {'(', 'INTC', 'ID'},
	"VarDecMore": {'PROCEDURE', 'BEGIN'},
	"IdMore": {';'},
	"VarIdList": {';'},
	"VarIdMore": {';'},
	"VarDeclaration": {'PROCEDURE', 'BEGIN'},
	"FieldVar": {'DO', 'END', '*', ';', '-', '/', ']', '<', 'ENDWH', '=', 'ELSE', '+', 'FI', 'THEN', ')', ':=', ','},
	"OutputStm": {'ENDWH', 'ELSE', 'END', 'FI', ';'},
	"OtherTerm": {'DO', 'END', ';', ']', '<', 'ENDWH', '=', 'ELSE', 'FI', 'THEN', ')', ','},
	"BaseType": {';', 'ID'},
	"ParamMore": {')'},
	"ParamList": {')'},
	"FieldVarMore": {'DO', 'END', '*', ';', '-', '/', ']', '<', 'ENDWH', '=', 'ELSE', '+', 'FI', 'THEN', ')', ':=', ','},
	"TypeDeclaration": {'BEGIN', 'VAR', 'PROCEDURE'},
	"RecType": {';', 'ID'},
	"ProcDec": {'BEGIN'},
	"Stm": {'ENDWH', 'ELSE', 'END', 'FI', ';'},
	"VarDec": {'PROCEDURE', 'BEGIN'},
	"ProcDeclaration": {'BEGIN'},
	"RelExp": {'THEN', 'DO'},
	"ParamDecList": {')'},
	"ProgramHead": {'VAR', 'TYPE', 'BEGIN', 'PROCEDURE'},
	"Param": {')', ';'},
	"ProgramBody": {'BEGIN', '.', 'PROCEDURE'},
	"MultOp": {'(', 'INTC', 'ID'},
	"Top": {']'},
	"Invar": {')'},
	"TypeDecList": {'BEGIN', 'VAR', 'PROCEDURE'},
	"FidMore": {')', ';'},
	"Exp": {']', ';', '<', 'ENDWH', 'DO', '=', 'ELSE', 'END', 'FI', 'THEN', ')', ','},
	"ActParamMore": {')'},
	"FormList": {')', ';'},
	"TypeDec": {'BEGIN', 'VAR', 'PROCEDURE'},
	"VarDecList": {'PROCEDURE', 'BEGIN'},
	"ProgramName": {'VAR', 'TYPE', 'BEGIN', 'PROCEDURE'},
}