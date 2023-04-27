#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <math.h>

int solution(int n) {
    int ans = 0;
    for(int i=1; i<=pow(n, 0.5); i++){
        if(n % i == 0){
            int q = n / i;
            printf("i: %d, q: %d\n", i, q);
            ans += q==i ? i : q+i;
        }
    }
    return ans;
}


int main(){
    printf("%d\n", solution(12)); // 28
    printf("%d\n", solution(5)); //6
    printf("%d\n", solution(4)); //7
    printf("%d\n", solution(2)); //3
    printf("%d\n", solution(1)); //1
    printf("%d\n", solution(0)); //0
    return 0;
}
