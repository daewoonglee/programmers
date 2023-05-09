#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int solution(long num) {
    for(int i=0; i<500; i++){
        if(num == 1) return i;
        num = num%2==0 ? num/2 : num*3+1;
        
    }
    return -1;
}


int main(){
    printf("%d\n", solution(6)); //8
    printf("%d\n", solution(16)); //4
    printf("%d\n", solution(626331)); //-1
    printf("%d\n", solution(1)); //0
    return 0;
}
