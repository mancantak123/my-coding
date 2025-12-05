#include <bits/stdc++.h>
using namespace std;

int main(){
    vector<int>v;
    
    v.push_back(10); // tambah elemen
    v.push_back(20);
    v.push_back(30);
    
    cout<<"v[0] = "<<v[0]<<endl;    //tampilkan elemen , v.at(i) → check!
    cout<<"size = "<<v.size()<<endl; // jumlah elemen dari vector
    cout<<"capacity = "<<v.capacity()<<endl; // jumlah slot jumalh vector!
    
    vector<int> V = {5, 10, 20, 40};
    V.push_back(100);
    
    for(int i=0; i < 5;i++){ // iteasi biasa
        cout<<V[i]<<" ";
    }
    cout<<endl;
    
    cout<<"nama_Vector.erase(nama_Vector.begin + index)"<<endl; //nama_Vector.erase(nama_Vector.begin + index)
    V.erase(V.begin() + 1);
    for(int i : V){ // for each !!
        cout<< i << " ";
    }
    cout<<endl;
    
    cout<<"nama_Vector.insert(nama_vector.begin() + index , value);"<<endl;
    V.insert(V.begin() + 3 , 45); // nama Vector.insert(nama_vector.begin() + index , value);
    for(int i : V){ // for each !!
        cout<< i << " ";
    }
    cout<<endl;
}