#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

char* solution(int num) {
    char* answer = (char*)malloc(4);
    if (num % 2 == 0)
        answer = "Even";
    else
        answer = "Odd";
    return answer;
    
}

int main(){
    printf("%s\n", solution(3));
    printf("%s\n", solution(2147483647));
    return 0;
}


