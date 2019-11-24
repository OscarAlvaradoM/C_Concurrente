#include <stdio.h>
#include <omp.h>

int main()
{
    int a[100];

    #pragma omp parallel for
    for (int i = 0; i < 100; i++) {
        a[i] = 2 * i;
		printf( "%d\n", a[i]);
    }
    printf( "-> %d\n", a[99]);
    return 0;
}
