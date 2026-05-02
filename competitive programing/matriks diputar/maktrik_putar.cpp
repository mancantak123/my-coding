#include<iostream>
using namespace std;

int main(){
    int n,m;
    cin>> n >> m;
    int maxtrix[n][m] ={0};
    
    for(int i=0; i<n;i++){
        for(int j=0;j<m;j++){
            cin>>maxtrix[i][j];
        }
    }
    int maxtrix_hasil[m][n] = {0};
    
    for(int i=0;i<m;i++){
        for(int j=0;j<n;j++){
            maxtrix_hasil[i][j] = maxtrix[n - 1 - j][i];
        }
    }
    
    int temp = n;
    n = m;
    m = temp;
    
    for(int i=0; i<n;i++){
        for(int j=0;j<m;j++){
            cout<<maxtrix_hasil[i][j] << " ";
        }
        cout<<endl;
    }
    
    
    
    return 0;
}