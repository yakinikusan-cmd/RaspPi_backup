#include <stdio.h>
void disp(char *p[]){
    int i = 0;
    while (p[i] != NULL){
        printf("%s\n",p[i]);
        i++;
    }
}
int main(void){
    char *music[] = {"pops","rock","jazz","classic",NULL};
    disp(music);
    return 0;
}