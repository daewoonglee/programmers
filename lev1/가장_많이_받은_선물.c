#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>


// friends_len은 배열 friends의 길이입니다.
// gifts_len은 배열 gifts의 길이입니다.
// 파라미터로 주어지는 문자열은 const로 주어집니다. 변경하려면 문자열을 복사해서 사용하세요.
int solution(const char* friends[], size_t friends_len, const char* gifts[], size_t gifts_len) {
    int gift_log[friends_len][friends_len];
    memset(gift_log, 0, sizeof(int)*friends_len*friends_len);
    for (int i=0; i<gifts_len; i++){
        char gift_copy[22];
        strncpy(gift_copy, gifts[i], sizeof(gift_copy)-1);
        gift_copy[sizeof(gift_copy) - 1] = '\0';

        char *friend1 = strtok(gift_copy, " ");
        char *friend2 = strtok(NULL, " ");

        int row = 0, col = 0;
        for (int j=0; j<friends_len; j++){
            if (strcmp(friend1, friends[j]) == 0)
                row = j;
            if (strcmp(friend2, friends[j]) == 0)
                col = j;
        }
        gift_log[row][col]++;
    }

    int gift_index[friends_len];
    for (int i=0; i<friends_len; i++){
        int row_sum = 0, col_sum = 0;
        for (int j=0; j<friends_len; j++){
            row_sum += gift_log[i][j];
            col_sum += gift_log[j][i];
        }

        gift_index[i] = row_sum - col_sum;
    }
    
    int ans = 0;
    for (int i=0; i<friends_len; i++){
        int tmp = 0;
        for (int j=0; j<friends_len; j++){
            int gift_cnt1 = gift_log[i][j];
            int gift_cnt2 = gift_log[j][i];
            if (i == j) continue;
            if (gift_cnt1 > gift_cnt2) tmp++;
            else if (gift_cnt1 == gift_cnt2 && gift_index[i] > gift_index[j]) tmp++;
        }
        ans = ans < tmp ? tmp : ans;
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
