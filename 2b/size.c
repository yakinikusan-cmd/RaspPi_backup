#include <stdio.h>
int main(void){
    printf("char :%3d byte\n", sizeof(char));
    printf("short :%3d byte\n", sizeof(short));
    printf("int :%3d byte\n", sizeof(int));
    printf("long :%3d byte\n", sizeof(long));
    printf("float :%3d byte\n", sizeof(float));
    printf("double:%3d byte\n", sizeof(double));
 
    return 0;
}