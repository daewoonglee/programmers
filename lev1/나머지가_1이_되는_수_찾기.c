#include <stdio.h>
#include <stdbool.h>
#include <string.h>

int solution(int n) {
    // get prime number using Eratosthenes algorithm.
    bool prime[n+2]; // 소수2를 인덱스 시작 2로 설정하기 위해 +2
    memset(prime, true, sizeof(prime));

    for(int i=2; i*i<n; i++){
        if(prime[i]){
            for(int j=i*i; j<n; j+=i)
                prime[j] = false;
        }
    }

    for(int i=2; i<n; i++){
        if(prime[i]){
            if(n%i==1)
                return i;
        }
    }
    
    
    return 0;
}

int main(){
    printf("%d\n", solution(10)); //3
    printf("%d\n", solution(12)); //11
    return 0;
}
