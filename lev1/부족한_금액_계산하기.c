#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

long long solution(int price, int money, int count) {
    long long s = count*(price+price * count)/2;
    long long ans = money-s;
    return ans < 0 ? llabs(ans) : 0;
}


int main(){
    printf("%lld\n", solution(3, 20, 4)); //10
    printf("%lld\n", solution(1, 30, 2500)); //10
    return 0;
}
