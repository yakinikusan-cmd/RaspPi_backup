#include <stdio.h>
int main(void)
{
    int mark;
    char grade;
    scanf("%d",&mark);
    if (mark >= 85){
        grade = 'A';
        printf("goukaku\n");
    }
    printf("%c\n",grade);
    return 0;
}