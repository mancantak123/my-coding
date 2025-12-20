#include <bits/stdc++.h>
using namespace std;
class Siswa{
    private:
        string kelas;
        string nama;
        int nilai;
    
    void setNilai(int n){
        if(n >= 0 && n <= 100){
            nilai = n;
        }else{
            cout<<"tidak valid"<<endl;
        }
    }
    
    
    public:
        Siswa(string kls , string name , int n){
            kelas = kls;
            nama = name;
            setNilai(n);
        }
        
        void info(){
            cout<<"Kelas : "<<kelas<<endl;
            cout<<"Nama : "<<nama<<endl;
            cout<<"Nilai : "<<nilai<<endl;
        }
        
};

int main(){
    Siswa siswa1("x" , "udin" , 90);
    siswa1.info();
}