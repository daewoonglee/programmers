#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

int compare(const void *a, const void *b){
    return -(strcmp((char *)a, (char *)b));
};

void quick_sort(char arr[], int L, int R){
    int left = L;
    int right = R;
    int pivot = arr[(L + R) / 2];

    while(left <= right){
        while(arr[left] > pivot)
            left++;
        while(arr[right] < pivot)
            right--;
        if(left <= right){
            char tmp = arr[left];
            arr[left] = arr[right];
            arr[right] = tmp;

            left++;
            right--;
        }
    }

    if(L < right)
        quick_sort(arr, L, right);
    if(left < R)
        quick_sort(arr, left, R);
}

// 파라미터로 주어지는 문자열은 const로 주어집니다. 변경하려면 문자열을 복사해서 사용하세요.
char* solution(const char* s) {
    // // 3.919274
    // const int N = strlen(s);
    // char* ans = (char*)malloc(sizeof(char)*(N+1)); //'\0'
    // strcpy(ans, s);
    // for(int i=0; i<N; i++){
    //     for(int j=i+1; j<N; j++){
    //         if(ans[i] < ans[j]){
    //             char t = ans[i];
    //             ans[i] = ans[j];
    //             ans[j] = t;
    //         }
    //     } 
    // }
    // return ans;

    // // code refactoring - 0.191321(quicksort)
    // const int N = strlen(s);
    // char* ans = (char*)malloc(sizeof(char)*(N+1));
    // strcpy(ans, s);
    // quick_sort(ans, 0, N-1);

    // code refactoring - 0.629741(stdlib function)
    const int N = strlen(s);
    char* ans = (char*)malloc(sizeof(char)*(N+1));
    strcpy(ans, s);
    qsort(ans, N, sizeof(char), compare);
    return ans;
}


int main(){
    clock_t tic = clock();
    for (int i=0; i<10000; i++){
        solution("cdbefZg");
        solution("Zbcdefg");
        solution("ZbcdefgZbcdefgZbcdefgZbcdefgZbcdefgZbcdefgZbcdefgZbcdefgZbcdefgZbcdefg");
        solution("cdbefZgcdbefZgcdbefZgcdbefZgcdbefZgcdbefZgcdbefZgcdbefZgcdbefZg");
        solution("ZbcdefgZbcdefgZbcdefgZbcdefgZbcdefgZbcdefgZbcdefgZbcdefgZbcdefgZbcdefgZbcdefgZbcdefgZbcdefgZbcdefgZbcdefgZbcdefgZbcdefgZbcdefgZbcdefgZbcdefgZbcdefgZbcdefgZbcdefgZbcdefgZbcdefgZbcdefgZbcdefgZbcdefgZbcdefgZbcdefgZbcdefgZbcdefgZbcdefgZbcdefgZbcdefgZbcdefgZbcdefgZbcdefgZbcdefgZbcdefgZbcdefgZbcdefgZbcdefgZbcdefgZbcdefgZbcdefgZbcdefgZbcdefgZbcdefgZbcdefgZbcdefgZbcdefgZbcdefgZbcdefgZbcdefgZbcdefgZbcdefgZbcdefgZbcdefgZbcdefgZbcdefgZbcdefgZbcdefgZbcdefgZbcdefgZbcdefgZbcdefgZbcdefgZbcdefgZbcdefgZbcdefgZbcdefgZbcdefgZbcdefgZbcdefgZbcdefgZbcdefgZbcdefgZbcdefgZbcdefgZbcdefgZbcdefgZbcdefgZbcdefgZbcdefgZbcdefgZbcdefgZbcdefgZbcdefgZbcdefg");
    }
    clock_t toc = clock();
    printf("running time: %f\n", (double)(toc-tic) / CLOCKS_PER_SEC);
    return 0;
}
