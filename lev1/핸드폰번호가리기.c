#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

// 파라미터로 주어지는 문자열은 const로 주어집니다. 변경하려면 문자열을 복사해서 사용하세요.
char* solution(const char* phone_number) {
    int N = strlen(phone_number); 
    char* ans = (char*)malloc(sizeof(char) * (N+1)); // \0
    char* hide_number = "****************";
    strcpy(ans, phone_number);
    strncpy(ans, hide_number, N-4);
    return ans;
}


int main(){
    printf("%s\n", solution("01033334444")); //"*******4444"
    printf("%s\n", solution("027778888")); //"*****8888"
    return 0;
}
