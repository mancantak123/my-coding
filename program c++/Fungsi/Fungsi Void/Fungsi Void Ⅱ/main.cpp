#include<iostream>
using namespace std;
// global variable
int jumlah_orang = 0;

void masuk(){
    jumlah_orang++;
    cout<<"jumlah orang yang masuk :"<<jumlah_orang<<endl;
}

void keluar(){
    if(jumlah_orang <= 0){
        cout<<"didalam tidak ada orang sama sekali"<<endl;
    }else{
        jumlah_orang--;
        if(jumlah_orang <= 0){
            cout<<"tempat tersebut kosong"<<endl;
        }else{
            cout<<"jumlah orang yang masuk :"<<jumlah_orang<<endl;
        }
    }
}


int main(){
    masuk();
    masuk();
    keluar();
    keluar();
    keluar();
}