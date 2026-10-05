#include <stdio.h>
int main(void){
    int basic,grade;
    printf("基本額は？");
    scanf("%d",&basic);
    printf("成績は？");
    scanf("%d",&grade);
    switch(grade){
        case 5:
        case 4:
            basic *= 2;
            break;
        case 3:
            break;
        case 2:
        case 1:
            basic /= 2;
            break;
        default:
            basic = 0;
    }
    printf("今月のおこづかいは%d円です\n",basic);
    return 0;
}