#include <stdio.h>
void triple(int *point){
    *point *= 3;
}
int main(void){
    int point;
    printf("現在のポイント額を入れてください");
    scanf("%d",&point);
    triple(&point);
    printf("%dポイントになりました",point);
    return 0;
}