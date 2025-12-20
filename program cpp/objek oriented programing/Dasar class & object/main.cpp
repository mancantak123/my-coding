#include<bits/stdc++.h>
using namespace std;

class Siswa{ // template
    public:     // tipe variabel class
        string nama;    // member data
};

int main(){

    Siswa Data1;    // declarasi objek
    Data1.nama = "Udin";        // mengisi value objek (public)
    cout<<"hallo nama ku adalah "<<Data1.nama<<endl;    //output dari object
}