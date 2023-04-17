def solution(r1, r2):
    def cnt_coords(r):
        total = r_square = r*r
        for x in range(r-1, -1, -1):
            cnt = 0
            y = r-1
            while r_square < x**2 + y**2:
                cnt += 1
                y -= 1
            if cnt == 0:
                break
            total -= cnt
        return total

    # r2-r1+1 = 1사분면에 해당하는 좌표 수, 4사분면에 대해 모두 카운트하여 *4하면 중복 계산
    # 중복 계산을 없애고자 1사분면에 해당하는 좌표를 제외하고 *4 진행
    print(cnt_coords(r2))
    print(cnt_coords(r1))
    return (cnt_coords(r2)+2-cnt_coords(r1)-(r2-r1+1))*4


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
print(solution(6, 7)) # 40


