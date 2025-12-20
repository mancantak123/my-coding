#include<iostream>
using namespace std;

void cek_bilangan(int x){
    if(x % 2 == 0){
        cout<< x <<" ini adalah bilangan genap"<<endl;
    }else{
        cout<< x <<" ini adalah bilangan ganjil"<<endl;
    }
}

int main(){

    cek_bilangan(99);
    cek_bilangan(90);
}