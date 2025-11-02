#include <iostream>
using namespace std;

// program perulangan while nilai ganjil

int main(){
    int a,b;
    
    cout << "nilai awal";
    cin >> a;
    cout << "nilai batas";
    cin >>b;

    while( a <= b){
        if(a % 2 != 0){
            cout << "nilai perulangan ke-"<< a <<endl;
            a++;
        }
    }
}