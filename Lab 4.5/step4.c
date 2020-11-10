#include <stdio.h>

int main(void) {
  int sum;
  for (int i = 1; i < 101; i++) {
    sum += i;
  }
  printf("%d\n" , sum);
  return sum;
}