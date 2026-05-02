#include <bits/stdc++.h>
using namespace std;
// pass by reference !!

void swap(int& p , int &q){
    p = q;
}

int main(){
    int p,q;
    
    cout<<"nilai p :";
    cin>>p;
    cout<<"Nilai q :";
    cin>>q;
    
    cout<<endl;
    
    swap(p , q);
    cout<<"Nilai p :"<<p<<endl;
    cout<<"Nilai q :"<<q<<endl;
    
    
    cin.get();
}