#include <stdio.h>
#include <stdlib.h>

int main(void) {
  int myArray[100];
  int sum;
  int avg;
  for (int i = 0; i < 100; i++) {
    myArray[i] = rand();
  }
  for (int j = 0; j < 100; j++) {
    sum += myArray[j];
  }
  avg = sum/100;
  printf("%d", avg);
}