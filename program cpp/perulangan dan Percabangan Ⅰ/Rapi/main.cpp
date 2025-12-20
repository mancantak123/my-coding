#include <bits/stdc++.h>
using namespace std;


int main(){
    int n;
    cin>>n;
    
    for(int i=1;i<=n;i++){
        if(i > 10){
            cout<<" "<<i;
            if(i % 10 == 0){
                cout<<endl;
            }
        }
    }
}


