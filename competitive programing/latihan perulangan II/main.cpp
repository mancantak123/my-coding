#include<iostream>
using namespace std;

// program akan mulai dari kamar 1
// setiap pindah kamar = value k tambah 1  , dengan base case value k  = 1
// program akan mengecek kamar dan mencari value kamar dengan value false 
// setiap program akan pindah kamar , kamar tersebut akan menjadi value kebalikan "false = true"
// pergerakan program akan disesuaikan dengan jumlah dari kamar yang dia dicek hingga semua value kamar true
// dan pergerakan program akan dibatasi dengan total kalkulasi gerak "2^n - 1"
// secara visual kita dapat bisa mengetahui berapa pergerakan program dan kalkulasi namun komputer tidak

int pangkat(short n){
	short basis = 2;
	int hasil = 1;
	for(int i=0; i < n;i++){
		hasil *= basis;
	}
	return hasil;
}

void pattern(short patern[] , short n , int max){
	bool* cek = new bool[n]();
	
	for(int i=0; i < max;i++){
		short index = 1;
		short k = 1;
		
		while(cek[k % n] == true){
			cek[k % n] = false;
			index = index + 1;
			k++;
		}
		cek[k % n] = true;
		patern[i] = index;
	}
	
	delete[] cek;
}

int main (){
	short n=0;
	cin>>n;
	
	int max = pangkat(n) - 1;
	
	short patern[max] = {};
	
	pattern(patern , n , max);
	
	for(int i =0; i < max;i++){
		for(int j=1; j <= patern[i];j++){
			cout<<"*";
		}
		cout<<endl;
	}
	
	return 0;
}