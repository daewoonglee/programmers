"""
문제 설명
가로 길이가 2이고 세로의 길이가 1인 직사각형모양의 타일이 있습니다.
이 직사각형 타일을 이용하여 세로의 길이가 2이고 가로의 길이가 n인 바닥을 가득 채우려고 합니다. 타일을 채울 때는 다음과 같이 2가지 방법이 있습니다.

타일을 가로로 배치 하는 경우
타일을 세로로 배치 하는 경우
예를들어서 n이 7인 직사각형은 다음과 같이 채울 수 있습니다.

Img

직사각형의 가로의 길이 n이 매개변수로 주어질 때, 이 직사각형을 채우는 방법의 수를 return 하는 solution 함수를 완성해주세요.

제한사항
가로의 길이 n은 60,000이하의 자연수 입니다.
경우의 수가 많아 질 수 있으므로, 경우의 수를 1,000,000,007으로 나눈 나머지를 return해주세요.

입출력 예
n	result
4	5

입출력 예 설명
입출력 예 #1
다음과 같이 5가지 방법이 있다.
"""

from math import factorial
def solution(n):
    # 테스트 통과하지만 효율성 통과 X - 0.101247703
    # N = 1000000007
    # row, col = divmod(n, 2)
    # ans = 0
    # while row >= 0:
    #     m = 1
    #     for i in range(row):
    #         m *= row+col-i
    #     ans += m // factorial(row)
    #     if ans >= N:
    #         ans %= N
    #     row -= 1
    #     col += 2
    # return ans

    # 0.043514741999999995
    if n == 1:
        return 1
    N = 1000000007
    fibo = [1, 2]
    for _ in range(n-2):
        fibo[0], fibo[1] = fibo[1], (fibo[0]+fibo[1]) % N
    return fibo[1]


print(solution(1))
print(solution(2))
print(solution(3))
print(solution(4))
print(solution(5))
print(solution(7))


if __name__ == '__main__':
    from timeit import Timer
    query = [1, 2, 3, 4, 5, 7]
    t = Timer(f"for t in {query}: solution(t)", "from __main__ import solution")
    print(t.timeit(number=10000))
