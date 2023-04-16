def solution(r1, r2):
    def cnt_coords(r):
        return r**2 if ((r-1)**2)*2 <= r**2 else r**2-1
    coords = cnt_coords(r2)-cnt_coords(r1)-(r2-r1)*2 # (x,0), (0,y) 제외
    return coords*4 + (r2-r1+1)*4


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
print(solution(2, 5)) # 72
