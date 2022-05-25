"""
1: 2 승
2: 5
3: 2
4: 3 2
mmmmmmmm
2: 1 3 4 패
3: 4
5: 2

승리 그래프
1  3 <- 4
 \ |  /
 > V <
   2 -> 5

패배 그래프
1  3 -> 4
 < X  >
 \ | /
   2 <- 5

자기를 바라보는 엣지 + 내가 바라보는 엣지의 합이 n이 되느냐?

자기 자신을 기준으로
    1. 자기를 바라보는 엣지가 있는가? (자기가 패배, 상대가 승리)
        나를 승리한 상대를 승리한 상대가 있는가?, 단 나를 이미 승리한 상대는 제외
    2. 내가 바라보는 엣지가 있는가? (자기가 승리, 상대가 패배)
        내가 승리한 상대에 대해서 상대가 패배한 상대가 있는가?, 단 내가 이미 승리한 상대는 제외
    1+2 관계의 합이 n이 되는 경우를 ans에 추
"""


def solution(n, results):
    def win_search(k, visited, res=0):
        res += 1
        visited[k-1] = 1
        if k in win:
            for node in win[k]:
                if visited[node-1]: continue
                res = win_search(node, visited, res)
        return res

    def loose_search(k, visited, res=0):
        res += 1
        visited[k-1] = 1
        if k in loose:
            for node in loose[k]:
                if visited[node-1]: continue
                res = loose_search(node, visited, res)
        return res
# 1 -> 2 -> 3, n=3
    win, loose = {}, {}
    for r in results:
        w, l = r
        if w not in win: win[w] = []
        if l not in loose: loose[l] = []
        win[w].append(l)
        loose[l].append(w)
    print(f"win: {win}")
    print(f"loose: {loose}")
    ans = 0
    for i in range(1, n+1):
        win_nodes, loose_nodes = 0, 0
        loose_nodes += loose_search(i, [0 for _ in range(n)])
        win_nodes += win_search(i, [0 for _ in range(n)])
        print(f"i: {i}, win: {win_nodes}, loose: {loose_nodes}")
        if win_nodes + loose_nodes == n+1: ans += 1
    return ans


# print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))
# print(solution(5, [[1, 2], [2, 3], [3, 4], [4, 5]]))
print(solution(6, [[1, 2], [2, 3], [3, 4], [4, 5], [4,6]]))
