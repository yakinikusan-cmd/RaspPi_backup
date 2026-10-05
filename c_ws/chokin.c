#include <stdio.h>
int main(void)
{
    float money;
    int year;
    money = 10000;
    year = 0;
    while(money <= 15000){
        money = money*1.03;
        year++;
    }
    printf("%d年後\n",year);
    return 0;
}