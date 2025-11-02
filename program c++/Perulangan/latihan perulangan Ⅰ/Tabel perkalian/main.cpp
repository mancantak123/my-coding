#include <iostream>
using namespace std;

int main(){
    std::cout << "selamat datang aplikasi tabel perkalian" << std::endl;
    
    int perkalian;
    string a;
    
    while(true){
        cout<<"perkalian berapa? :";
        std::cin >> perkalian;
        
        cout<<"Tabel perkalian"<<perkalian<<endl;
        for(int i=1; i<= 10;i++){
            cout<< i << " x " <<perkalian<<" = "<< i * perkalian<<endl;
        }
        
        cout<<"lanjut(y/n) :";
        cin>>a;
        if(a == "n"){
            break;
        }
        
        cout<<endl;
    }
    
}