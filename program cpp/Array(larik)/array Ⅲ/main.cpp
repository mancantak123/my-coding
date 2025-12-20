#include<bits/stdc++.h>
using namespace std;
//operasi & logika
int main(){
    int stok[5]= {10,0,15,0,20};
    int barang_habis = 0;

    for(int i=0; i<5;i++){
        if(stok[i] == 0){
            barang_habis++;
        }
    }
    cout<<barang_habis<<endl;
}