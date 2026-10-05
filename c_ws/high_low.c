#include <stdio.h>
#include <stdlib.h>
int main(void)
{
    int target_num,user_ans,ans_times;
    target_num = rand()%100+1;
    //printf("%d\n",target_num);
    printf("Plz enter num\n");
    scanf("%d",&user_ans);
    ans_times = 1;
    while (user_ans != target_num)
    {
        if (target_num > user_ans)
        {
            printf("Your ans is small\n");
        }else{
            printf("Your ans is big\n");
        }
        printf("Plz enter num\n");
        scanf("%d",&user_ans);
        ans_times++;
    }
    printf("Correct!\n");
    printf("You answer %d times.\n",ans_times);
    return 0;
}