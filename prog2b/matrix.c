#include <stdio.h>
void unit(int x[][5]){
    for (int i = 0;i < 5;i++)
        for (int j = 0;j < 5;j++)
            x[i][j] = i == j;
            //x[i][j] = i == j?1:0;
}
int main(void){
    int data[5][5];
    unit(data);
    for (int i = 0;i < 5;i++){
        for (int j = 0;j < 5;j++)
            printf("%2d",data[i][j]);
        printf("\n");
    }
    return 0;
}