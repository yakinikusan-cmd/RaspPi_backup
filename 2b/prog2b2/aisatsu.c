#include <stdio.h>
#include <string.h>
int main(void){
    char lang[30];
    printf("言語名を入れて");
    scanf("%s",lang);
    if(strcmp(lang,"japanese") == 0)
        printf("こんにちは\n");
    else if(strcmp(lang,"english") == 0)
        printf("Hello\n");
    else if(strcmp(lang,"chinese") == 0)
        printf("汝好\n");
    return 0;
}