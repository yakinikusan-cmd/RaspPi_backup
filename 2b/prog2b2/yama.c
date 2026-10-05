#include <stdio.h>
#include  <stdlib.h>
int main(void){
    FILE *fp;
    int price,hight;
    char name[20],place[20];
    fp = fopen("yama.data","r");
    if(fp == NULL){
        printf("failed to open file!");
        exit(1);
    }
    while(fscanf(fp,"%d%s%s%d",&price,name,place,&hight) != EOF){
        printf("%4d %15s %17s %6d\n",price,name,place,hight);
    }
    fclose(fp);
    return 0;
}