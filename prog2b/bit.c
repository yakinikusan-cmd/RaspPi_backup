#include <stdio.h>
int main(void){
    int x;
    printf("整数を入れて\n");
    scanf("%d",&x);
    for(int i = sizeof(x) * 8;i > 0;i--){
        printf("%d",x >> (i-1) & 0x00000001);
    }
    printf("\n");
    return 0;
}