#include <stdio.h>
int tasu(int,int);
int hiku(int,int);

int main(void){
    int a,b;
    printf("二つの整数を入れて下さい\n");
    scanf("%d%d",&a,&b);
    printf("和は%dです\n差は%dです\n",tasu(a,b),hiku(a,b));
    return 0;
}

int tasu(int a,int b){
    return a + b;
}
    

int hiku(int a,int b){
    if(a < b)
        return b - a;
    else
        return a - b;
}

