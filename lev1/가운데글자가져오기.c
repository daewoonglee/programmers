#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

// 파라미터로 주어지는 문자열은 const로 주어집니다. 변경하려면 문자열을 복사해서 사용하세요.
char* solution(const char* s) {
    const int N = strlen(s);
    // return 값은 malloc 등 동적 할당을 사용해주세요. 할당 길이는 상황에 맞게 변경해주세요.
    char* ans;
    if(N%2==1){
        ans = (char*)malloc(sizeof(char)*2);
        ans[0] = s[(int)N/2];
        ans[1] = '\0';
    }
    else{
        ans = (char*)malloc(sizeof(char)*3);
        ans[0] = s[(int)N/2-1];
        ans[1] = s[(int)N/2];
        ans[2] = '\0';
    }
    return ans;
}


int main(){
    printf("%s\n", solution("abcde")); //"c"
    printf("%s\n", solution("qwer")); //"we"
    return 0;
}