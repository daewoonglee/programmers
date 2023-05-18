#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

// 파라미터로 주어지는 문자열은 const로 주어집니다. 변경하려면 문자열을 복사해서 사용하세요.
char* solution(const char* s) {
    const int N = strlen(s);
    // return 값은 malloc 등 동적 할당을 사용해주세요. 할당 길이는 상황에 맞게 변경해주세요.
    char* ans = (char*)malloc(sizeof(char)*(N+1)); //'\0'
    strcpy(ans, s);
    for(int i=0; i<N; i++){
        for(int j=i+1; j<N; j++){
            if(ans[i] < ans[j]){
                char t = ans[i];
                ans[i] = ans[j];
                ans[j] = t;
            }
        } 
    }
    return ans;
}


int main(){
    // printf("%s\n", solution("Zbcdefg")); //"gfedcbZ"
    printf("%s\n", solution("cdbefZg")); //"gfedcbZ"

    return 0;
}
