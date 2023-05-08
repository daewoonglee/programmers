#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

long long solution(int a, int b) {
    long long ans = 0;
    if(b < a){
        int t = a;
        a = b;
        b = t;
    }
    for(int i=a; i<=b; i++)
        ans += i;
    return ans;
}


int main(){
    printf("%lld\n", solution(3, 5)); //12
    printf("%lld\n", solution(3, 3)); //3
    printf("%lld\n", solution(5, 3)); //12
    return 0;
}