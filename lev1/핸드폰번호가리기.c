#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

// 파라미터로 주어지는 문자열은 const로 주어집니다. 변경하려면 문자열을 복사해서 사용하세요.
char* solution(const char* phone_number) {
    
    const int N = strlen(phone_number);
    char* ans = (char*)malloc(sizeof(char) * (N+1)); // \0
    strcpy(ans, phone_number);

    // // 0.002742
    // char* hide_number = "****************";
    // strncpy(ans, hide_number, N-4);

    // // 0.002520
    for(int i=0; i<N-4; i++)
        ans[i] = '*';

    return ans;
}


int main(){
    clock_t tic = clock();
    for (int i=0; i<10000; i++){
        solution("01033334444");
        solution("027778888");
        solution("1234");
        solution("11111111111111111111");
    }
    clock_t toc = clock();
    printf("running time: %f\n", (double)(toc-tic) / CLOCKS_PER_SEC);
    return 0;
}
