#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int solution(int n) {
    int ans = 0;
    while(n>0){
        ans += n % 10;
        n /= 10;
    }
    return ans;
}


int main(){
    printf("%d\n", solution(123)); //6
    printf("%d\n", solution(987)); //24
    printf("%d\n", solution(10000000)); //1
    return 0;
}
