#include <stdio.h>
#include <stdlib.h>
int compare(const void *a,const void *b){
    char x = *((char*)a);
    char y = *((char*)b);
    if(x > y)
        return 1;
    else if(x < y)
        return -1;
    else 
        return 0;
}
int main(void){
    char message[] = "there is no royal road to learning";
    char search,*index_p;
    qsort(message,34,sizeof(char),compare);
    printf("%s\n",message);
    scanf("%c",&search);
    index_p = (char*)bsearch(&search,message,34,sizeof(char),compare);
    if(index_p == NULL)
        printf("なかったよ\n");
    else
        printf("message[%d]にあったよ\n",index_p - message);
    return 0;  
}
