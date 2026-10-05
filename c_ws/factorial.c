#include <stdio.h>
int main(void)
{
    int n,i,kaijo;
    printf("n=\n");
    scanf("%d",&n);
    kaijo = 1;
    for(i = 1;i <= n;i++){
        kaijo *= i;
        printf("%2d!%13d\n",i,kaijo);
    }

    return 0;
}