#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <ctype.h>

// 파라미터로 주어지는 문자열은 const로 주어집니다. 변경하려면 문자열을 복사해서 사용하세요.
bool solution(const char* s) {
    // // 0.000830
    // int N = strlen(s);
    // int zero = (int)'0';

    // if(N == 4 || N == 6){
    //     for(int i=0; i<N; i++){
    //         if(zero>s[i] || zero+9<s[i])
    //             return false;
    //     }
    //     return true;
    // }
    // return false;

    // using ctype-digit function - 0.001284
    int N = strlen(s);
    if(N == 4 || N == 6){
        for(int i=0; i<N; i++){
            if(!isdigit(s[i]))
                return false;
        }
        return true;
    }
    return false;
}


int main(){
    clock_t tic = clock();
    for (int i=0; i<10000; i++){
        solution("a234");
        solution("1234");
        solution("01234567");
        solution("012347");
        solution("0ZZZ");
        solution("0123Z7");
        solution("654321");
    }
    clock_t toc = clock();
    printf("running time: %f\n", (double)(toc-tic) / CLOCKS_PER_SEC);
    return 0;
}
