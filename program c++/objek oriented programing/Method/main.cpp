#include<bits/stdc++.h>
using namespace std;

class Siswa{
    public:
        string nama;
        int kecepatan;
        
    void jalan(){ // method(Fungsi) berinteraksi dengan data member!!
        cout<< nama << " berjalan dengan kecepatan " <<kecepatan<<endl;
    }
};

int main(){
    Siswa siswa1;
    siswa1.nama = "udin";
    siswa1.kecepatan = 12;
    
    siswa1.jalan();
    
}