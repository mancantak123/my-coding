#include<bits/stdc++.h>
using namespace std;

int main(){
    int N;
    int T = 0;
    cin>>N;
    
    vector<int> Data;
    for(int i=0; i <N;i++){
        int x;
        cin>>x;
        Data.push_back(x);
    }
    
    for(int x : Data){
        T += x;
    }
    
    for(int i=0;i < Data.size(); i++){
        cout<<T - Data[i]<<endl;
    }
}