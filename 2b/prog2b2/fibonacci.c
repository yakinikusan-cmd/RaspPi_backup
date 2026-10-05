#include <stdio.h>
int fibo(int num){
    if(num == 0 || num == 1)
        return 1;
    return fibo(num - 1) + fibo(num - 2);
}
int main(void){
    int num;
    printf("num = ");
    scanf("%d",&num);
    printf("fibo(%d) = %d\n",num,fibo(num));
    return 0;
}
