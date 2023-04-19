from math import sqrt, ceil, floor


def solution(r1, r2):
    ans = 0
    r1_square = r1*r1
    r2_square = r2*r2

    # # 0.9326737469999999
    # for i in range(1, r2+1):
    #     x1 = 0 if r1_square - i*i <= 0 else ceil(sqrt(r1_square-i*i))
    #     x2 = floor(sqrt(r2_square-i*i))
    #     ans += (x2-x1+1)
    # return ans * 4

    # code refactoring - 0.73335442
    for i in range(r1):
        ans += int(sqrt(r2_square - i*i)) - int(sqrt(r1_square - i*i - 1))
    for i in range(r1, r2):
        ans += int(sqrt(r2_square - i*i))
    return ans * 4


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
# print(solution(5, 6)) # 44
# print(solution(5, 7)) # 80
print(solution(5, 10)) # 248


if __name__ == "__main__":
    from timeit import Timer
    query = [
        [2,3],[1,3],[2,4],[3,4],[2,5],[2,6],[6,7],[5,6],[5,7],[5,10],[1,10000],[9999,10000]
    ]
    t = Timer(f"for t in {query}: solution(*t)", "from __main__ import solution")
    print(t.timeit(number=100))
