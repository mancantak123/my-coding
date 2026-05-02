#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main() {
    string S, T;
    
    if (!(cin >> S >> T)) return 0;

    size_t pos = S.find(T);
    while (pos != string::npos) {
        S.erase(pos, T.length());
        pos = S.find(T);
    }

    cout << S << endl;

    return 0;
}