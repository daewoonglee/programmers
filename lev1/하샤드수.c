#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

bool solution(int x) {
    int n = x;
    int harshad_n = 0;
    while(n>0){
        harshad_n += n%10;
        n /= 10;
        // printf("x: %d, h: %d, n: %d\n", x, harshad_n, n);
    }
    return x % harshad_n == 0 ? true : false;
}


int main(){
    printf("%d\n", solution(10)); //true
    printf("%d\n", solution(12)); //true
    printf("%d\n", solution(11)); //false
    printf("%d\n", solution(13)); //false
    printf("%d\n", solution(10000)); //true
    printf("%d\n", solution(9999)); //false
    return 0;
}
