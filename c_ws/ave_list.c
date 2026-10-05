#include <stdio.h>
int main(void)
{
    int score[6] = {44,67,78,98,34,65};
    int i,sum;
    sum = 0;
    for(i = 0;i < 6;i++)
        sum  += score[i];
    printf("%d",sum/6);
}