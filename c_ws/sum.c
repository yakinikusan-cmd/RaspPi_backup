#include <stdio.h>
int main(void)
{
    int a,sum;
    sum = 0;
    while(scanf("%d",&a) != EOF){
        printf("a:%d\n",a);
        sum += a;
    }
    printf("sum:%d\n",sum);
    return 0;
}