#include<bits/stdc++.h>
using namespace std;

int main(){
    int array[5] = {23 , 34 ,45 ,65 ,100};
    
    cout<<"ini adalah for(perulangan biasa atau berdasarkan index) biasa"<<endl; // iterasi biasa
    for(int i = 0; i < 5; i++){ // 
        cout<<array[i]<<" ";
    }
    cout<<endl;

    cout<<"ini adalah for each(perulangan berdasarkan jumlah elemen)"<<endl; // for each!!
    for(int i : array) {
        cout<< i <<" ";
    }
    cout<<endl;
}