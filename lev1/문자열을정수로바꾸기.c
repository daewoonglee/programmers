#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

// 파라미터로 주어지는 문자열은 const로 주어집니다. 변경하려면 문자열을 복사해서 사용하세요.
int solution(const char* s) {
    int LEN = strlen(s);
    int ans = 0;
    int start = 0;
    int sign = 1;

    if(s[0]==43) 
        start++;
    else if(s[0]==45){
        start++;
        sign = -1;
    }

    for(int i=start; i<LEN; i++)
        ans += (int)pow(10, LEN-i-1)*(int)(s[i]-'0');
    return ans * sign;
}


int main(){
    printf("%d\n", solution("1234"));
    printf("%d\n", solution("-1234"));
    return 0;
}
