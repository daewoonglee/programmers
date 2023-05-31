#include <stdio.h>
#include <time.h>

void solution(int a, int b){
    // // 0.123384
    // for(int i=0; i<b; i++){
    //     for(int j=0; j<a; j++)
    //         printf("*");
    //     printf("\n");
    // }

    // 0.124000 - O(n+m)
    for(int i=0; i<a*b; i++){
        printf("*");
        if((i+1)%a==0)
            printf("\n");
    }
}

int main(void) {
    clock_t tic = clock();
    solution(5, 3);
    solution(1000, 3);
    solution(1000, 1000);
    clock_t toc = clock();
    printf("running time: %f\n", (double)(toc-tic) / CLOCKS_PER_SEC);
    return 0;
}