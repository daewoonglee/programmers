from collections import deque
def solution(n, wires):
    ad_mat = {}
    for wire in wires:
        if wire[0] not in ad_mat:
            ad_mat[wire[0]] = list()
        if wire[1] not in ad_mat:
            ad_mat[wire[1]] = list()
        ad_mat[wire[0]].append(wire[1])
        ad_mat[wire[1]].append(wire[0])
    
    visited_idx = {k: i for i, k in enumerate(set(sum(wires, [])))}
    ans = n
    for wire in wires:
        visited = [0 for _ in visited_idx]
        visited[visited_idx[wire[1]]] = 1
        
        cnt = 0
        bfs = deque([wire[0]])    
        while bfs:
            node = bfs.popleft()
            visited[visited_idx[node]] = 1
            cnt += 1
            for v in ad_mat[node]:
                if not visited[visited_idx[v]]:
                    bfs.append(v)
        diff = abs(n - cnt -cnt)
        if diff < ans:
            ans = diff
    return ans

#print(solution(9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]))
#print(solution(4, [[1,2],[2,3],[3,4]]))
#print(solution(7, [[1,2],[1,7],[2,3],[2,6],[3,4],[3,5]])) 
#print(solution(3, [[1,10],[10,100]]))

#print(solution(11, [[1,2],[1,5],[2,3],[3,4],[5,6],[6,7],[7,8],[8,9],[8,10],[8,11]]))
#print(solution(8, [[1,2],[1,7],[2,3],[2,6],[3,4],[3,5],[5,6]]))
print(solution(9, [[1,2],[2,3],[2,4],[4,5],[5,6],[6,7],[7,8],[7,9]]))

