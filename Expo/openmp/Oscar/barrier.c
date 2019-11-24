#include <stdio.h>
#include <omp.h>

int main()
{
	int x[4];
	int y[4];
	#pragma omp parallel
	{
	int mytid = omp_get_thread_num();
	x[mytid] = mytid * 10;
	#pragma omp barrier
	y[mytid] = x[mytid]+x[mytid+1];
	printf("Soy el hilo %d -> %d -> %d \n", mytid, x[mytid], y[mytid]);
	}
	return 0;
}
