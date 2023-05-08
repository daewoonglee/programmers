#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <time.h>

long long solution(int a, int b) {
    // // running time: 0.847277
    // long long ans = 0;
    // if(b < a){
    //     int t = a;
    //     a = b;
    //     b = t;
    // }
    // for(int i=a; i<=b; i++)
    //     ans += i;
    // return ans;

    // code refactoring, sum of arithmetic sequence - 0.000511
    if(a==b) return a;
    
    int n = a < b ? b-a+1 : a-b+1;
    int sum = a+b;
    return (long long)n*sum/2;
}


int main(){
    clock_t tic = clock();
    for (int i=0; i<10000; i++){
        solution(3, 5);
        solution(3, 3);
        solution(5, 3);
        solution(0, 10000); 
        solution(-10000, 0);
        solution(-10000, 10000);
    }
    clock_t toc = clock();
    printf("running time: %f\n", (double)(toc-tic) / CLOCKS_PER_SEC);
    return 0;
}