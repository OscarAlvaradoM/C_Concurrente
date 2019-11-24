#include<stdio.h>
#include<omp.h>
#define N 8

int main() {
  int numeros[N];
  unsigned long suma=0,producto=1;

  for (int i = 0; i < N; i++) {
    numeros[i] = i;
  }
  printf("Inicia secciones...\n");
  #pragma omp parallel
  {
    #pragma omp sections
    {
      #pragma omp section
      {
        for (int i = 0; i < N; i++)
          suma = suma + numeros[i];
      }
      #pragma omp section
      {
        for (int i = 1; i < N; i++)
          producto = producto * numeros[i];
      }
    }
  }
  printf("Suma de los primeros %d numeros es %lu\n",N-1,suma);
  printf("Producto de los primeros %d numeros es %lu\n",N-1,producto);

  return 0;
}
