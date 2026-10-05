#include <stdio.h>
int main(void)
{
    int mark[2][4] = {{50,60,70,80},
                      {70,80,90,100}};
    int *p,i;
    p = mark[1];
    for(i = 0; i < 4;i++)
        printf("%d ",p[i]);
    printf("\n");
    return 0;
}