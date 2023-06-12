#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

// number_len은 배열 number의 길이입니다.
int solution(int number[], size_t number_len) {
    int ans=0;
    int total=0;
    for(int i=0; i<number_len; i++){
        total += number[i];
        for(int j=i+1; j<number_len; j++){
            total += number[j];
            for(int z=j+1; z<number_len; z++){
                if(total+number[z] == 0)
                    ans += 1;
            }
            total -= number[j];
        }
        total = 0;
    }
    return ans;
}


int main(){
    int arr[3][7] = {
        {-2, 3, 0, 2, -5},
        {-3, -2, -1, 0, 1, 2, 3},
        {-1, 1, -1, 1}
    };
    printf("%d\n", solution(arr[0], 5)); //2
    printf("%d\n", solution(arr[1], 7)); //5
    printf("%d\n", solution(arr[2], 4)); //0
    return 0;
}
