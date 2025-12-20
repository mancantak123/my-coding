#include <iostream>
using namespace std;

int main(){
    string a;
    string Login ="Admin123";
    
    cout<<"Silahkan isi Login >> : ";
    cin >> a;
    
    if(a == Login){
        std::cout << "login Berhasil!!" << std::endl;
    }else{
        cout<<"Login anda salah!! Silahkan isi kembali!!"<<endl;
    }
}