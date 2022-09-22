def solution(n):
    ans = []

    def hanoi(s, e, i, n):
        if n == 1:
            ans.append([s,e])
            return

        hanoi(s,i,e,n-1)
        ans.append([s,e])
        hanoi(i,e,s,n-1)

    hanoi(1,3,2,n)

    return ans


print(solution(2))
print(solution(3))
