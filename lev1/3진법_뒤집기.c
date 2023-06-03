#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <math.h>

void ternary(int n, int* n3, int *idx){
    int base = 3;
    while(n>0){
        n3[(*idx)++] = n%base;
        n/=base;
    }
    
}

int solution(int n) {
    int N = 0;
    int* n3 = (int*)malloc(sizeof(int)*17);
    ternary(n, n3, &N);

    int multi = N-1;
    int ans = 0;
    for(int i=0; i<N; i++){
        ans += ((int)pow(3, multi)*n3[i]);
        multi -= 1;
    }
    free(n3);
    return ans;
}

/*
3   45
3   15  0
3    5  0
    1   2

    1 2 0 0
    1*3^3 + 2*3^2 + 0*3^1 + 0*3^0 -> 45
    0 0 2 1
    0*3^3 + 0*3^2 + 2*3^1 + 1*3^0 -> 7
*/


int main(){
    printf("%d\n", solution(45)); //7
    printf("%d\n", solution(125)); //229
    return 0;
}
