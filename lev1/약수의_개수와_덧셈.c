#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>


int sum_square_number(int x){
    return (x * (x + 1) * (2 * x + 1) / 6);
}

int solution(int left, int right) {
    // int ans = 0;
    // for(int i=left; i<=right; i++){
    //     bool is_div = false;
    //     // 2.643107
    //     // for(int j=1; j<=(int)sqrt(i)+1; j++){
    //     // code refactoring - 1.376362(without callback function (sqrt))
    //     for(int j=1; j*j<=i; j++){
    //         if(i%j==0 & j*j==i){
    //             is_div = true;
    //             break;
    //         }
    //     }
    //     ans += is_div ? -i : i;
    // }
    // return ans;
    
    // code refactoring - 0.001346 -> 0.000599 (약 55% 성능 증진)
    int ans = (right-left+1)*(left+right)/2; // sum left to right
    ans -= 2 * (sum_square_number(sqrt(right)) - sum_square_number(sqrt(left - 1)));
    return ans;
}


int main(){
    clock_t tic = clock();
    for (int i=0; i<10000; i++){
        solution(13, 17);
        solution(24, 27);
        solution(1, 1);
        solution(1,1000);
        solution(1,997);
    }
    clock_t toc = clock();
    printf("running time: %f\n", (double)(toc-tic) / CLOCKS_PER_SEC);
    return 0;
}
