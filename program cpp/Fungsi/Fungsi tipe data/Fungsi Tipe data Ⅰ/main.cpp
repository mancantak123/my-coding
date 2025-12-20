#include <bits/stdc++.h>
using namespace std;

float nilai_Rata2(int ujian ,int ujian2 , int ujian3){
    return (ujian + ujian2 + ujian3)/3;
}

int main(){
    cout<<nilai_Rata2(84,89,45)<<endl;
}