#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

// scores_rows는 2차원 배열 scores의 행 길이, scores_cols는 2차원 배열 scores의 열 길이입니다.
int solution(int** scores, size_t scores_rows, size_t scores_cols) {
    int target1 = scores[0][0];
    int target2 = scores[0][1];
    int target = target1 + target2;

    for (int i=0; i<scores_rows; i++){
        for (int j=i+1; j<scores_rows; j++){
            if (scores[i][0] < scores[j][0]){
                int temp[2] = {scores[i][0], scores[i][1]};
                for (int z=0; z<2; z++){
                    scores[i][z] = scores[j][z];
                    scores[j][z] = temp[z];
                }
            }
        }
    }

    for (int i=0; i<scores_rows; i++){
        for (int j=i+1; j<scores_rows; j++){
            if (scores[i][1] > scores[j][1]){
                int temp[2] = {scores[i][0], scores[i][1]};
                for (int z=0; z<2; z++){
                    scores[i][z] = scores[j][z];
                    scores[j][z] = temp[z];
                }
            }
        }
    }

    int ans = 1;
    int max_b = 0;
    for (int i=0; i<scores_rows; i++){
        if (target1 < scores[i][0] & target2 < scores[i][1])
            return -1;
        
        if (scores[i][1] >= max_b){
            max_b = scores[i][1];
            if ((scores[i][0] + scores[i][1]) > target)
                ans++;
        }
    }

    return ans;
}

int main(){
    // int values[][2] = {{2,2},{1,4},{3,2},{3,2},{2,1}}; // 4
    // int values[][2] = {{2,2},{2,4},{2,2},{2,3},{2,1},{2,2}}; // 3
    // int values[][2] = {{0,3},{1,2},{1,2},{1,2},{1,1},{1,2},{1,2}}; // 1
    int values[][2] = {{0,0},{1,2},{2,1},{1,1},{1,2},{1,2}}; // -1
    
    int rows = sizeof(values) / sizeof(values[0]);

    int** arr = (int**)malloc(sizeof(int*)*rows);
    for (int i=0; i<rows; i++){
        arr[i] = (int*)malloc(sizeof(int)*2);
        for (int j=0; j<2; j++)
            arr[i][j] = values[i][j];
    }
    
    printf("%d\n", solution(arr, rows, 2));
    
    for (int i=0; i<rows; i++)
        free(arr[i]);
    free(arr);
}