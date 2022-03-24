#include <iostream>
#include <stdlib.h>
#include <time.h>
#include <ctime>

using namespace std;

void dar_vueltas( int C[], int cant_monedas, int vueltas ) {
	int M[ vueltas + 1 ][ cant_monedas ];
	pair<int, int> B[ vueltas + 1 ][ cant_monedas ];
	for ( int i = 0; i < vueltas + 1; i++){
		for (int j = 0; j < cant_monedas; j++){
			M[i][j] = 0;
		}
	}
	for ( int i = 0; i < vueltas + 1; i++){
		for (int j = 0; j < cant_monedas; j++){
			B[i][j] = make_pair(0,0);
		}
	}

	
	for (int i = 1; i < vueltas + 1; i++){
		M[ i ][ 0 ] = i;
	}

	
	for (int i = 1; i < cant_monedas; i++) {
		for (int j = 1; j < vueltas + 1; j++) {
			if( C[ i ] > j ) {
				M[ j ][ i ] = M[ j ][ i - 1 ];
				B[ j ][ i ] = make_pair(j, i - 1);
			} else {
				int a = M[ j - C[ i ] ][ i ] + 1;
				int b = M[ j ][ i - 1];
				if ( a < b ) {
					M[ j ][ i ] = a;
					B[ j ][ i ] = make_pair(j - C[ i ], i );
				}else {
					M[ j ][ i ] = b;
					B[ j ][ i ] = make_pair(j, i - 1);
				}
			}
		}
	}
	
	int j = cant_monedas - 1;
	int i = vueltas;
	
	int cant[j + 1];
	for ( int k = 0; k < j + 1; k++ ){
		cant[k] = 0;
	}
	
    while (i != 0) {
        int ic = i;
        i = B[ ic ][ j ].first;
		j = B[ ic ][ j ].second;
        if ( ic != i ){
            if ( j == 0 ){
                cant[ j ] = ic;
            }
            else{
                cant[ j ] += 1;
            }
        }
	}
    for (int k = 0; k < cant_monedas; k++){
        if ( cant[ k ] == 1 )
            cout << cant[k] << " moneda de " << C[k] << endl;
        else if ( cant[ k ] > 1)
            cout << cant[k] << " monedas de " << C[k] << endl;
    }
}

int main() {
	srand(time(NULL));
  int total;
  int valor;
  total = 54000 + rand()%(1000);
	double suma = 0;
	unsigned t;
	for( int i = 0; i < 1000; i++){
		valor = 1 + rand()%(total);
		int C[11] = {1, 50, 100, 200, 500, 1000, 2000, 5000, 10000, 20000, 50000};
		cout << "Para " << total-valor << ":" << endl;
		t = clock();
		dar_vueltas(C, 11, total-valor);
		suma += (double(clock() - t)/CLOCKS_PER_SEC);
		cout << endl;
	}
	cout << "Tiempo total: " << suma << " segundos " << endl << "Tiempo promedio: " << suma/1000 << " segundos" << endl;
}
