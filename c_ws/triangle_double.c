#include <stdio.h>
int main(void)
{
    double teihen,takasa;
    printf("底辺と高さを入れて\n");
    scanf("%lf%lf",&teihen,&takasa);
    printf("三角形の面積は%6.2fです.\n",teihen*takasa/2);
    return 0;
}