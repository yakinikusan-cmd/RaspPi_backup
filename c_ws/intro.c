#include <stdio.h>
int main(void)
{
    char name[25],address[30],hobby[20];
    printf("name\n");
    scanf("%s",name);
    printf("address\n");
    scanf("%s",address);
    printf("hobby\n");
    scanf("%s",hobby);
    printf("Hello.My name is %s.\nI live in %s.\nMy hobby is %s.\n",name,address,hobby);
    return 0;
}