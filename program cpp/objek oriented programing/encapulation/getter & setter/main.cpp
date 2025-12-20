#include <bits/stdc++.h>
using namespace std;

class Siswa{
    private:
        int Nilai;
    
    public:
        string nama;
        
    //setter encapulation!!
    void setnilai(int N){
        if(N > 0 && N < 100){
             Nilai = N;
        }else{
            cout<< "eror"<<endl;
        }
    }
    
    // getter encapulation!!
    int getNilai(){
        return Nilai;
    }
};

int main(){
    Siswa siswa1;
    siswa1.nama = "udin";
    siswa1.setnilai(90);
    cout<<siswa1.getNilai()<<endl;
    siswa1.setnilai(-10);
    cout<<siswa1.getNilai()<<endl;
}