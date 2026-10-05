#include <stdio.h>
int main(void){
    FILE *fp;
    int data[100];
    fp = fopen("/dev/input/event0","rb");
    while(1){
        fseek(fp,0,SEEK_SET);
        fread(data,sizeof(int),100,fp);
        for(int i = 0; i < 100;i++)
            printf("%5d ",data[i]);
        printf("\n");
    }
    
}