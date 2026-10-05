#include <stdio.h>
int main(void)
{
    int a,b;
    char c;
    a = 0;
    c = getchar() - '0';
    a = c*100000000 +a;
    c = getchar() - '0';
    a = c*10000000 +a;
    c = getchar() - '0';
    a = c*1000000 +a;
    c = getchar() - '0';
    a = c*100000 +a;
    c = getchar() - '0';
    a = c*10000 +a;
    c = getchar() - '0';
    a = c*1000 +a;
    c = getchar() - '0';
    a = c*100 +a;
    c = getchar() - '0';
    a = c*10 +a;
    c = getchar() - '0';
    a = c*1 +a;
    printf("%d\n",a);
    b = c/100000000.0 - c%100000000 + '0';
    putchar(b);
    b = c/10 + '0';
    printf("%d",c/10 - c%10);
    // putchar(b);
    
    return 0;
}