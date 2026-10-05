// #include<stdio.h>
// #include<stdlib.h>
// #define N 100000
// int main(void){
//     float x,y,pai;
//     int a = 0;
//     for(int i = 0; i < N; i++){
//         x = (float)rand()/(float)RAND_MAX;
//         y = (float)rand()/(float)RAND_MAX;
//         // if(sqrt(pow(x,2)+pow(y,2)) <= 1){
//         //     a++;
//         // }
//         if(x*x+y*y <= 1){
//             a++;
//         }
//     }
//     pai = 4.0 * (float)a/(float)N;
//     printf("%.4f\n",pai);
//     return 0;
// }
#include<stdio.h>
#include<stdlib.h>
#define N 100000
int main(void){
    float x,y,z;
    int a = 0;
    for(int i = 0; i < N; i++){
        x = (float)rand()/(float)RAND_MAX;
        y = (float)rand()/(float)RAND_MAX;
        z = (float)rand()/(float)RAND_MAX;
        // if(sqrt(pow(x,2)+pow(y,2)) <= 1){
        //     a++;
        // }
        if(x*x+y*y + z*z <= 1){
            a++;
        }
    }
    printf("%.4f",6.0 * (float)a/(float)N);
    return 0;
}