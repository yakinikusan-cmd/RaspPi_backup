#include <stdio.h>
int main(void)
{
    char a[4];
    a[0] = 'A';
    a[1] = 'B';
    a[2] = 'C';
    a[3] = '\0';
    printf("%s\n",a);
    return 0;
}