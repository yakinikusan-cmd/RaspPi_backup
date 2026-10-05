#include <stdio.h>
#include <stdlib.h>
int main(void){
    FILE *fp;
    int data1[100];
    int data2[100];
    for(int i = 0;i < 100;i++)
        data1[i] = (i + 1) * 10;
    fp = fopen("test.data","wb");
    if(fp == NULL){
        printf("failed to open file");
        exit(1);
    }
    if(fwrite(data1,sizeof(int),100,fp) != 100){
        printf("failed  to write binary");
        fclose(fp);
        exit(1);
    }
    fclose(fp);


    fp = fopen("test.data","rb");
    if(fp == NULL){
        printf("failed to open file");
        exit(1);
    }
    if(fread(data2,sizeof(int),100,fp) != 100){
        printf("failed to read binary");
        fclose(fp);
        exit(1);
    }

    for(int i = 0;i < 100;i++)
        printf("%d ",data2[i]);
    fclose(fp);
    return 0;
}