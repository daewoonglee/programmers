#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int compare(const void* n1, const void* n2){
    if(*(int*)n1 > *(int*)n2)
        return 1;
    else if(*(int*)n1 < *(int*)n2)
        return -1;
    else
        return 0;
}

// numbers_len은 배열 numbers의 길이입니다.
int* solution(int numbers[], size_t numbers_len) {
    int N = (numbers_len-1)*numbers_len/2;
    int* answer = (int*)malloc(sizeof(int)*N);
    int* sums = (int*)calloc(N, sizeof(int));
    int idx = 0;
    for(int i=0; i<numbers_len; i++){
        for(int j=i+1; j<numbers_len; j++){
            sums[idx] = numbers[i]+numbers[j];
            idx++;
        }
    }
    qsort(sums, N, sizeof(int), compare);
    
    int ans_idx = 1;
    answer[0] = sums[0];
    for(int i=1; i<N; i++){
        if (answer[ans_idx-1] != sums[i]){
            answer[ans_idx] = sums[i];
            ans_idx++;
        }
    }
    // free(sums);
    return answer;
}


int main(){
    int arr[4][5] = {
        {2,1,3,4,1},
        {5,0,2,7},
        {0,0},
        {1,10,100,1000,10000}
    };
    // int* arr1 = solution(arr[0], 5);
    // for(int i=0; i<7; i++)
    //     printf("%d ", arr1[i]); // [2,3,4,5,6,7]
    // printf("\n");

    // int* arr2 = solution(arr[1], 4);
    // for(int i=0; i<5; i++)
    //     printf("%d ", arr2[i]); //[2,5,7,9,12]
    // printf("\n");

    // int* arr3 = solution(arr[2], 2);
    // for(int i=0; i<5; i++)
    //     printf("%d ", arr3[i]); //[0]
    // printf("\n");

    int* arr4 = solution(arr[3], 5);
    for(int i=0; i<10; i++)
        printf("%d ", arr4[i]); //[0]
    printf("\n");

    return 0;
}
