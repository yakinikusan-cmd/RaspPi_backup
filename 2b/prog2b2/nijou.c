#include <stdio.h>
#define sqr(x) ((x)*(x))
int main(void){
    int num;
    printf("整数を入れて");
    scanf("%d",&num);
    printf("二乗の値は %d です.\n",sqr(num));
    return 0;
}