#include <iostream>
using namespace std;

int main(){
    
    int total = 0;
    
    for(int i =1; i<= 20; i++){
        total += i;
    }
    
    std::cout << total << std::endl;
}