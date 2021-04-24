#include<iostream>
#include<fstream>
#include<string>
#include<algorithm>

using namespace std;


void Scanner(FILE *,FILE *);
void OutPrint(string,FILE *);
bool IsKeyWord(string,FILE *);
bool IsSeparater(char);
bool IsOperator(char);
bool IsSeparater0(string);
bool IsFilter(char);
bool IsUpLetter(char);
bool IsLowLetter(char);
bool IsDigit(char);


//源程序行数
int line=1;
//注释区域标识
bool NoIn =false;
//保留字
string KeyWord[63]={
    "BEGIN","END","INTEGER","CHAR","PROGRAM","ARRAY","OF","RECORD","VAR","PROCEDURE","IF","THEN","ELSE","FI","WHILE","DO","ENDWH","READ","WRITE","RETURN","TYPE",
    "Begin","End","Integer","Char","Program","Array","Of","Record","Var","Procedure","If","Then","Else","Fi","While","Do","Endwh","Read","Write","Return","Type",
    "begin","end","integer","char","program","array","of","record","var","procedure","if","then","else","fi","while","do","endwh","read","write","return","type"};
//单字符分界符
char Separater[13]={',','+','-','*','/',';','.','<','=','[',']','(',')'};
string Separater0="EOF";
//格式符
char Filter[4]={' ','\t','\r','\n'};
//标识符
const string ID="ID";
//无符号整数
const string INTC="INTC";


/*词法分析主函数*/
int main(){
	char fName[40];
	FILE *socFile;
	FILE *tkFile;
	cout<<"Source program path:";
	while(true){
        cin>>fName;
        if((socFile=fopen(fName,"r"))!=NULL)  break;
        else{
            cout<<"Wrong!"<<endl;
            cout<<"Source program path:";
        }
	}
	if((tkFile=fopen("TokenList.txt","w+"))==NULL) cout<<"Wrong!"<<endl;
	Scanner(socFile,tkFile);
	cout<<"Token has been printed in \"TokenList.txt\".";
	fclose(socFile);
	fclose(tkFile);
	return 0;
}


/*词法分析过程函数*/
void Scanner(FILE *source,FILE *obj){
	string  word="";
	char curChar=' ';
	//自动机
	while((curChar=fgetc(source))!=EOF){
        if(curChar=='\n') line++;
		word="";
		if(IsFilter(curChar)){}//判断是否为格式符
		else if(IsUpLetter(curChar)||IsLowLetter(curChar)){//判断是否为关键字
			while(IsUpLetter(curChar)||IsLowLetter(curChar)||IsDigit(curChar)){
				word+=curChar;
				curChar=fgetc(source);
			}
			if(IsSeparater0(word)){//输出单字符分界符EOF
			    fseek(source,-1,SEEK_CUR);//文件指针后退一字节
			    OutPrint(word,obj);
			}else if(IsKeyWord(word,obj)){//关键字
                fseek(source,-1,SEEK_CUR);//文件指针后退一字节
            }else{//输出标识符
				fseek(source,-1,SEEK_CUR);//文件指针后退一字节
				if(NoIn==false){fprintf(obj,"ID\t%s\t%d\n",word.data(),line);/*cout<<ID<<' '<<word<<' '<<line<<endl;*/}
			}
		}
		else if(IsDigit(curChar)){//判断是否为数字
			while(IsDigit(curChar)){
				word+=curChar;
				curChar=fgetc(source);
			}
			fseek(source,-1,SEEK_CUR);//文件指针后退1字节
            //输出无符号整数
            if(NoIn==false){fprintf(obj,"INTC\t%s\t%d\n",word.data(),line);/*cout<<INTC<<' '<<word<<' '<<line<<endl;*/}
		}
		else switch(curChar){
            case ',':
			case '+':
			case '-':
			case '*':
			case '/':
			case '<':
			case ';':
			case '=':
			case '(':
			case ')':
			case '[':
			case ']':
            case '\'': {word+=curChar;OutPrint(word,obj);break;}
            case '.':
			{
			    word+=curChar;//.
			    curChar=fgetc(source);
			    if(curChar=='.'){
					    word+=curChar;//.
				}else fseek(source,-1,SEEK_CUR);//文件指针后退一字节
				OutPrint(word,obj);
				break;
			}
			case ':':
			{
                word+=curChar;//.
			    curChar=fgetc(source);
			    if(curChar=='='){
					    word+=curChar;//=
				}else fseek(source,-1,SEEK_CUR);//文件指针后退一字节
				OutPrint(word,obj);
				break;
			}
			case '{': {NoIn=true;break;}
			case '}': {NoIn=false;break;}
			default :if(NoIn==false){/*cout<<"\""<<curChar<<"\":Wrong!"<<endl;*/}
		}
	}
}

/*词法分析功能函数*/
//通用输出
void OutPrint(string word,FILE *obj){
    if(NoIn==false){fprintf(obj,"%s\t%s\t%d\n",word.data(),word.data(),line);/*cout<<word<<' '<<word<<' '<<line<<endl;*/}
}

//判断输入参数是否为关键字
bool IsKeyWord(string word,FILE *obj){
	for(int i=0;i<63;i++){
		if(KeyWord[i]==word&&NoIn==false){//输出关键字
		    string UpperKey;
		    transform(word.begin(),word.end(),back_inserter(UpperKey),::toupper);//转为大写
		    OutPrint(UpperKey,obj);
            return true;
        }
    }
	return false;
}

//判断输入参数是否为单字符分界符
bool IsSeparater(char ch){
	for(int i=0;i<13;i++){
		if(Separater[i]==ch){return true;}
	}
	return false;
}
bool IsSeparater0(string word){
	if(word==Separater0){return true;}
	return false;
}

//判断输入参数是否为格式符
bool IsFilter(char ch){
	for(int i=0;i<4;i++){
		if(Filter[i]==ch){return true;}
	}
	return false;
}

//判断输入参数是否为大写字母
bool IsUpLetter(char ch){
	if(ch>='A'&&ch<='Z'){return true;}
	return false;
}

//判断输入参数是否为小写字母
bool IsLowLetter(char ch){
	if(ch>='a'&&ch<='z'){return true;}
	return false;
}

//判断输入参数是否为无符号整数
bool IsDigit(char ch){
	if(ch>='0'&&ch<='9')return true;
	return false;
}
