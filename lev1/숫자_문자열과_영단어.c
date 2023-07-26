#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>

// 파라미터로 주어지는 문자열은 const로 주어집니다. 변경하려면 문자열을 복사해서 사용하세요.
int solution(const char* s) {
    char *table[] = {
        "zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"
    };
    int ans = 0;
    while(*s){
        if(isdigit(*s))
            ans = ans*10 + *s-'0';
        else{
            for(int j=0; j<10; j++){
                if(strncmp(s, table[j], strlen(table[j])) == 0){
                    ans = ans*10 + j;
                    s += strlen(table[j])-1;
                }
            }
        }
        s++;
    }
    return ans;
}


int main(){
    printf("%d\n", solution("one4seveneight")); //1478
    printf("%d\n", solution("23four5six7")); //234567
    printf("%d\n", solution("2three45sixseven")); //234567
    printf("%d\n", solution("123")); //123
    printf("%d\n", solution("onetwothree")); //123
    return 0;
}
