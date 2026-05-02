#include<bits/stdc++.h>
using namespace std;

int main(){
    
    // input value
    
    int N;
    vector<int> Data;
    cin>> N;
    
    for(int i=0; i < N; i++){
        int x;
        cin>>x;
        Data.push_back(x);
    }
    
    // output dari value
    
    int x = Data[0];
    int y = Data[0];
    
    for(int i=0; i < N;i++){
        if(x > Data[i]){
            x = Data[i];
        }
        
        if(y < Data[i]){
            y = Data[i];
        }
    }
    cout<<y<<" "<<x<<endl;
    
}