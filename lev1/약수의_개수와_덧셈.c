#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <math.h>

int solution(int left, int right) {
    int ans = 0;
    for(int i=left; i<=right; i++){
        bool is_div = false;
        for(int j=1; j<(int)sqrt(i)+1; j++){
            if(i%j==0 & j*j==i){
                is_div = true;
                break;
            }
        }
        // printf("i: %d, div: %d\n", i, div);
        ans += is_div ? -i : i;
    }
    return ans;
}


int main(){
    printf("%d\n", solution(13, 17)); //43
    printf("%d\n", solution(24, 27)); //52
    printf("%d\n", solution(1, 1)); //-1
    return 0;
}
