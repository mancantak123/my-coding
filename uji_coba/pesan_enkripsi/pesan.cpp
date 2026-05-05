#include<iostream>
#include<string>
using namespace std;
string huruf = {"abcdefghijklmnopqrstuvwxyz"};

int main(){
    int n;
    string pesan;
    cin>>n;
    getline(cin , pesan);
    string pesan_enk = "";
    
    int ptr;
    if(n < 25){
        ptr = n-1;
    }else{
        cout<< "melebihi index alpabet";
        return 0;
    }
    for(int i=0; i < pesan.length();i++){
        if(pesan[i] == ' '){
            pesan_enk += "_";
            continue;
        }
        for(int j=0; j < 26;j++){
            if(pesan[i] == huruf[j]){
                if(ptr + j < 26){
                    pesan_enk += huruf[ptr + j];
                }else{
                    int m = (ptr+j) - 26;
                    pesan_enk += huruf[m];
                }
            }
        }
    }
    cout<<pesan_enk<<endl;
    return 0;
}