#include <bits/stdc++.h>
using namespace std;

string chekbil(int n){
    if(n <= 1) return "BUKAN";
    for(int i = 2; i * i <= n; i++){
        if(n % i == 0)
            return "BUKAN";
    }
    return "YA";
}

int main(){
    int n;
    cin >> n;

    vector<int> input(n);
    for(int i = 0; i < n; i++){
        cin >> input[i];
    }

    for(int i = 0; i < n; i++){
        cout << chekbil(input[i]) << endl;
    }

    return 0;
}
