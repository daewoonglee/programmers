#include <stdio.h>
#include <stdbool.h>
#include <string.h>
#include <time.h>

int solution(int n) {
    // // 0.721268
    // // get prime number using Eratosthenes algorithm.
    // bool prime[n+2]; // 소수2를 인덱스 시작 2로 설정하기 위해 +2
    // memset(prime, true, sizeof(prime));

    // for(int i=2; i*i<n; i++){
    //     if(prime[i]){
    //         for(int j=i*i; j<n; j+=i)
    //             prime[j] = false;
    //     }
    // }

    // for(int i=2; i<n; i++){
    //     if(prime[i]){
    //         if(n%i==1)
    //             return i;
    //     }
    // }
    
    // return 0;

    // 0.000011
    // n이 작아 소수를 찾는 행위보다 탐색이 더 빠름
    int ans = 0;
    for(int i=2;i<n;i++){
        if(n%i==1){
            return i;
        }
    }
    return ans;
}

int main(){
    clock_t tic = clock();
    for (int i=0; i<100; i++){
        solution(3);
        solution(10);
        solution(12);
        solution(1000000);
        solution(999999);
    }
    clock_t toc = clock();
    printf("running time: %f\n", (double)(toc-tic) / CLOCKS_PER_SEC);
    return 0;
}
