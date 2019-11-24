#include <stdio.h>
#include <omp.h>

int main() {
  printf("Inicia region paralela\n");
  int var = 23;
  printf("var = %d\n",var);
  #pragma omp parallel firstprivate(var)
  {
    printf("Hilo %d: var = %d\n",omp_get_thread_num(), var);
  }
  return 0;
}
