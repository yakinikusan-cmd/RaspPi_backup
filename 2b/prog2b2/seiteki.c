#include <stdio.h>
void test(void){
    int jido = 0;
    static int sei = 0;
    printf("(自動変数:%d)(静的変数:%d)\n",++jido,++sei);
}
int main(void){
    for(int i ;i < 10;i ++){
        test();
    }
    return 0;
}