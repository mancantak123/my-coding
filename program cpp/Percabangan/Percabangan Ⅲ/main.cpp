#include <iostream>
using namespace std;

int main(){
    int NILAI,KEHADIRAN;
    
    cout<<"NIlai : ";
    std::cin >>NILAI;
    cout<<"Persentase Kehadiran (no %) :";
    cin>>KEHADIRAN;
    
    if(NILAI >= 75 && KEHADIRAN >= 80){
        cout<<"lulus dengan Nilai "<< NILAI << " dan Persentase Kehadiran "<<KEHADIRAN<<endl;
    }else{
        cout<<"tidak lulus";
    }
    
}