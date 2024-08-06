#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

typedef struct Queue{
    int *queue;
    int front;
    int rear;
    int size;
} queue;

void init_queue(queue *q, int size){
    q->queue = (int*)malloc(sizeof(int)*size);
    q->front = 0;
    q->rear = 0;
    q->size = size;
}

bool is_empty(queue* q){
    return (q->front == q->rear) ? true : false;
}

void push(queue *q, int x){
    q->queue[q->rear] = x;
    q->rear = (q->rear+1) % q->size;
}

int pop(queue *q){
    int x = q->queue[q->front];
    q->front = (q->front+1) % q->size;
    return x;
}

void free_queue(queue *q){
    free(q->queue);
}

int* solution(int n, int** roads, size_t roads_rows, size_t roads_cols, int sources[], size_t sources_len, int destination) {
    int* ans = (int*)malloc(sizeof(int)*sources_len);
    int* lookup_table = (int*)malloc(sizeof(int)*(n+1));
    for (int i=0; i<n+1; i++)
        lookup_table[i] = -1;
        
    int** road_path = (int**)malloc(sizeof(int*)*(n+1));
    int* col_cnt = (int*)calloc(n+1, sizeof(int)); // 동적 col size 계산
    for (int i=0; i<roads_rows; i++){
        col_cnt[roads[i][0]]++;
        col_cnt[roads[i][1]]++;
    }
    
    for (int i=0; i<n+1; i++){
        road_path[i] = (int*)calloc(col_cnt[i], sizeof(int));
        col_cnt[i] = 0; // 동적 indexing 목적으로 0 초기화
    }
    for (int i=0; i<roads_rows; i++){
        int a = roads[i][0];
        int b = roads[i][1];
        road_path[a][col_cnt[a]++]=b; // 동적으로 indexing하여 값 할당
        road_path[b][col_cnt[b]++]=a; // 동적으로 indexing하여 값 할당
    }

    lookup_table[destination] = 0;
    queue q;
    init_queue(&q, n+1);
    push(&q, destination);

    while (!is_empty(&q)){
        int cur_node = pop(&q);
        int depth = lookup_table[cur_node];
        for (int i=0; i<col_cnt[cur_node]; i++){
            int next_node = road_path[cur_node][i];
            if (lookup_table[next_node] == -1 & next_node != 0){
                lookup_table[next_node] = depth+1;
                push(&q, next_node);
            }
        }
    }
    for (int i=0; i<sources_len; i++)
        ans[i] = lookup_table[sources[i]];
    
    free_queue(&q);
    free(lookup_table);
    free(col_cnt);
    for (int i=0; i<n+1; i++)
        free(road_path[i]);
    free(road_path);
    return ans;
}

int main(){
    // int values[][2] = {{1, 2}, {2, 3}}; // [1,2]
    // int values[][2] = {{1, 2}, {1, 4}, {2, 4}, {2, 5}, {4, 5}}; // [2,-1,0]
    int values[][2] = {{1, 2}, {1, 3}, {1, 5}, {5, 4}, {2, 3}, {3, 5}}; // [0,1,1,2,1]
    int rows = sizeof(values) / sizeof(values[0]);

    int** arr = (int**)malloc(sizeof(int*)*rows);
    for (int i=0; i<rows; i++)
        arr[i] = (int*)malloc(sizeof(int)*2);

    for (int i=0; i<rows; i++){
        for (int j=0; j<2; j++)
            arr[i][j] = values[i][j];
    }
    int sources[] = {1,2,3,4,5};

    int* res = solution(6, arr, rows, 2, sources, sizeof(sources)/sizeof(sources[0]), 1);
    for (int i=0; i<sizeof(sources)/sizeof(sources[0]); i++)
        printf("%d ", res[i]);

    for (int i=0; i<rows; i++)
        free(arr[i]);
    free(arr);
    free(res);
}


