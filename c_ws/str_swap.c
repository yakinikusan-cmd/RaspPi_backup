#include <stdio.h>
#include <string.h>
int main(void)
{
    char a[32],b[32],c[32];
    scanf("%s%s",a,b);
    strcpy(c,a);
    strcpy(a,b);
    strcpy(b,c);
    printf("a=%s,b=%s\n",a,b);
    return 0;

}