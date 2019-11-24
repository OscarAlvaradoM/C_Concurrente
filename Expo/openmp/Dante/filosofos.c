#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

#include <omp.h>

int tenedores = 5;

void filosofo();

int main() {
  #pragma omp parallel num_threads(5)
  {
    filosofo();
  }
  return 0;
}

void filosofo() {
  int id = omp_get_thread_num();
  while (1) {
    while (tenedores >= 2) {
      #pragma omp critical
      {
        printf("Hay %d tenedores\n",tenedores);
        tenedores -= 2;
        printf("Filosofo %d esta comiendo\n",id);
        sleep(1);
        tenedores += 2;
        printf("Termino de comer. Hay %d tenedores\n",tenedores);

      }
    }
  }
}
