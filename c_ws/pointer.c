#include <stdio.h>
int main(void) 
{
    int tokuten,*p;
    p = &tokuten;
    *p = 90;
    printf("%d\n",tokuten);
    return 0;
}