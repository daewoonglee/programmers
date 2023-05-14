#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

char* solution(int n) {
    // // 리턴할 값은 메모리를 동적 할당해주세요.
    char* ans = (char*)malloc(sizeof(char)*(n*3+1));
    strcpy(ans, "");
    for(int i=0; i<n; i++)
        strcat(ans, i%2==0 ? "수" : "박");
    ans[n*3+1] = '\0';
    return ans;
    
}


int main(){
    printf("%s\n", solution(3)); //"수박수"
    printf("%s\n", solution(4)); //"수박수박"
    return 0;
}
