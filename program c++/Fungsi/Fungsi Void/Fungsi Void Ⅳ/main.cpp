#include<iostream>
using namespace std;

bool sedang_login = false;

void login(string username , string password){
    string username_admin = "kaja";
    string password_admin = "Admin123";

    if(username == username_admin && password == password_admin){
        cout<<"login berhasil"<<endl;
        sedang_login = true;
    }else{
        cout<<"username atau password salah!!"<<endl;
    }
    
}



int main(){
    string nama,password,a;
    while(true){
        cout<<"login,logout atau tidak : ";
        cin>>a;
        
        if(a == "login"){
            if(sedang_login == true){
                cout<<"anda sudah login"<<endl;
            }else{
                cout<<"username : ";
                cin>>nama;
                cout<<"password : ";
                cin>>password;
                login(nama , password);   
            }
        }else if(a == "logout"){
            if(sedang_login == false){
                cout<<"terjadinya kesalahan"<<endl;
            }else{
                sedang_login = false;
                cout<<"akun anda sudah logout"<<endl;
            }
        }else if(a == "tidak"){
            break;
        }else{
            cout<<"terjadi kesalahan"<<endl;
        }
    }
}