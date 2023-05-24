#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <time.h>

long long solution(int price, int money, int count) {
    // // 0.000415
    // // long long sn = money-(count*(price+price * count)/2); //memory error
    // long long n = (price+price*count);
    // long long sn = count*n/2;
    // long long ans = money-sn;

    // code refactoring - 0.000184
    // long long ans = money-((count + 1) * count / 2 * price); // memory error
    long long n = (count+1)*count/2;
    long long sn = price*n;
    long long ans = money-sn;

    return ans < 0? ans*-1 : 0;
}


int main(){
    printf("%lld\n", solution(3, 20, 4)); //10
    clock_t tic = clock();
    for (int i=0; i<10000; i++){
        solution(3, 20, 4);
        solution(2500, 100, 2500);
        solution(2500, 1000000000, 2500);
    }
    clock_t toc = clock();
    printf("running time: %f\n", (double)(toc-tic) / CLOCKS_PER_SEC);
    return 0;
}
