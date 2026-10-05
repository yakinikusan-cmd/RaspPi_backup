#include <stdio.h>
void waru(int num_1,int num_2,int *quot,int *rem){
    *quot = num_1 / num_2;
    *rem = num_1 % num_2; 
}
int main(void){
    int warareru_num,waru_num,syou,amari;
    printf("二つの整数を入れて下さい\n");
    scanf("%d%d",&warareru_num,&waru_num);
    waru(warareru_num,waru_num,&syou,&amari);
    printf("商は %d で,余りは %d です\n",syou,amari);
    return 0;
}