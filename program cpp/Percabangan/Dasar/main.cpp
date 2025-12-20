#include <iostream>
using namespace std;

int main(){
    int Nilai;
    
    cout << "masukan Nilai: \t";
    cin >> Nilai;
    
    if(Nilai >= 70){
        cout<<"masuk kkm dengan Nilai: : "<<Nilai<<endl;
    }else{
        cout<<"Tidak masuk KKm dengan Nilai : "<<Nilai<<endl;
    }
}