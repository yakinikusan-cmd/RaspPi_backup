#include <stdio.h>
int main(void){
    enum animal {dog,cat,monkey};
    enum animal my_pet;
    printf("0:犬,1:猫,2:猿\n");
    scanf("%d",&my_pet);
    switch (my_pet)
    {
        case dog:
            printf("わんわん\n");
            break;
        case cat:
            printf("にゃあにゃあ\n");
            break;
        case monkey:
            printf("きいきい\n");
            break;
    }
    return 0;

}