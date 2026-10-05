#include <stdio.h>
int hiku(int num_1,int num_2)
{
    if (num_1 > num_2){
        return num_1 - num_2;
    }else{
        return num_2 - num_1;
    }
}

int main(void)
{   
    int num_1,num_2;
    printf("二つの整数を入れて下さい\n");
    scanf("%d%d",&num_1,&num_2);
    printf("差は %d です\n",hiku(num_1,num_2));
    return 0;
}