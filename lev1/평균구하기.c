#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

// arr_len은 배열 arr의 길이입니다.
double solution(int arr[], size_t arr_len) {
    double ans;
    for (int i=0; i<arr_len; i++){
        ans += arr[i];
    }
    return ans / arr_len;
}

int main(){
    int arr[4] = {1,2,3,4};
    printf("%f\n",solution(arr, sizeof(arr)/sizeof(arr[0]))); //2.5
    int arr1[2] = {5,5};
    printf("%f\n",solution(arr1, sizeof(arr1)/sizeof(arr1[0]))); //5
    int arr2[100] = {0};
    for (int i=0; i<100; i++)
        arr2[i] = 10000;
    printf("%f\n",solution(arr2, sizeof(arr2)/sizeof(arr2[0]))); //10,000
    return 0;
}