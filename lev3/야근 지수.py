import heapq
def solution(n, works):
    if sum(works) <= n: return 0
    works = [-w for w in works]
    heapq.heapify(works)
    for _ in range(n):
        heapq.heappush(works, heapq.heappop(works)+1)
    return sum([(w*w) for w in works])


# print(solution(4,[4,3,3])) # 12
# print(solution(1,[2,1,2])) # 6
# print(solution(3,[1,1]))   # 0
# print(solution(7,[10,9,3,3,3])) # 99
# print(solution(99,[2,15,22,55,55])) # 580
print(solution(2,[8])) # 580

