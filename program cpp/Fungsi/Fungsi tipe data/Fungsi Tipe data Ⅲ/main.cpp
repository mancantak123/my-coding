#include <bits/stdc++.h>
using namespace std;

int chek(int bil){
    if(bil % 2==0){
        return true;
    }else{
        return false;
    }
}

int main() {
    cout<<chek(100);
}