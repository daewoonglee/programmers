#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

// 파라미터로 주어지는 문자열은 const로 주어집니다. 변경하려면 문자열을 복사해서 사용하세요.
bool solution(const char* s) {
    int N = strlen(s);
    int zero = (int)'0';

    if(N == 4 || N == 6){
        for(int i=0; i<N; i++){
            if(zero>s[i] || zero+9<s[i])
                return false;
        }
        return true;
    }
    return false;
}


int main(){
    printf("%d\n", solution("a234")); //false
    printf("%d\n", solution("1234")); //true
    printf("%d\n", solution("01234567")); //false
    return 0;
}
