#include <stdio.h>
int main(void){
    struct person{
        int month;
        char *seiza;
        char *blood;
    };
    struct person my_data;
    my_data.month = 1;
    my_data.seiza  = "やぎ";
    my_data.blood = "?";
    printf("%d月生まれの%s座の%s型です\n",my_data.month,my_data.seiza,my_data.blood);
    return 0;
}