#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

// 파라미터로 주어지는 문자열은 const로 주어집니다. 변경하려면 문자열을 복사해서 사용하세요.
int solution(const char* t, const char* p) {
    int ans = 0;
    int TN = strlen(t);
    int PN = strlen(p);
    
    for(int i=0; i<=TN-PN; i++){
        if(strncmp(t+i, p, PN) <= 0)
            ans++;
    }
    return ans;
}

int main(){
    printf("%d\n", solution("3141592", "271")); // 2
    printf("%d\n", solution("500220839878", "7")); // 8
    printf("%d\n", solution("10203", "15")); // 3
    printf("%d\n", solution("1221351118575141528544", "12511")); // 1
    return 0;
}
