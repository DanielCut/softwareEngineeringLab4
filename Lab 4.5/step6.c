#include <stdio.h>
#include <stdlib.h>

int main(void) {
  int myArray[100];
  int array[100];
  for (int i = 0; i < 100; i++) {
    myArray[i] = rand();
  }
  for (int i = 0; i < 100; i++) {
    if (i == 0 || i == 100) {
      array[i] = myArray[i];
    }
    array[i] = (myArray[i-1] + myArray[i] + myArray[i+1])/3;
  }
  return 0;
}