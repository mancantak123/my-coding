#include<iostream>
#include<cmath>
using namespace std;

int pangkat(int basis, short exp) {
    int hasil = 1;
    for (int i = 0; i < exp; i++) {
        hasil *= basis;
    }
    return hasil;
}

int dekat(int x1, int y1, int x2, int y2, short D){
	return pangkat(abs(x1 - x2) , D) + pangkat(abs(y1 - y2) , D);
}


int main(){
	short N , D;
	cin >> N >> D;
	short matriks [N][2] = {};
	
	for(short i =0; i < N; i++){
		for(short j=0; j < 2;j++){
			cin>>matriks[i][j];
		}
	}
	
	int min = 2000000;
	int max = -1;
	
	for(short i =0; i < N;i++){
		for(short j=i+1;j < N;j++){
			int total = dekat(matriks[i][0] , matriks[i][1] , matriks[j][0] , matriks[j][1] , D);
				
			if(total < min) min = total;
			if(total > max) max = total;
		}
	}
	
	cout<<min<<" "<<max<<endl;
	return 0;
}