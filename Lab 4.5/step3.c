#include <stdio.h>
#include <stdlib.h>

int main(void) {
  int i = 60;
  int j = 0;

  while (i < j) {
    i = i - 1;
    j = j+5;
  }  
  if (j != 0) {
    return rand(); //returning random bounded integer due to the ecall code being 42 in assembly
  }
  return 0; //returning 0 upon exiting due to the assembly code calling exit code 93 with the value 0 above it
}
