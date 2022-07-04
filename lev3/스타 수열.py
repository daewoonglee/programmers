def solution(a):
    ans = {0:0} # ans가 비었을 때 max 함수를 돌리기 위해 0으로 초기화
    for i in range(0, len(a)-1, 2):
        if a[i] == a[i+1]: continue
        for n in a[i:i+2]:
            if n not in ans: ans[n] = 2
            else: ans[n] += 2
    m = max([v for v in ans.values()])
    return m if m > 2 else 0


print(solution([0])) # 0
# print(solution([5,2,3,3,5,3])) # 4
# print(solution([0,3,3,0,7,2,0,2,2,0])) # 8
# print(solution([5,2,3,4,6,7,8,9,2,4,7,1,7,10])) # 6
print(solution([5,2,2,4,2,3,4,1,4,6,4,7])) # 8
print(solution([1,2,3,4,5,6,7,8,9,10])) # 0
