#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>


// edges_rows는 2차원 배열 edges의 행 길이, edges_cols는 2차원 배열 edges의 열 길이입니다.
int* solution(int** edges, size_t edges_rows, size_t edges_cols) {
    // return 값은 malloc 등 동적 할당을 사용해주세요. 할당 길이는 상황에 맞게 변경해주세요.
    int* ans = (int*)malloc(sizeof(int)*edges_rows);
    memset(ans, 0, edges_rows*sizeof(int));

    int N = 0;
    for (int row=0; row<edges_rows; row++){
        for(int col=0; col<edges_cols; col++){
            if (edges[row][col] > N) 
                N = edges[row][col];
        }
    }
    printf("N: %d\n", N);

    int* inout_edges = (int*)malloc(sizeof(int)*(N+1)*2);
    memset(inout_edges, 0, (N+1)*2*sizeof(int));
    for (int row=0; row<edges_rows; row++){
        int a = edges[row][0];
        int b = edges[row][1];
        inout_edges[b*2]++;
        inout_edges[a*2+1]++;
    }

    int total_out_edges = 0;
    for (int i=0; i<N+1; i++){
        printf("i: %d, input: %d, output: %d\n", i, inout_edges[i*2], inout_edges[i*2+1]);
        int in_edge = inout_edges[i*2];
        int out_edge = inout_edges[i*2+1];
        if (in_edge == 0){
            if (out_edge >= 2){
                ans[0] = i;
                total_out_edges = out_edge;
            }
        }
        else {
            if (out_edge == 0) ans[2]++;
            else if (out_edge == 2) ans[3]++;
        }
    }
    free(inout_edges);
    ans[1] = total_out_edges - (ans[2]+ans[3]);
    return ans;
}

int main(){
    int** arr = (int**)malloc(sizeof(int*)*4);
    for (int i=0; i<4; i++)
        arr[i] = (int*)malloc(sizeof(int)*2);

    // int values[4][2] = {{2, 3}, {4, 3}, {1, 1}, {2, 1}}; // [2, 1, 1, 0]
    int values[4][2] = {{20, 0}, {1, 0}, {20, 3}, {3, 3}}; // [2, 1, 1, 0]
    for (int i=0; i<4; i++){
        for (int j=0; j<2; j++){
            // printf("values %d ", values[i][j]);
            arr[i][j] = values[i][j];
        }
        // printf("\n");
    }

    int* res = solution(arr, 4, 2);
    for (int i=0; i<4; i++)
        printf("%d ", res[i]);

    free(res);
    free(arr);
}


