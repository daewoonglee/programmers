#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <math.h>

#define EPSILON 1e-6

int solution(int h1, int m1, int s1, int h2, int m2, int s2) {
    int hms1 = h1*3600 + m1*60 + s1;
    int hms2 = h2*3600 + m2*60 + s2;
    int ans = 0;

    if (hms1 == 0 || hms1 == 12*3600) ans++;
    for (int sec=0; sec<hms2-hms1; sec++){
        int cur_s = s1 +sec;
        float cur_m = m1 + cur_s / 60.0;
        float cur_h = fmod((float)h1 + cur_m / 60, 12.0) * 5.0;

        cur_s %= 60;
        cur_m = fmod(cur_m, 60.0);
        cur_h = fmod(cur_h, 60.0);

        int next_s = s1 + sec+1;
        float next_m = m1 + (s1 + sec+1) / 60.0;
        float next_h = fmod((float)h1 + next_m / 60, 12.0) * 5.0;

        next_s = next_s % 60 != 0 ? next_s % 60 : 60;
        next_m = fmod(next_m, 60.0) != 0 ? fmod(next_m, 60.0) : 60.0;
        next_h = fmod(next_h, 60.0) != 0 ? fmod(next_h, 60.0) : 60.0;

        if (cur_s < cur_h && next_s >= next_h) ans++;
        if (cur_s < cur_m && next_s >= next_m) ans++;
        if ((fabs(next_s - next_m) < EPSILON) && (fabs(next_s - next_h) < EPSILON)) ans--;
    }
    return ans;
}

int main(){
    printf("ans: %d\n", solution(0,5,30,0,7,0)); // 2
    printf("ans: %d\n", solution(12,0,0,12,0,30)); // 1
    printf("ans: %d\n", solution(0,6,1,0,6,6)); // 0
    printf("ans: %d\n", solution(11,59,30,12,0,0)); // 1
    printf("ans: %d\n", solution(11,58,59,11,59,0)); // 1
    printf("ans: %d\n", solution(1,5,5,1,5,6)); // 2
    printf("ans: %d\n", solution(0,0,0,23,59,59)); // 2852
}
