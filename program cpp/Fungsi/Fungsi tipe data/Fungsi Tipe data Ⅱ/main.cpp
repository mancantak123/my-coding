#include <bits/stdc++.h>
using namespace std;

string kelulusan(float lulus){
    if(lulus >= 75){
        return "selamat anda lulus dengan nilai " + to_string(lulus);
    }else{
        return "anda tidak lulus dengan niliai " + to_string(lulus) ;
    }
}

int main(){
    cout<<kelulusan(80)<<endl;
    cout<<kelulusan(70)<<endl;
}