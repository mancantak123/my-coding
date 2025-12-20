#include <bits/stdc++.h>
using namespace std;


int main(){
    int jumlah_tertinggi , jumlah_terendah , total;
    int hari[7] = {12 , 9 , 15 , 7 , 20 ,22 , 18};
    
    jumlah_tertinggi = hari[0];
    jumlah_terendah = hari[0];
    total = 0;
    
    for(int i=1; i < 7;i++){
        
        if(hari[i] > jumlah_tertinggi){
            
            jumlah_tertinggi = hari[i];
            
        }else if(hari[i] < jumlah_terendah){
            
            jumlah_terendah = hari[i];
        }
        
        total += hari[i];
        
    }
    
    cout<<"jumlah tertinggi = "<<jumlah_tertinggi<<endl;
    cout<<"jumlah_terendah = "<<jumlah_terendah<<endl;
    cout<<"total keseluruhan = "<<total<<endl;
}


