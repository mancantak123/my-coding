#include <bits/stdc++.h>
using namespace std;

class Siswa{
    public:
        string nama;
        string kelas;
        int nilai;
        
    Siswa(){    //constructor (menginisiasi!!)
        nama = "udin";
        kelas = "x";
        nilai = 75;
    }
    
    void info(){
        cout<<"nama :"<<nama<<endl;
        cout<<"kelas :"<<kelas<<endl;
        cout<<"Nilai :"<<nilai<<endl;
        
    }
};

int main(){
    Siswa siswa1;
    siswa1.info();
}