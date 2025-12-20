#include<bits/stdc++.h>
using namespace std;


class Siswa{
    private:
        string nama;
        int umur;
        
        void setNilai(int n){
            if(n >= 15 && n <= 18){
                umur = n;
            }else{
                cout<<"tidak valid!!"<<endl;
            }
        }
        
        
    public:
        Siswa(string na , int u){
            nama = na;
            setNilai(u);
        }
    
    void infoDasar(){
        cout<<"Nama :"<<nama<<endl;
        cout<<"umur :"<<umur<<endl;
    }
};

class SiswaSma : public Siswa{
    private:
        string jurusan;
        
        void setJurusan(string ju){
            if(ju == "IPA"){
                jurusan = "IPA";
                
            }else if(ju == "IPS" ){
                jurusan = "IPS";
                
            }else{
                cout<<"tidak valid"<<endl;
            }
        }
    public:
        SiswaSma(string name , int age, string major )
            : Siswa(name , age) {
                setJurusan(major);
            }
        
        void info(){
            infoDasar();
            cout<<"Jurusan :"<<jurusan<<endl;
        }
};

int main(){
    SiswaSma SISWA1("Udin" , 17 , "IPA");
    SISWA1.info();
    
    cin.get();
}



