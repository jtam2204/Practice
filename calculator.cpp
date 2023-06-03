#include <iostream> 
#include <stdlib.h>
#include <sstream>
using namespace std;


float add(float a, float b){
    return a+b;
}
float subtract(float a, float b){
    return a-b;
}
float multiply(float a, float b){
    return a*b;
}
float division(float a, float b){
    return a/b;
}

int main(){
    string input="";
    while (input!="Y")
    {
        cout<<"Please enter the equation(Y to quit): (at most 10 numbers, no brackets and only +,-,*,/ operators)\n";
        cin>>input;
        int optr=0, pptr=0, lptr=0;
        string list[10];
        char olist[10];
        float result=0, plist[10];
        for (int i = 0; i < input.length(); i++)
        {
            //cout<<i<<" input: "<<input[i]<<"\n";
            if (input[i]!='+'&&input[i]!='-'&&input[i]!='*'&&input[i]!='/'){
                list[lptr]+=input[i];
                //cout<<lptr<<" list: "<<list[lptr]<<"\n";
                if (input[i+1]=='+'||input[i+1]=='-'||input[i+1]=='*'||input[i+1]=='/'||i==input.length()-1){
                    stringstream num;
                    num<<list[lptr];
                    num>>plist[pptr];
                    //cout<<pptr<<" plist: "<<plist[pptr]<<"\n";
                    lptr++;
                    pptr++;
                    //cout<< "pptr: "<< pptr<<"\n";
                    //cout<< "optr: "<< optr<<"\n";
                    if (olist[optr-1]=='*'||olist[optr-1]=='/'){
                        float num1=plist[pptr-2], num2=plist[pptr-1];
                        //cout<<num1<<olist[optr-1]<<num2<<"\n";
                        switch (olist[optr-1])
                        {
                        case '*':
                            plist[pptr-2]=multiply(num1,num2);
                            pptr--;
                            break;
                        case '/':
                            plist[pptr-2]=division(num1,num2);
                            pptr--;
                            break;
                        }
                        optr--;
                    }
                }
            } else {
                olist[optr]=input[i];
                //cout<<optr<<" olist: "<<olist[optr]<<"\n";
                optr++;
                lptr++;
            } 
        }
        pptr--;
        optr--;
        while (optr>=0)
        {
            //cout<<olist[optr]<<plist[pptr]<<"\n";
            switch (olist[optr])
            {
            case '+':
                plist[pptr-1]=add(plist[pptr-1],plist[pptr]);
                pptr--;
                break;
            case '-':
                plist[pptr-1]=subtract(plist[pptr-1],plist[pptr]);
                pptr--;
                break;
            }
            optr--;
        }
        result=plist[0];
        cout<<"Result: "<<result<<"\n";
    }   
    return 0;
}