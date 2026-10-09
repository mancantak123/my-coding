#include <iostream>

using namespace std;

void perkalian(int a[100][100], int b[100][100], int c[100][100], int n, int p, int m) {
    // 1. Reset matriks c ke 0
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            c[i][j] = 0;
        }
    }

    for (int i = 0; i < n; ++i) {
        for (int k = 0; k < p; ++k) {
            for (int j = 0; j < m; ++j) {
                c[i][j] += a[i][k] * b[k][j];
            }
        }
    }
}

int main() {
    int n, p, m;
    cin >> n >> p >> m;
    
    int A[100][100] = {};
    int B[100][100] = {};
    int C[100][100] = {};
    

    for(int i = 0; i < n; i++){
        for(int j = 0; j < p; j++){
            cin >> A[i][j];
        }
    }
    
    // Input Matriks B 
    for(int i = 0; i < p; i++){
        for(int j = 0; j < m; j++){
            cin >> B[i][j];
        }
    }
    
    // Jalankan perkalian
    perkalian(A, B, C, n, p, m);
    
    for(int i = 0; i < n; i++){
        for(int j = 0; j < m; j++){
            cout << C[i][j] << " "; 
        }
        cout << endl;
    }

    return 0;
}