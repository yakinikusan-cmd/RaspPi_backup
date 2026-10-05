#include <stdio.h>
int main (void)
{
    int i,j,n;
    scanf("%d",&n);
    for(i = 1;i <= n;i++){
        for(j = 1;j <= n;j++)
            printf("%4d",i * j);
        printf("\n");
    }
    return 0;
}