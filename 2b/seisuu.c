#include <stdio.h>
int main(void){
    int num;
    int is_continue;
    do{
        printf("整数を入れて下さい\n");
        scanf("%d",&num);
        if(num % 2 == 0){
            printf("偶数だよ\n");
        }else{
            printf("奇数だよ\n");
        }
        printf("繰り返しますか ？　(yes：1/no：0)\n");
        scanf("%d",&is_continue);
    }while(is_continue == 1);
    return 0;
}