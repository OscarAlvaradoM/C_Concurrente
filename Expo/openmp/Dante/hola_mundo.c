
#include<stdio.h>
#include<omp.h>

int main(){
  int nthreads;

  /* Fork a team of threads with each thread having a private tid variable */
  printf("Inicia seccion paralela\n");
  #pragma omp parallel
  {
    int tid = omp_get_thread_num();  //Obtencion del thread-id

    printf("Hola mundo desde hilo %d\n", tid);

    if (tid == 0)
    {
      nthreads = omp_get_num_threads();
      printf("Numero de hilos = %d\n", nthreads);
    }
  }
  printf("Termina seccion paralela\n");

  return 0;
}
