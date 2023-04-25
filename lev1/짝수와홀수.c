#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <time.h>

char* solution(int num) {
    // // 0.017163
    // char* answer = (char*)malloc(4);
    // if (num % 2 == 0)
    //     answer = "Even";
    // else
    //     answer = "Odd";

    // code refactoring - 0.014269
    int d = num%2;
    char* answer = (char*)malloc(sizeof(char)*(5-d));
    answer = d ? "Odd" : "Even";
    return answer;
    
};

int main(){
    clock_t tic = clock();
    for (int i=0; i<100000; i++){
        solution(3);
        solution(2147483647);
        solution(2147483646);
    }
    clock_t toc = clock();
    printf("running time: %f\n", (double)(toc-tic) / CLOCKS_PER_SEC);
    return 0;
}


