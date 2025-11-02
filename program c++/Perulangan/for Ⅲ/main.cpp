#include <iostream>
using namespace std;

int main(){
    
    int angka_dasar = 5;
    
    cout<<"Tabel perkalian 5"<<endl;
    
    for(int i =1; i <=10;i++){
        std::cout << i <<"x"<< angka_dasar <<" = "<< angka_dasar*i<<std::endl;
    }
}