#include <iostream>
using namespace std;
int main()
{
    int a;
    
    while(true){
        cout<<"masukan nilai angka : ";
        std::cin >> a;
        
        if(a == 0){
            std::cout << "angka anda masukan nilai 0!!" << std::endl;
            break;
        }
    }

    return 0;
}