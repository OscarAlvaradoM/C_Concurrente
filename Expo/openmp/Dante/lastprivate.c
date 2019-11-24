#include <stdio.h>
#include <stdlib.h>
#include <omp.h>


int main(void){
  int i;
  int x=44;

  #pragma omp parallel for lastprivate(x)
  for(i=0;i<=10;i++){
    x=i;
    printf("Hilo %d\tx=%d\n",omp_get_thread_num(),x);
  }
  printf("x = %d\n", x);

  return 0;
}
