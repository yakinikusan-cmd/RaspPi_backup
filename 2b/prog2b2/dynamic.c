#include<stdio.h>
#include<stdlib.h>
int main(void){
    int *id;
    int n;
    scanf("%d",&n);
    id = (int*)malloc(sizeof(int) * n);
    if(id == NULL){
        printf("Memory Error\n");
        exit(1);
    }
    for(int i = 0;i < n;i++)
        id[i] = i + 1;
    for(int i = 0;i < n;i++)
        printf("%d ",id[i]);
    printf("\n");
    free(id);
    return 0;

}