#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

// 파라미터로 주어지는 문자열은 const로 주어집니다. 변경하려면 문자열을 복사해서 사용하세요.
char* solution(const char* s) {
    // return 값은 malloc 등 동적 할당을 사용해주세요. 할당 길이는 상황에 맞게 변경해주세요.
    int N = strlen(s);
    char* ans = (char*)malloc(sizeof(char)*(N+1)); // add '\0'

    int start = 'a';
    int end = 'z';
    int diff = 'a'-'A';
    int space = ' ';
    int j = 0;
    for(int i=0; i<N; i++){
        if(s[i]==space){
            j=0;
            ans[i] = s[i];
        }
        else{
            if(j++%2==0)
                ans[i] = (start<=s[i] & s[i]<=end) ? s[i]-diff : s[i];
            else
                ans[i] = (start<=s[i] & s[i]<=end) ? s[i] : s[i]+diff;
        }
    }
    ans[N]='\0';
    return ans;
}

int main(){
    // solution("try hello world"); //"TrY HeLlO WoRlD"
    solution("t r y"); //"T R Y"
    solution("T R Y"); //"t r y"
    solution("TT RR YY"); //"Tt Rr Yy"
    solution("tt rr yy"); //"Tt Rr Yy"
    return 0;
}
