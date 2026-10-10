#include<iostream>
using namespace std;

int main(){
	long long N;
	cin>> N;
	
	long long R_terbaik = 1;
	long long C_terbaik = N;
	
	for(long long r =1; r < N;r++){
		if(N % r == 0){
			long long c = N/r;
			if((c - r) < (C_terbaik - R_terbaik)){
				R_terbaik = r;
				C_terbaik = c;
			}
		}
	}
	
	cout<<R_terbaik<<" "<<C_terbaik<<endl;
	
	return 0;
}