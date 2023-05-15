#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

// a_len은 배열 a의 길이입니다.
// b_len은 배열 b의 길이입니다.
int solution(int a[], size_t a_len, int b[], size_t b_len) {
    int ans = 0;
    for(int i=0; i<a_len; i++)
        ans += (a[i] * b[i]);
    return ans;
}


int main(){
    int arr[2][4] = {
        {1,2,3,4},
        {-3,-1,0,2}
    };
    int arr1[2][3] = {
        {-1,0,1},
        {1,0,-1}
    };
    printf("%d\n", solution(arr[0], 4, arr[1], 4)); //3
    printf("%d\n", solution(arr1[0], 3, arr1[1], 3)); //-2
    return 0;
}
