#include<iostream>
using namespace std;

void sapaFormal(string nama){
    cout <<"hallo atas nama "<< nama <<endl;
}

void sapaSantai(string nama){
    cout<<"halo "<<nama<<" apakabar bro"<<endl;
}

int main(){

    string nama;
    
    cout<<"nama :";
    cin >> nama;
    sapaSantai(nama);
    sapaFormal(nama);
}
