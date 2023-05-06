#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <time.h>

// 파라미터로 주어지는 문자열은 const로 주어집니다. 변경하려면 문자열을 복사해서 사용하세요.
int solution(const char* s) {
    // // 0.004899
    // int LEN = strlen(s);
    // int ans = 0;
    // int start = 0;
    // int sign = 1;

    // if(s[0]==43) 
    //     start++;
    // else if(s[0]==45){
    //     start++;
    //     sign = -1;
    // }

    // for(int i=start; i<LEN; i++)
    //     ans += (int)pow(10, LEN-i-1)*(int)(s[i]-'0');
    // return ans * sign;

    // // code refactoring 01 - 0.001830
    // return atoi(s);

    //  code refactoring 02 - 0.000412
    int ans = 0;
    int sign = 1;
    int i = 0;

    if(s[0]==43) 
        i++;
    else if(s[0]==45){
        i++;
        sign = -1;
    }

    while(s[i]){
        ans = ans * 10 + (int)(s[i] - '0');
        i++;
    }
    return ans*sign;
}


int main(){
    clock_t tic = clock();
    for (int i=0; i<10000; i++){
        solution("1234");
        solution("-1234");
        solution("99999");
        solution("+9999");
        solution("-9999");
    }
    clock_t toc = clock();
    printf("running time: %f\n", (double)(toc-tic) / CLOCKS_PER_SEC);
    return 0;
}
