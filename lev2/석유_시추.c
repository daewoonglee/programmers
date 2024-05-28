#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>


int move_xy[4][2] = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};


void bfs(int** land, int x, int y, int* oil_cols, size_t rows, size_t cols){
    int oil = 1;
    int *col = (int *)malloc(sizeof(int)*cols);
    for(int i=0; i<cols; i++)
        col[i] = -1;

    int queue[rows*cols][2];
    int front = 0, rear = 0;

    land[x][y] = 0;
    queue[rear][0] = x;
    queue[rear][1] = y;
    rear++;

    int idx = 0;
    int flag = 0;
    while (front < rear){
        int cur_x = queue[front][0];
        int cur_y = queue[front][1];
        front++;

        for (int i=0; i<cols; i++)
            printf("Y: %d, col: %d\n", cur_y, col[i]);
        

        flag = 0;
        for (int i=0; i<cols; i++){
            if(col[i] == cur_y){
                flag = 1;
                break;
            }
        }
        printf("WITHOUR flag %d,  IDX: %d\n", flag, idx);
        printf("********\n");
        if (!flag){
            col[idx] = cur_y;
            idx++;
        }

        for (int i=0; i<4; i++){
            int nx = move_xy[i][0] + cur_x;
            int ny = move_xy[i][1] + cur_y;
            if (0 <= nx && nx < rows && 0 <= ny && ny < cols && land[nx][ny] == 1){
                queue[rear][0] = nx;
                queue[rear][1] = ny;
                land[nx][ny] = 0;
                oil++;
                rear++;
            }
        }
    }
    for (int i=0; i<cols; i++){
        printf("i: %d, col[i]: %d\n", i, col[i]);
        if (col[i] != -1)
            oil_cols[col[i]] += oil;
    }
    for (int i=0; i<cols; i++){
        printf("oil_cols: %d\n", oil_cols[i]);
    }
    printf("\n");

    free(col);
}

// land_rows는 2차원 배열 land의 행 길이, land_cols는 2차원 배열 land의 열 길이입니다.
int solution(int** land, size_t land_rows, size_t land_cols) {
    int ans = 0;
    int *oil_drilling = (int*)malloc(sizeof(int)*land_cols);
    for (int i=0; i<land_cols; i++)
        oil_drilling[i] = 0;

    for (int i=0; i<land_rows; i++){
        for (int j=0; j<land_cols; j++){
            if (land[i][j] == 1){
                bfs(land, i, j, oil_drilling, land_rows, land_cols);
            }
        }
    }
    for (int i=0; i<land_cols; i++){
        printf("oil: %d, ans: %d\n", oil_drilling[i], ans);
        ans = ans > oil_drilling[i] ? ans : oil_drilling[i];
    }
    free(oil_drilling);
    return ans;
}

int main(){
    // int row = 5, col = 8;
    // int values[5][8] = {
    //     {0, 0, 0, 1, 1, 1, 0, 0},
    //     {0, 0, 0, 0, 1, 1, 0, 0},
    //     {1, 1, 0, 0, 0, 1, 1, 0},
    //     {1, 1, 1, 0, 0, 0, 0, 0},
    //     {1, 1, 1, 0, 0, 0, 1, 1}
    // };
    int row = 7, col = 6;
    int values[7][8] = {
        {1, 0, 1, 0, 1, 1},
        {1, 0, 1, 0, 0, 0},
        {1, 0, 1, 0, 0, 1},
        {1, 0, 0, 1, 0, 0},
        {1, 0, 0, 1, 0, 1},
        {1, 0, 0, 0, 0, 0},
        {1, 1, 1, 1, 1, 1}
    };

    int **arr = (int**)malloc(sizeof(int*) * row);
    for(int i=0; i<row; i++){
        arr[i] = (int*) malloc(sizeof(int) * col);
        for(int j = 0; j < col; j++)
            arr[i][j] = values[i][j];
    }
    printf("ans: %d\n", solution(arr, row, col));

    for(int i = 0; i < row; i++)
        free(arr[i]);
    free(arr);
    return 0;
}

