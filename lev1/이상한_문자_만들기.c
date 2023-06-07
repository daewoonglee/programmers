#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

// 파라미터로 주어지는 문자열은 const로 주어집니다. 변경하려면 문자열을 복사해서 사용하세요.
char* solution(const char* s) {
    int N = strlen(s);
    char* ans = (char*)malloc(sizeof(char)*(N+1)); // add '\0'
    
    // // 0.002256
    // int start = 'a';
    // int end = 'z';
    // int diff = 'a'-'A';
    // int space = ' ';
    // int j = 0;
    // for(int i=0; i<N; i++){
    //     if(s[i]==space){
    //         j=0;
    //         ans[i] = s[i];
    //     }
    //     else{
    //         if(j++%2==0)
    //             ans[i] = (start<=s[i] && s[i]<=end) ? s[i]-diff : s[i];
    //         else
    //             ans[i] = (start<=s[i] && s[i]<=end) ? s[i] : s[i]+diff;
    //     }
    // }

    // code refactoring - 0.002050
    int j = 0;
    for(int i=0; i<N; i++){
        if(s[i]==' '){
            j=0;
            ans[i] = s[i];
        }
        else{
            if(j++%2==0)
                ans[i] = (s[i]&32) ? s[i]^32 : s[i];
            else
                ans[i] = (s[i]&32) ? s[i] : s[i]|32;
        }
    }

    ans[N]='\0';
    return ans;
}

int main(){
    clock_t tic = clock();
    char q[7][60]={
        {"try hello world"},
        {"t r y"},
        {"T R Y"},
        {"TT RR YY"},
        {"tt rr yy"},
        {"ttttttttttttttttttttttttttttttttttttttttttttttttttttttt"},
        {"TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT"}
    };
    for (int i=0; i<10000; i++){
        char* a = solution(q[i%7]);
        free(a);
    }
    clock_t toc = clock();
    printf("running time: %f\n", (double)(toc-tic) / CLOCKS_PER_SEC);
    return 0;
}
