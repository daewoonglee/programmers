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
    printf("\n N: %d\n", N);
    int* answer = (int*)malloc(sizeof(int)*(numbers_len+1));
    int* sums = (int*)calloc(N, sizeof(int));
    int idx = 0;
    for(int i=0; i<numbers_len; i++){
        for(int j=i+1; j<numbers_len; j++){
            printf("i: %d, j: %d, sum: %d, idx: %d\n", i, j, numbers[i]+numbers[j], idx);
            sums[idx] = numbers[i]+numbers[j];
            idx++;
        }
    }
    for(int i=0; i<N; i++)
        printf("%d ", sums[i]);
    printf("\n");
    qsort(sums, N, sizeof(int), compare);
    for(int i=0; i<N; i++)
        printf("%d ", sums[i]);
    printf("\n");

    int ans_idx = 1;
    answer[0] = sums[0];
    for(int i=1; i<N; i++){
        printf("ansidx: %d, i: %d ans: %d, sum: %d, flag: %d\n", ans_idx, i, answer[ans_idx-1], sums[i], answer[ans_idx-1] != sums[i]);
        if (answer[ans_idx-1] != sums[i]){
            answer[ans_idx] = sums[i];
            ans_idx++;
        }
    }
    printf("ans: %d, %d\n", answer[3], answer[4]);
    free(sums);
    printf("ans: %d, %d\n", answer[3], answer[4]);
    return answer;
}


int main(){
    int arr[3][5] = {
        {2,1,3,4,1},
        {5,0,2,7},
        {0,0}
    };
    int* arr1 = solution(arr[0], 5);
    for(int i=0; i<7; i++)
        printf("%d ", arr1[i]); // [2,3,4,5,6,7]
    printf("\n");

    int* arr2 = solution(arr[1], 4);
    for(int i=0; i<5; i++)
        printf("%d ", arr2[i]); //[2,5,7,9,12]
    printf("\n");

    int* arr3 = solution(arr[2], 2);
    for(int i=0; i<5; i++)
        printf("%d ", arr3[i]); //[0]
    printf("\n");

    return 0;
}
