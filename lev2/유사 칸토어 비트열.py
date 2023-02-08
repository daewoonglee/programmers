import math
def solution(n, l, r):
    # def cnt_cantor(N, remainder):
    #     plus = [0, 1, 2, 2, 3]
    #     cnt = 0
    #     while N > 1:
    #         bit = 4**N // 4
    #         length = 5**(N-1)
    #         quotient, remainder = divmod(remainder, length)
    #
    #         # # 1.765711215
    #         # cnt += bit * len([q for q in range(0, quotient) if q != 2])
    #
    #         # code refactoring - 1.199981254
    #         cnt += bit * quotient if quotient <= 2 else bit * (quotient-1) # q=2면 00000 구간이라서 -1로 해당 카운트 제외
    #         # print(f"q: {quotient}, r: {remainder}, len: {length}, bit: {bit}, cnt: {cnt}")
    #         N -= 1
    #
    #         # 00000 구간인 경우이면 그 이후 계산X
    #         if quotient == 2:
    #             break
    #     else:
    #         cnt += plus[remainder]
    #
    #     return cnt
    #
    # if n == 1:
    #     return "11011"[l-1:r].count("1")
    #
    # L = cnt_cantor(n, l-1)
    # R = cnt_cantor(n, r)
    #
    # return R - L

    # code refactoring - 0.619151372
    # 5^n 전체 범위에 대한 1의 개수 : 4^n
    def sol(x):
        if x <= 2:
            return x
        elif x <= 5:
            return x - 1

        base = int(math.log(x) // math.log(5))
        bit = 4 ** base
        length = 5 ** base
        quotient = x // length
        remainder = x % length

        ans = bit * quotient if quotient <= 2 else bit * (quotient-1)
        # print(f"base: {base}, q: {quotient}, r: {remainder}, ans: {ans}")

        if quotient == 2:
            return ans

        return ans + sol(remainder)

    L = sol(l - 1)
    R = sol(r)
    # print(f"R: {R}, L: {L}")

    return R - L


# print(solution(1, 2, 5)) # 3

# print(solution(2, 1, 1)) # 1
# print(solution(2, 3, 3)) # 0
# print(solution(2, 1, 5)) # 4
# print(solution(2, 4, 8)) # 4
# print(solution(2, 4, 20)) # 10
# print(solution(2, 4, 25)) # 14
# print(solution(2, 4, 19)) # 9
# print(solution(2, 3, 14)) # 6
# print(solution(2, 17, 24)) # 6
# print(solution(2, 10, 24)) # 8

# print(solution(3, 1, 16)) # 9
# print(solution(3, 1, 25)) # 16
# print(solution(3, 1, 125)) # 64
# print(solution(3, 4, 99)) # 45
# print(solution(3, 4, 100)) # 46
print(solution(3, 20, 25)) # 5

# print(solution(4, 1, 64)) # 32
# print(solution(4, 1, 125)) # 64
# print(solution(4, 4, 600)) # 238
# print(solution(4, 500, 600)) # 49

# print(solution(5, 1, 256)) # 128
# print(solution(5, 1, 625)) # 256

# print(solution(20, 4, 19)) # 9


if __name__ == "__main__":
    from timeit import Timer
    query = [
        [1,2,5], [2,1,1],[2,3,3],[2,1,5],[2,6,8],[2,6,20],[2,6,25],[2,10,19],[2,3,14],[2,17,24],[2,10,24],
        [3,1,16],[3,1,25],[3,1,125],[3,4,99],[3,4,100],[3,20,25],[4,50,64],[4,100,125],[4,4,600],[4,500,600],
        [5,1,256],[5,1,625],[20,4,19],[20,400,5**19], [20,5**10, 5**19]
    ]
    t = Timer(f"for t in {query}: solution(*t)", "from __main__ import solution")
    print(t.timeit(number=10000))
