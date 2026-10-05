#include <stdio.h>
#include <time.h>
// int main(void){
//     time_t ct,birth_t;
//     struct tm *birth_tm;
//     ct = time(NULL);
//     birth_tm = localtime(&ct);
//     birth_tm -> tm_year = 2009 - 1900;
//     birth_tm -> tm_mon = 1 - 1;
//     birth_tm -> tm_mday = 6;
//     birth_t = mktime(birth_tm);
//     printf(ctime(&birth_t));
//     return 0;
// }
int main(void){
    time_t birth_t = 0;
    struct tm *birth_tm ;
    birth_tm = localtime(&birth_t);
    birth_tm -> tm_year = 2009 - 1900;
    birth_tm -> tm_mon = 1 - 1;
    birth_tm -> tm_mday = 6;
    birth_t = mktime(birth_tm);
    printf(ctime(&birth_t));
    return 0;
}