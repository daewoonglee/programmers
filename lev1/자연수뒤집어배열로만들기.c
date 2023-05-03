#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <math.h>

int* solution(long long n) {
    int size=(int)log10(n)+1;
    int* ans = (int*)malloc(sizeof(int)*size);
    for(int i=0; i<size; i++){
        ans[i] = n%10;
        n /= 10;
        printf("%d", ans[i]);
    }
    printf("\n");
    return ans;
}


int main(){
    solution(12345);
    solution(314);
    solution(9876543219);
    return 0;
}
