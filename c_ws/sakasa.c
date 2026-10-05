#include <stdio.h>
int main(void)
{
    int i;
    char *str;
    str = "computer";
    for(i = 7; i>= 0 ; i--)
        printf("%c",*(str + i));
    putchar('\n');
    return 0;
}