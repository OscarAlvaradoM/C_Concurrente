#include <stdio.h>
#include <omp.h>

int main()
{

	const int SIZE = 1000000;
	int a[SIZE];
	unsigned long sum = 0;

	double t0,tf,tiempo;

	// Construyendo el arreglo que sumaremos.
	for(int i = 0; i < SIZE; i++)
		a[i] = i;

	t0 = omp_get_wtime();
	// Sumando el arreglo que construimos arriba.
	for (int i = 0; i < SIZE; i++)
		sum += a[i];

	printf("%lu \n",sum);
	tf = omp_get_wtime();
	tiempo = tf-t0;
	printf("Tiempo sin la reducción: %f \n", tiempo);

	sum = 0;
	t0 = omp_get_wtime();
	// Sumando de manera paralela el arreglo que construimos arriba.
	#pragma omp parallel for shared(a) reduction(+: sum)
	for (int i = 0; i < SIZE; i++)
		sum += a[i];

	printf("%lu \n",sum);
	tf = omp_get_wtime();
	tiempo = tf-t0;
	printf("tiempo con la reducción: %f \n", tiempo);

	return 0;
}
