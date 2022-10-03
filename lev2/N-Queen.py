def solution(n):
    # def search_queen(li, col):
    #     global ans
    #     if len(col) == n:
    #         ans += 1
    #     else:
    #         for i in range(n):
    #             if i in li or i in col: continue
    #             search_queen([j-1 if idx % 2 == 0 else j+1 for idx, j in enumerate(li)] + [i-1, i+1], col + [i])
    #
    # # 4.174215736
    # global ans
    # ans = 0
    # for i in range(n):
    #     search_queen([i-1, i+1], [i])
    # return ans

    # code refactoring - 1.251609092
    # row=2, col=2
    # 퀸은 row+col이 같은 칸과 row-col이 같은 칸을 공격할 수 있습니다. (2, 2)에 있는 퀸은 (1, 3), (3, 1), (1, 1), (3, 3) 등을 공격할 수 있습니다
    cols = [False] * 32
    line1 = [False] * 32
    line2 = [False] * 32
    def search_queen(r):
        answer = 0
        if r == n+1:
            return 1
        for c in range(1, n+1):
            if cols[c] is False and line1[r+c] is False and line2[n+(r-c)] is False:
                cols[c] = True
                line1[r+c] = True
                line2[n+(r-c)] = True
                answer += search_queen(r+1)
                cols[c] = False
                line1[r+c] = False
                line2[n+(r-c)] = False
        return answer
    return search_queen(1)


print(solution(4)) # 2
# print(solution(5)) # 10
# print(solution(6)) # 4


if __name__ == "__main__":
    from timeit import Timer
    query = [i for i in range(1, 13)]
    t = Timer(f"for t in {query}: solution(t)", "from __main__ import solution")
    print(t.timeit(number=1))
