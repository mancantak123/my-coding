#include <iostream>
using namespace std;

int main(){
    int SUHU;
    
    cout<<"SUHU :";
    
    cin >>SUHU;
    
    if(SUHU >= 30){
        
        cout << "panas" <<endl;
        
    }else if(SUHU <= 29 && SUHU > 20){
        
        cout << "Normal"<<endl;
        
    }else if(SUHU <= 20){
        
        cout<<"Dingin"<<endl;
        
    }else{
        
        cout<<"Terjadi Kesalahan"<<endl;
    }
}