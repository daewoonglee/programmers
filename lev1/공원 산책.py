def solution(park, routes):
    N, M = len(park), len(park[0])
    x, y = 0, 0
    for i, rows in enumerate(park):
        for j, r in enumerate(rows):
            if r.upper() == "S":
                x, y = i, j
                break

    move = {"E": (0, 1), "W": (0, -1), "S": (1, 0), "N": (-1, 0)}
    for route in routes:
        d, m = route.split()
        mx, my = list(map(lambda x: x * int(m), move[d]))
        # print(f"pts: {x}, {y}, mx: {mx}, {my}")
        if 0 <= x + mx < N and 0 <= y + my < M:
            nx, ny = x, y
            for _ in range(int(m)):
                nx += move[d][0]
                ny += move[d][1]
                if park[nx][ny] == "X":
                    break
            else:
                x, y = nx, ny
    return [x, y]


"""
시작 지점 탐색
routes를 돌며 이동 가능 여부 확인
    1. 주어진 맵을 벗어나는가 & 장애물이 있는가
최종 목적지 반환

OOO
OOO
OOO
OOS
"""

# print(solution(["SOO","OOO","OOO"], ["E 2","S 2","W 1"])) #[2,1]
# print(solution(["SOO","OXX","OOO"], ["E 2","S 2","W 1"])) #[0,1]
# print(solution(["OSO","OOO","OXO","OOO"], ["E 2","S 3","W 1"])) #[0,0]
print(solution(["OOO","OOO","OOO","OOS"], ["N 3"])) # [0,2]
print(solution(["OOO","OOO","OOX","OOS"], ["N 3"])) # [3,2]
