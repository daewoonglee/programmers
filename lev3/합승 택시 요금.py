import heapq


def solution(n, s, a, b, fares):
    def dijkstra(idx):
        h = []
        maps = [float("inf")] * n
        maps[idx] = 0
        # 처음 노드 기준 다익스트라 배열 생성
        for node, fare in fare_dict[idx]:
            maps[node] = fare
            heapq.heappush(h, (fare, node))

        # 모드 노드 탐색하면서 최단거리 계산
        while h:
            cur_fare, cur_node = heapq.heappop(h) # 가장 거리가 짧은 노드 선택
            for next_node, next_fare in fare_dict[cur_node]:
                if maps[next_node] > maps[cur_node] + next_fare:
                    maps[next_node] = maps[cur_node] + next_fare
                    heapq.heappush(h, (maps[next_node], next_node))
        # print(f"idx: {idx}, maps: {maps}")
        return maps

    fare_dict = {k:[] for k in range(n)}
    for data in fares:
        start, end, fare = data
        fare_dict[start-1].append([end-1, fare]) # 1~n시작을 0~n-1로 변환
        fare_dict[end-1].append([start-1, fare])

    # 0.49168040200000007
    dij_maps = [dijkstra(i) for i in range(n)]
    ans = dij_maps[s-1][a-1] + dij_maps[s-1][b-1]
    for i in range(n):
        fare_way = dij_maps[s-1][i] + dij_maps[i][a-1] + dij_maps[i][b-1]
        if fare_way < ans:
            ans = fare_way
    return ans


# print(solution(6,4,6,2,[[4,1,10], [3,5,24], [5,6,2], [3,1,41], [5,1,24], [4,6,50], [2,4,66], [2,3,22], [1,6,25]])) #82
# print(solution(7,3,4,1,[[5,7,9], [4,6,4], [3,6,1], [3,2,3], [2,1,6]])) #14
print(solution(6,4,5,6,[[2,6,6], [6,3,7], [4,6,7], [6,5,11], [2,5,12], [5,3,20], [2,4,8], [4,3,9]])) #18


if __name__ == "__main__":
    from timeit import Timer
    query = [
        [6,4,6,2,[[4,1,10], [3,5,24], [5,6,2], [3,1,41], [5,1,24], [4,6,50], [2,4,66], [2,3,22], [1,6,25]]],
        [7,3,4,1,[[5,7,9], [4,6,4], [3,6,1], [3,2,3], [2,1,6]]],
        [6,4,5,6,[[2,6,6], [6,3,7], [4,6,7], [6,5,11], [2,5,12], [5,3,20], [2,4,8], [4,3,9]]],
        [200,1,100,150,[[199,200,100],[2,6,6], [6,3,7], [4,6,7], [6,5,11], [2,5,12], [5,3,20], [20,40,8], [40,30,9],[50,70,9], [40,60,4], [30,60,1], [30,20,3], [20,10,6],[41,11,10], [31,51,24], [51,61,2], [31,11,41], [51,10,24], [41,60,50], [21,41,66], [21,31,22], [10,61,25],[1,100,100],[100,150,100],[100,10,1000]]]
    ]
    t = Timer(f"for t in {query}: solution(*t)", "from __main__ import solution")
    print(t.timeit(number=1000))
