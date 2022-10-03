def solution(n):
    def search_queen(li, col):
        global ans
        if len(col) == n:
            ans += 1
        else:
            for i in range(n):
                if i in li or i in col: continue
                search_queen([j-1 if idx % 2 == 0 else j+1 for idx, j in enumerate(li)] + [i-1, i+1], col + [i])

    global ans
    ans = 0
    for i in range(n):
        columns = [i]
        line = [i-1, i+1]
        search_queen(line, columns)
    return ans


# print(solution(4)) # 2
# print(solution(5)) # 10
print(solution(6)) # 4

