#include <bits/stdc++.h>
using namespace std;

string ubah(int bil){
    if(bil == 100){
        return "a+";
    }else if(80 >= bil <= 90){
        return "a";
    }else if(79 >= bil <= 70){
        return "b";   
    }else if (69 >= bil <=60){
        return "c";
    }else{
        return "f";
    }
}

int main(){
    cout<<ubah(90);
}