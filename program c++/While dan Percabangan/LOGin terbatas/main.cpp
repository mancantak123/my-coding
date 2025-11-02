#include <iostream>
using namespace std;

int main(){
    string username,password;
    
    string USERNAME ="orangutan";
    string PASSWORD ="Admin123";
    
    int percobaan = 0;
    
    while(true && percobaan < 3){
        cout<<"username :";
        cin>>username;
        cout<<"password :";
        cin>>password;
        
        if(username == USERNAME && password == PASSWORD){
            cout<<"login berhasil"<<endl;
            break;
        }else{
            cout<<"coba lagi"<<endl;
            percobaan++;
            continue;
        }
    }
    if(percobaan >= 3){
        cout<<"akun anda diblokir karena sudah 3 percobaan untuk login"<<endl;
    }
}