#include <stdio.h>
#include <omp.h>

#define MAX 4

int main() {
   int count = 0;
   #pragma omp parallel num_threads(MAX)
   {
     // #pragma omp atomic
      count++;
   }
   printf("Número de hilos: %d\n", count);
}
