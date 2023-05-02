#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>

long long solution(long long n) {
    // // 0.010661
    // double N = sqrt(n);
    // return (N == (int)N) ? (long long)pow(N+1, 2) : -1;

    // 0.009822
    long long N = sqrtl(n); // return long long
    return (N*N == n) ? (long long)(N+1)*(N+1) : -1;
}


int main(){
    clock_t tic = clock();
    for (int i=0; i<100000; i++){
        solution(121);
        solution(3);
        solution(4000000);
        solution(7);
        solution(2147483646);
        solution(50000000000000);
    }
    clock_t toc = clock();
    printf("running time: %f\n", (double)(toc-tic) / CLOCKS_PER_SEC);
    return 0;
}
