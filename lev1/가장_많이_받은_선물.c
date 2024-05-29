#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>


typedef struct{
    char names[11];
    int index;
} Friend;

// friends_len은 배열 friends의 길이입니다.
// gifts_len은 배열 gifts의 길이입니다.
// 파라미터로 주어지는 문자열은 const로 주어집니다. 변경하려면 문자열을 복사해서 사용하세요.
int solution(const char* friends[], size_t friends_len, const char* gifts[], size_t gifts_len) {
    Friend friend_name_idx[friends_len];
    for (int i=0; i<friends_len; i++){
        strcpy(friend_name_idx[i].names, friends[i]);
        friend_name_idx[i].index = i;
    }
    
    int **gift_log = (int**)malloc(sizeof(int*)*friends_len);
    for (int i=0; i<friends_len; i++){
        gift_log[i] = (int*)malloc(sizeof(int)*friends_len);
        for (int j=0; j<friends_len; j++)
            gift_log[i][j] = 0;
    }
    for (int i=0; i<gifts_len; i++){
        char gift_copy[22];
        strncpy(gift_copy, gifts[i], sizeof(gift_copy)-1);
        gift_copy[sizeof(gift_copy) - 1] = '\0'; 

        char *friend1 = strtok(gift_copy, " ");
        char *friend2 = strtok(NULL, " ");

        int friend1_idx = 0;
        int friend2_idx = 0;

        for (int j=0; j<friends_len; j++){
            if (!strcmp(friend_name_idx[j].names, friend1))
                friend1_idx = friend_name_idx[j].index;
            if (!strcmp(friend_name_idx[j].names, friend2))
                friend2_idx = friend_name_idx[j].index;
        }
        gift_log[friend1_idx][friend2_idx]++;
    }

    int gift_index[friends_len];
    for (int i=0; i<friends_len; i++){
        int row_sum = 0;
        for (int j=0; j<friends_len; j++)
            row_sum += gift_log[i][j];
        int col_sum = 0;
        for (int j=0; j<friends_len; j++)
            col_sum += gift_log[j][i];
        gift_index[i] = row_sum - col_sum;
    }
    
    int ans_arr[friends_len];
    for (int i=0; i<friends_len; i++)
        ans_arr[i] = 0;
    for (int i=0; i<friends_len; i++){
        for (int j=i+1; j<friends_len; j++){
            int gift_cnt1 = gift_log[i][j];
            int gift_cnt2 = gift_log[j][i];
            if (gift_cnt1 == gift_cnt2){
                if (gift_index[i] > gift_index[j])
                    ans_arr[i] += 1;
                else if (gift_index[i] < gift_index[j])
                    ans_arr[j] += 1;
            }
            else 
                ans_arr[gift_cnt1 > gift_cnt2 ? i : j] += 1;
        }
    }
    int ans = 0;
    for (int i=0; i<friends_len; i++){
        if (ans < ans_arr[i])
            ans = ans_arr[i];
    }
    return ans;
}

int main(){
    // const char *friends[] = {"muzi", "ryan", "frodo", "neo"};
    // const char *gifts[] = {"muzi frodo", "muzi frodo", "ryan muzi", "ryan muzi", "ryan muzi", "frodo muzi", "frodo ryan", "neo muzi"};
    const char *friends[] = {"aaaaaaaaaa", "bbbbbbbbbb", "c", "d", "e", "f"};
    const char *gifts[] = {"aaaaaaaaaa bbbbbbbbbb"};
    size_t friends_len = sizeof(friends)/sizeof(friends[0]);
    size_t gifts_len = sizeof(gifts)/sizeof(gifts[0]);
    printf("ans: %d\n", solution(friends, friends_len, gifts, gifts_len));
    return 0;
}
