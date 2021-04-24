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


//Դ��������
int line=1;
//ע�������ʶ
bool NoIn =false;
//������
string KeyWord[63]={
    "BEGIN","END","INTEGER","CHAR","PROGRAM","ARRAY","OF","RECORD","VAR","PROCEDURE","IF","THEN","ELSE","FI","WHILE","DO","ENDWH","READ","WRITE","RETURN","TYPE",
    "Begin","End","Integer","Char","Program","Array","Of","Record","Var","Procedure","If","Then","Else","Fi","While","Do","Endwh","Read","Write","Return","Type",
    "begin","end","integer","char","program","array","of","record","var","procedure","if","then","else","fi","while","do","endwh","read","write","return","type"};
//���ַ��ֽ��
char Separater[13]={',','+','-','*','/',';','.','<','=','[',']','(',')'};
string Separater0="EOF";
//��ʽ��
char Filter[4]={' ','\t','\r','\n'};
//��ʶ��
const string ID="ID";
//�޷�������
const string INTC="INTC";


/*�ʷ�����������*/
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


/*�ʷ��������̺���*/
void Scanner(FILE *source,FILE *obj){
	string  word="";
	char curChar=' ';
	//�Զ���
	while((curChar=fgetc(source))!=EOF){
        if(curChar=='\n') line++;
		word="";
		if(IsFilter(curChar)){}//�ж��Ƿ�Ϊ��ʽ��
		else if(IsUpLetter(curChar)||IsLowLetter(curChar)){//�ж��Ƿ�Ϊ�ؼ���
			while(IsUpLetter(curChar)||IsLowLetter(curChar)||IsDigit(curChar)){
				word+=curChar;
				curChar=fgetc(source);
			}
			if(IsSeparater0(word)){//������ַ��ֽ��EOF
			    fseek(source,-1,SEEK_CUR);//�ļ�ָ�����һ�ֽ�
			    OutPrint(word,obj);
			}else if(IsKeyWord(word,obj)){//�ؼ���
                fseek(source,-1,SEEK_CUR);//�ļ�ָ�����һ�ֽ�
            }else{//�����ʶ��
				fseek(source,-1,SEEK_CUR);//�ļ�ָ�����һ�ֽ�
				if(NoIn==false){fprintf(obj,"ID\t%s\t%d\n",word.data(),line);/*cout<<ID<<' '<<word<<' '<<line<<endl;*/}
			}
		}
		else if(IsDigit(curChar)){//�ж��Ƿ�Ϊ����
			while(IsDigit(curChar)){
				word+=curChar;
				curChar=fgetc(source);
			}
			fseek(source,-1,SEEK_CUR);//�ļ�ָ�����1�ֽ�
            //����޷�������
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
				}else fseek(source,-1,SEEK_CUR);//�ļ�ָ�����һ�ֽ�
				OutPrint(word,obj);
				break;
			}
			case ':':
			{
                word+=curChar;//.
			    curChar=fgetc(source);
			    if(curChar=='='){
					    word+=curChar;//=
				}else fseek(source,-1,SEEK_CUR);//�ļ�ָ�����һ�ֽ�
				OutPrint(word,obj);
				break;
			}
			case '{': {NoIn=true;break;}
			case '}': {NoIn=false;break;}
			default :if(NoIn==false){/*cout<<"\""<<curChar<<"\":Wrong!"<<endl;*/}
		}
	}
}

/*�ʷ��������ܺ���*/
//ͨ�����
void OutPrint(string word,FILE *obj){
    if(NoIn==false){fprintf(obj,"%s\t%s\t%d\n",word.data(),word.data(),line);/*cout<<word<<' '<<word<<' '<<line<<endl;*/}
}

//�ж���������Ƿ�Ϊ�ؼ���
bool IsKeyWord(string word,FILE *obj){
	for(int i=0;i<63;i++){
		if(KeyWord[i]==word&&NoIn==false){//����ؼ���
		    string UpperKey;
		    transform(word.begin(),word.end(),back_inserter(UpperKey),::toupper);//תΪ��д
		    OutPrint(UpperKey,obj);
            return true;
        }
    }
	return false;
}

//�ж���������Ƿ�Ϊ���ַ��ֽ��
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

//�ж���������Ƿ�Ϊ��ʽ��
bool IsFilter(char ch){
	for(int i=0;i<4;i++){
		if(Filter[i]==ch){return true;}
	}
	return false;
}

//�ж���������Ƿ�Ϊ��д��ĸ
bool IsUpLetter(char ch){
	if(ch>='A'&&ch<='Z'){return true;}
	return false;
}

//�ж���������Ƿ�ΪСд��ĸ
bool IsLowLetter(char ch){
	if(ch>='a'&&ch<='z'){return true;}
	return false;
}

//�ж���������Ƿ�Ϊ�޷�������
bool IsDigit(char ch){
	if(ch>='0'&&ch<='9')return true;
	return false;
}
