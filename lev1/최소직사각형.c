#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

// sizes_rows는 2차원 배열 sizes의 행 길이, sizes_cols는 2차원 배열 sizes의 열 길이입니다.
int solution(int sizes[][2], size_t sizes_rows, size_t sizes_cols) {
    int h = 0;
    int w = 0;

    for(int i=0; i<sizes_rows; i++){
        if(sizes[i][0] < sizes[i][1]){
            int t = sizes[i][0];
            sizes[i][0] = sizes[i][1];
            sizes[i][1] = t;
        }
        if(h < sizes[i][0]) h = sizes[i][0];
        if(w < sizes[i][1]) w = sizes[i][1];
    }

    return h * w;
}

int main(){
    int arr[][2] = {{60, 50}, {30, 70}, {60, 30}, {80, 40}};
    printf("%d\n", solution(arr, 4, 2)); //4000
    int arr1[][2] = {{10, 7}, {12, 3}, {8, 15}, {14, 7}, {5, 15}};
    printf("%d\n", solution(arr1, 5, 2)); //120
    int arr2[][2] = {{14, 4}, {19, 6}, {6, 16}, {18, 7}, {7, 11}};
    printf("%d\n", solution(arr2, 5, 2)); //133
    return 0;
}
