#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

// numbers_len은 배열 numbers의 길이입니다.
int solution(int numbers[], size_t numbers_len) {
    int total = 0;
    for(int i=0; i<numbers_len; i++)
        total += numbers[i];
    return 45-total;
}


int main(){
    int arr1[] = {1,2,3,4,6,7,8,0};
    printf("%d\n", solution(arr1, 8));//14
    int arr2[] = {5,8,4,0,6,7,9};
    printf("%d\n", solution(arr2, 7));//6
    return 0;
}
