#include<bits/stdc++.h>
using namespace std;

int main(){

    // pointer adalah alamat dari variabel!!
    int x = 9;
    cout<<"nilai dari x : "<< x <<endl; 
    cout<<"ini adalah alamat dari x :" << &x <<endl;
    
    // decklarasi pointer!!

    int * p;
    cout<<"alamat p :" << p <<endl;

    //definisi
    cout<<" ( * ) mengakses nilai alamat dari variabel dan decklarasi"<<endl;
    cout<<" ( & ) adalah mengambil alamat milik variabel"<<endl;

    cin.get();
}