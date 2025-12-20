#include <bits/stdc++.h>
using namespace std;
//operasi dalam array!!

int main(){
    int suhu[5]{29,31,32,30,28};
    int jumlah = 0;

    for(int i=1; i <= 5;i++){
        jumlah += suhu[i];
    }

    cout<<jumlah/5<<endl;
}