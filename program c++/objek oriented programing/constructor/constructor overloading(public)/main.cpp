#include <bits/stdc++.h>
using namespace std;

class Siswa{
    public:
        string nama;
        string kelas;
        int nilai;
        
    Siswa(string name , string k , int N ){    //constructor (menginisiasi!!)
        nama = name;
        kelas = k;
        nilai = N;
    }
    
    void info(){
        cout<<"nama :"<<nama<<endl;
        cout<<"kelas :"<<kelas<<endl;
        cout<<"Nilai :"<<nilai<<endl;
        
    }
};

int main(){
    Siswa siswa1("udin" , "x" , 80);    //overloading
    siswa1.info();
}