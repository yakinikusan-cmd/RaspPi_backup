#include <stdio.h>
#include <stdlib.h>
int main(int argc,char *argv[]){
    FILE *fp;
    char buf[256];
    if(argc != 2){
        printf("Usage: ./print2 file_name\n");
        exit(1);
    }
    fp = fopen(argv[1],"r");
    if(fp == NULL){
        printf("Failed to open file\n");
        exit(1);
    }
    while(fgets(buf,256,fp) != NULL){
        printf(buf);
    }
    fclose(fp);
    return 0;
}