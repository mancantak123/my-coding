#include<bits/stdc++.h>
using namespace std;
// operasi array & keputusan atau percabangan
int main(){
    int array[7] = {60, 75 , 80 , 40 , 55 , 90 ,100};
    int rata_rata = 0;
    int lulus = 0;

    for(int i=0; i<7;i++){
        rata_rata += array[i];
        if(array[i]>=70){
            lulus++;
        }
    }

    cout<<"rata-rata nilai adalah : "<<rata_rata/7<<" dengan lulus sebanyak :"<<lulus<<endl;
}