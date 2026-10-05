#include <stdio.h>
#include <stdlib.h>
int main(void){
    int rand1,rand2,answer;
    srand(20090106);
    for(int i = 0; i < 3;i++){
        rand1 = rand() % 9 + 1;
        rand2 = rand() % 9 + 1;
        printf("%d ☓ %d = ",rand1,rand2);
        scanf("%d",&answer);
        if(rand1 * rand2 == answer){
            printf("正解です\n");
        }else{
            printf("まちがいです\n");
        }
    }
    
    return 0;
}