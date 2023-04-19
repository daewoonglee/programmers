def solution(r1, r2):
    ans = 0
    for x in range(r2):
        for y in range(r2):
            if r1**2 <= x**2+y**2 <= r2**2:
                ans += 1
    ans += 2 # (r2,0), (0,r2) 추가
    return (ans-(r2-r1+1))*4


"""
1. 1사분면만 계산해서 *4
2. 위 *4를 할 때 (x,0), (0,y) 부분이 중복 계산 문제 발생
    2-1. (x,0), (0,y) 부분을 제외한 {(r2-1) 정수 좌표 & (r1-1) 정수 좌표 카운트} * 4 (4사분면까지 있으니)
    2-2. (x,0), (0,y) 부분 카운트 * 4
3. 2-1 + 2-2 카운트 반환
"""

# print(solution(2, 3)) # 20
# print(solution(1, 3)) # 28
# print(solution(2, 4)) # 40
# print(solution(3, 4)) # 24
# print(solution(2, 5)) # 72
# print(solution(2, 6)) # 104
# print(solution(6, 7)) # 40
print(solution(5, 6)) # 44
print(solution(5, 7)) # 80

