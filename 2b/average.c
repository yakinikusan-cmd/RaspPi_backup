#include <stdio.h>
int heikin(int a[]){
    int sum = 0;
    int i = 0;
    while(a[i] != -999){
        sum += a[i];
        i++;
    }
    return sum/i;
} 
int main(void){
    int tokuten[] = {65,80,70,90,85,-999};
    int ave;
    ave = heikin(tokuten);
    printf("平均は%d点です",ave);
    return 0;
}