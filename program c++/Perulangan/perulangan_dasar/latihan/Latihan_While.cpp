#include <iostream>
using namespace std;

int main(){

    int i,a;

    cout << "Nilai  : ";
    cin >> i;
    cout << "nilai batas : ";
    cin >> a;
    while (i <= a)
    {
        cout << "perulangan ke-"<< i << endl;
        i++;
    }
}