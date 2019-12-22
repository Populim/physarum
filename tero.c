#include <stdio.h>
#include <stdlib.h>


void printDoubleMatrix(double** d, int n){
	for (int i = 0; i < n; ++i){
		for (int j = 0; j < n; ++j){
			printf("%.2lf ", d[i][j]);
		}
		printf("\n");
	}
}

void invertMatrixElements(double** d, int n){
	for (int i = 0; i < n; ++i){
		for (int j = 0; j < n; ++j){
			if(d[i][j] != 0){
				d[i][j] = 1/d[i][j];
			}
		}
	}
}

double** getCondutivityMatrix(int n){
	double** c = malloc(sizeof(double*) * n);
	for (int i = 0; i < n; ++i){
		c[i] = malloc(sizeof(double) * n);
	}

	for (int i = 0; i < n; ++i){
		for (int j = 0; j < n; ++j){
			c[i][j] = (rand()%50001 + 50000)/(double)100000;
		}
	}
	return c;
}

double** multiplyMatrixElements(double** a,double** b, int n){
	double** c = malloc(sizeof(double*) * n);
	for (int i = 0; i < n; ++i){
		c[i] = malloc(sizeof(double) * n);
	}

	for (int i = 0; i < n; ++i){
		for (int j = 0; j < n; ++j){
			c[i][j] = a[i][j] * b[i][j];
		}
	}
	return c;
}


int main(){
	FILE* fp = fopen("input.in","r");
	int n;
	fscanf(fp,"%d",&n);
	double** distances = malloc(sizeof(double*) * n);
	for (int i = 0; i < n; ++i){
		distances[i] = malloc(sizeof(double) * n);
	}

	for (int i = 0; i < n; ++i){
		for (int j = 0; j < n; ++j){
			fscanf(fp,"%lf", &distances[i][j]);
		}
	}

	printDoubleMatrix(distances,n);
	printf("\n\n");
	
	invertMatrixElements(distances,n);

	printDoubleMatrix(distances,n);
	printf("\n\n");

	double** condutivity = getCondutivityMatrix(n);

	// condutivity divided by distances:
	double** CdD = multiplyMatrixElements(distances,condutivity,n);

	printDoubleMatrix(CdD,n);
	printf("\n\n");


	double* pressure = malloc(sizeof(double) * n);
	pressure[17] = 1;
	pressure[20] = 0;
	

}