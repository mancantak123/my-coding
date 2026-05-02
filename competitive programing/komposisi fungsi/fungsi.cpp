#include <bits/stdc++.h>
using namespace std;

int main() {
    long long A, B, K, x;
    cin >> A >> B >> K >> x;

    while (K--) {
        x = llabs(A * x + B);
    }

    cout << x << "\n";
    return 0;
}
