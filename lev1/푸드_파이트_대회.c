#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

// food_len은 배열 food의 길이입니다.
char* solution(int food[], size_t food_len) {
    int N = 1;
    for(int i=1; i<food_len; i++){
        if(food[i]%2 != 0)
            food[i]--;
        N += food[i];
    }

    char* answer = (char*)malloc(sizeof(char)*(N+1));
    int idx=0;
    for(int i=1; i<food_len; i++){
        for(int j=0; j<food[i]/2; j++)
            answer[idx++] = i+'0';
    }
    answer[idx++] = '0';
    for(int i=food_len-1; i>0; i--){
        for(int j=0; j<food[i]/2; j++)
            answer[idx++] = i+'0';
    }
    answer[idx] = '\0';
    return answer;
}

int main(){
    int s1[] = {1,3,4,6};
    printf("%s\n", solution(s1, 4)); // "1223330333221"
    int s2[] = {1,7,1,2};
    printf("%s\n", solution(s2, 4)); // "111303111"
    return 0;
}
