#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

// absolutes_len은 배열 absolutes의 길이입니다.
// signs_len은 배열 signs의 길이입니다.
int solution(int absolutes[], size_t absolutes_len, bool signs[], size_t signs_len) {
    int ans = 0;
    for(int i=0; i<absolutes_len; i++)
        ans += signs[i] ? absolutes[i] : -absolutes[i];
    return ans;
}


int main(){
    int arr[][3] = {
        {4, 7, 12},
        {1, 2, 3},
        {1, 1, 1},
        {1, 1, 1}
    };
    bool sign[][3] = {
        {true, false, true},
        {false, false, true},
        {false, false, false},
        {true, true, true}
    };
    printf("%d\n", solution(arr[0], 3, sign[0], 3)); //9
    printf("%d\n", solution(arr[1], 3, sign[1], 3)); //0
    printf("%d\n", solution(arr[2], 3, sign[2], 3)); //0
    printf("%d\n", solution(arr[3], 3, sign[3], 3)); //0
    return 0;
}
