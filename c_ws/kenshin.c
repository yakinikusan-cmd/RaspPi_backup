#include <stdio.h>
int main(void)
{
    int age,money;
    printf("年齢を入れてね\n");
    scanf("%d",&age);
    if( (int)(age/10) == 1 || (int)(age/10) == 3){
        money = 3000;
        printf("特別料金だよ\n");
    }else{
        money = 5000;
        printf("通常料金だよ\n");
    }
    printf("料金は%d円です\n",money);
    return 0;
}