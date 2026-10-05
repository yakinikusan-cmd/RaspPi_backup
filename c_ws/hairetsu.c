#include <stdio.h>
int main (void)
{
    int a[20],i;
    for(i = 0;i < 20; i++)
        a[i] = i;
    for(i = 0; i< 20;i++)
        printf("a[%d] = %d\n",i,a[i]);
    return 0;
}