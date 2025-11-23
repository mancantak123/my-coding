#include <iostream>
using namespace std;

int main(){
    
    int angka_tebak =36;
    int user;
    
    while(true){
        cout <<"angka Tebak:";
        cin >> user;
        
        if(user < angka_tebak){
            cout<<"nilai Terlalu kecil!!"<<endl;
            continue;
        }else if(user > angka_tebak){
            cout<<"nilai Terlalu besar!!"<<endl;
            continue;
        }else{
            cout<<"jawaban anda benar"<<endl;
            break;
        }
    }
}