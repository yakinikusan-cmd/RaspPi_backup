#include <stdio.h>
int main(void)
{
    int money,mark;
    money = 5000;
    scanf("%d",&mark);
    if(mark >= 80){
        money += 2000;
        printf("ごほうびだよ\n");
    }else{
        money -= 1000;
        printf("次は頑張ってね\n");
    }
    printf("今月のお小遣いは%d円です.\n",money);
    return 0;
}