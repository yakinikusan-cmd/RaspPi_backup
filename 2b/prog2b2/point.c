#include <stdio.h>
#include <stdlib.h>
int main(void){
    char point_str[10] = "100";
    int point;
    char message[25];
    int n;
    printf("ポイント何倍デーですか？");
    scanf("%d",&n);
    point = n*atoi(point_str);
    sprintf(message,"You get %d points.\n",point);
    printf(message);
    return 0;

}
