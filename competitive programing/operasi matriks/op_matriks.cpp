#include<iostream>
#include<string>
using namespace std;

void rot(int max[100][100], string op, int &k, int &h) {
    int total_putaran = stoi(op) / 90;
    
    while(total_putaran > 0) {
        int hasil[100][100] = {0};
        for(int i = 0; i < k; i++) {
            for(int j = 0; j < h; j++) {
                hasil[i][j] = max[h - 1 - j][i];
            }
        }
        int temp = h;
        h = k;
        k = temp;
        
        for(int i = 0; i < h; i++) {
            for(int j = 0; j < k; j++) {
                max[i][j] = hasil[i][j];
            }
        }
        total_putaran--;
    }
}


void ref(int max[100][100] , string op , int k , int h){
    int hasil[100][100] = {};
    
    if(op == "_"){
        int hzl = h - 1;
        for(int i=0; i < h;i++){
            for(int j=0;j<k;j++){
                hasil[i][j] = max[hzl][j];
            }
            hzl--;
        }
    }else if(op == "|"){
        for(int i=0; i < h;i++){
            int vtl = k - 1;
            for(int j=0;j<k;j++){
                hasil[i][j] = max[i][vtl];
                vtl--;
            }
        }
    }
    
    for(int i=0;i < h;i++){
        for(int j=0; j < k;j++){
            max[i][j] = hasil[i][j];
        }
    }
}



int main(){
    
    // input nilai maxtrix daan operasi
    int n,m,x;
    cin>> n >> m >> x;
    string operasi[100] = {};
    int maxtrix[100][100] = {};
    
    
    for(int i=0; i < n;i++){
        for(int j=0; j < m;j++){
            cin>> maxtrix[i][j];
        }
    }
    for(int i=0;i < x;i++){
        cin>>operasi[i];
    }
    
    // proses
    for(int i=0; i < x;i++){
        if(operasi[i] == "_" || operasi[i] == "|"){
            ref(maxtrix, operasi[i] , m , n);
        }else if(operasi[i] == "90" || operasi[i] == "180" || operasi[i] == "270"){
            rot(maxtrix , operasi[i] , m , n);
        }
    }
    //output
    
    for(int i=0; i < n;i++){
        for(int j=0; j < m;j++){
            cout<<maxtrix[i][j] << " ";
        }
        cout<<endl;
    }
    
    return 0;
}