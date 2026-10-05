#include <stdio.h>
int main(void){
    float temp,humid,uncomf;
    printf("気温?");
    scanf("%f",&temp);
    printf("湿度?");
    scanf("%f",&humid);
    uncomf = 0.81 * temp + 0.01 * humid * (0.99 * temp - 14.3) + 46.3;
    if(uncomf  >= 85.0)
        printf("暑くてたまらない\n");
    else if(uncomf >= 80.0)
        printf("暑くて汗が出る\n");
    else if(uncomf >= 75.0)
        printf("やや暑い\n");
    else
        printf("それほど暑くない\n");
    
    return 0;
}
