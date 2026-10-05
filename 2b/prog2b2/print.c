#include <stdio.h>
#include <stdlib.h>
int main(void){
    FILE *fp;
    int c;
    fp = fopen("print.c","r");
    if(fp == NULL){
        printf("Failed to open file!");
        exit(1);
    }
    while((c = fgetc(fp)) != EOF){
        printf("%c",c);
    }

    fclose(fp);
    return 0;
}