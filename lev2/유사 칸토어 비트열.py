def solution(n, l, r):
    # bit = "11011"
    # for _ in range(n - 1):
    #     bit = bit * 2 + "0" * len(bit) + bit * 2
    # return bit[l - 1: r].count("1")

    def cnt_cantor(N, d):
        plus = [0, 1, 2, 2, 3]
        cnt = 0
        while N > 1:
            bit = 4**N // 4
            length = 5**(N-1)
            q, d = divmod(d, length)

            cnt += bit * len([i for i in range(0, q) if i != 2])
            print(f"whille loop n: {N}, bit: {bit}, len: {length}, q: {q}, d: {d}, cnt: {cnt}")
            N -= 1

            if q == 2: break
        else:
            cnt += plus[d]

        return cnt

    if n == 1:
        return "11011"[l-1:r].count("1")

    L = cnt_cantor(n, l-1)
    print("-------")
    R = cnt_cantor(n, r)
    print(f"L: {L}, R: {R}\n")

    return R - L

"""
-풀이 방안-
L <= cantor <= R 범위 값을 구하려고하면 예외 상황이 너무 많이 발생
    > L,R이 같은 그룹(1/1/0/1/1)인 경우엔 L<=cantor<=R
    >       다른 그룹인 경우 
            > 다른 그룹 내 서브에서 같은 그룹인 경우 등 (실제 같은 그룹인게 아닌 가르키는 그룹 인덱스가 같음)
            
0<=cantor<=R - 0<=cantor<=L 로 하면 위 예외상황을 모두 무시할 수 있음 
단, 00000 00000 00000 00000 00000 구간에 들어간 경우 판단 필요, 어떻게 처리?
------------------------------------------------------------------------
1 2 3 4 5  6 7 8 9 10   11 12 13 14 15   16 17 18 19 20   21 22 23 24 25 (1-base)
1 1 0 1 1  1 1 0 1  1    0  0  0  0  0    1  1  0  1  1    1  1  0  1  1

1 2 3 4 5  6 7 8 9 10   11 12 13 14 15   16 17 18 19 20   21 22 23 24 25 (1-base)
1 1 0 1 1  1 1 0 1  1    0  0  0  0  0    1  1  0  1  1    1  1  0  1  1

1 2 3 4 5  6 7 8 9 60   61 62 63 64 65   16 17 18 19 20   21 22 23 24 25 (1-base)
0 0 0 0 0  0 0 0 0  0    0  0  0  0  0    0  0  0  0  0    0  0  0  0  0

n   bit                 total   len
1   1/1/0/1/1           4       5
2   4/4/0/4/4           16      25
3   16/16/0/16/16       64      125
4   64/64/0/64/64       256     625
5   256/256/0/256/256   1024    3125
"""


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
# print(solution(3, 20, 25)) # 5

# print(solution(4, 1, 64)) # 32
# print(solution(4, 1, 125)) # 64
# print(solution(4, 4, 600)) # 238
# print(solution(4, 500, 600)) # 49

print(solution(5, 1, 256)) # 128
# print(solution(5, 1, 625)) # 256

# print(solution(20, 4, 19)) # 9
