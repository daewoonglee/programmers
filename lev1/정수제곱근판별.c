#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <math.h>

long long solution(long long n) {
    double N = sqrt(n);
    return (N == (int)N) ? (long long)pow(N+1, 2) : -1;
}


int main(){
    printf("%lld\n", solution(121)); //144
    printf("%lld\n", solution(3)); //-1
    printf("%lld\n", solution(4000000)); //4004001
    printf("%lld\n", solution(7)); //-1
    return 0;
}
