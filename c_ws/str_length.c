#include <stdio.h>
int main(void)
{
    char *str;
    int i;
    str = "information";
    i = 0;
    while(*(str + i) != '\0')
        i++;
    printf("%d\n",i);
    
    return 0;
}