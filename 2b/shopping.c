#include <stdio.h>
int main(void){
    struct shopping
    {
        char *name;
        int price;
    };
    struct shopping *p,my_list[3] = {{"にんじん",150},
                                    {"さくらんぼ",250},
                                    {"しいたけ",130}};
    p = my_list;
    for(int i = 0;i < 3;i++){
        printf("購入物品 %s は, %d 円です\n",(p+i)->name,(p+i)->price);
    }
    return 0;
    
}