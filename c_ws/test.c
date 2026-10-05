#include <stdio.h>
int main(void)
{
    int *p , i;
    char string[] = "Hello";
    p = "a";
    for(i = 0; i < 500;i++){
        printf("%c\n",*p); 
        p++;
    }
}