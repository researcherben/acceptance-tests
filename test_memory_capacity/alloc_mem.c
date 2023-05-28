#include <stdio.h>
#include <stdlib.h>
#include <mpi.h>
#include <string.h>

// from https://stackoverflow.com/a/40407833/1164295

int main(int argc, char *argv[]) {
char *data;
int bytes = (1024*1024);
data = (char *) malloc(bytes);
for(int i=0;i<bytes;i++){
 data[i] = (char) rand();
 printf("%c",data[i]);
}
return 0;

}
