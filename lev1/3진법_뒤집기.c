#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>

void ternary(int n, int* n3, int *idx){
    int base = 3;
    while(n>0){
        n3[(*idx)++] = n%base;
        n/=base;
    }
    
}

int solution(int n) {
    // // 0.020568
    // int N = 0;
    // int* n3 = (int*)malloc(sizeof(int)*17);
    // ternary(n, n3, &N);

    // int ans = 0;
    // for(int i=0; i<N; i++)
    //     ans += ((int)pow(3, N-i-1)*n3[i]);
    // free(n3);
    // return ans;

    // code refactoring - 0.005917
    int ans = 0;
    while (n != 0){
        int remain = n % 3;
        ans *= 3;
        ans += remain;
        n /= 3;
    }
    return ans;
}


int main(){
    clock_t tic = clock();
    for (int i=0; i<10000; i++){
        solution(45);
        solution(125);
        solution(10000003);
        solution(100000000);
        solution(4123123);
    }
    clock_t toc = clock();
    printf("running time: %f\n", (double)(toc-tic) / CLOCKS_PER_SEC);
    return 0;
}
