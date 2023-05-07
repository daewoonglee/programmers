#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <time.h>


int sum(int x) {
    if(x<10) return x%10;   
    else return x%10 + sum(x/10); 
}

bool solution(int x) {
    // // 0.001444
    // int n = x;
    // int harshad_n = 0;
    // while(n>0){
    //     harshad_n += n%10;
    //     n /= 10;
    //     // printf("x: %d, h: %d, n: %d\n", x, harshad_n, n);
    // }
    // return x % harshad_n == 0 ? true : false;

    // code refactoring - recursive, 0.001838
    return (x%sum(x) == 0);
}




int main(){
    clock_t tic = clock();
    for (int i=0; i<10000; i++){
        solution(10);
        solution(12);
        solution(11);
        solution(13);
        solution(10000);
        solution(9999);
    }
    clock_t toc = clock();
    printf("running time: %f\n", (double)(toc-tic) / CLOCKS_PER_SEC);
    return 0;
}
