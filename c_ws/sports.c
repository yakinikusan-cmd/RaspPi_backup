#include <stdio.h>
int main (void)
{
    char *sports[3] = {"basketball","soccer","tennis"};
    int i;
    for(i = 0;i < 3;i++)
        printf("%s ",sports[i]);
    printf("\n");
    return 0;
}