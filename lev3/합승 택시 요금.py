def solution(n, s, a, b, fares):
    def get_min_idx(rows, visited_list):
        idx = 0
        min_value = float('inf')
        for i, r in enumerate(rows):
            if not visited_list[i] and min_value > r:
                idx = i
                min_value = r
        return idx

    def dijkstra():
        maps = [[float("inf")] * n for _ in range(n)]
        for i in range(n):
            visited = [0] * n

            # 최초 노드 기준 다익스트라 배열 생성
            for node, fare in fare_dict[i+1]:
                maps[i][node-1] = fare
            visited[i] = 1

            # 모든 노드 탐색하면 최단거리 계산
            for _ in range(n-1):
                idx = get_min_idx(maps[i], visited) # 자기자신 다음 노드부터 가장 작은 값 탐색
                visited[idx] = 1
                if idx+1 in fare_dict:
                    for node, fare in fare_dict[idx+1]:
                        if maps[i][node-1] > maps[i][idx] + fare:
                            maps[i][node-1] = maps[i][idx] + fare
            maps[i][i] = 0
        return maps

    fare_dict = {k+1:[] for k in range(n)}
    for data in fares:
        start, end, fare = data
        fare_dict[start].append([end, fare])
        fare_dict[end].append([start, fare])

    dij_maps = dijkstra()
    ans = dij_maps[s-1][a-1] + dij_maps[s-1][b-1]
    for i in range(n):
        fare_way = dij_maps[s-1][i] + dij_maps[i][a-1] + dij_maps[i][b-1]
        if fare_way < ans:
            ans = fare_way
    return ans


"""
s->A, B까지 bfs로 탐색
다만, A,B 사이 교집합 간선을 어떻게 탐색?
2차원 다익스트라
 - 각 노드별 최단 거리 계산
 - min(s->a + s->b, s->i + i->a + i->b)
* 자기자신I 기준 왼쪽은 계산 필요X
    1   2   3   4   5   6   
1   0   63  41  10  24  25
2   63  0   22  66  46  48
3   41  22  0   51  24  26
4   10  66  51  0   24  35
5   24  46  24  34  0   2
6   25  48  26  35  2   0
"""

# print(solution(6,4,6,2,[[4,1,10], [3,5,24], [5,6,2], [3,1,41], [5,1,24], [4,6,50], [2,4,66], [2,3,22], [1,6,25]])) #82
# print(solution(7,3,4,1,[[5,7,9], [4,6,4], [3,6,1], [3,2,3], [2,1,6]])) #14
print(solution(6,4,5,6,[[2,6,6], [6,3,7], [4,6,7], [6,5,11], [2,5,12], [5,3,20], [2,4,8], [4,3,9]])) #18
