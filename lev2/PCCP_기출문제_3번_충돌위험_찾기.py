from collections import deque
import copy


def solution(points, routes):
    def bfs(q, ex, ey):
        road = []
        while q:
            mx, my, road = q.popleft()
            # print(f"mx: {mx}, my: {my}, road: {road}")
            if road_map[mx][my] == 1: continue
            road_map[mx][my] = 1
            road.append([mx, my])
            if mx == ex and my == ey: break
            for step_x, step_y in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                if 0 <= mx+step_x < N and 0 <= my+step_y < M:
                    q.append([mx+step_x, my+step_y, copy.deepcopy(road)])
        return road

    robot_N = len(routes)
    robot_routes = [[] for _ in range(robot_N)]
    print(robot_routes, len(routes))
    max_len, max_idx = 0, 0
    N, M = max([point[0] for point in points]), max([point[1] for point in points])
    for i, route in enumerate(routes):
        for j in range(len(route)-1):
            start, end = route[j], route[j+1]
            road_map = [[0] * M for _ in range(N)]
            start_x, start_y = points[start-1]
            end_x, end_y = points[end-1]
            queue = deque([[start_x-1, start_y-1, []]])
            r = bfs(queue, end_x-1, end_y-1)
            robot_routes[i].extend(r[1:] if robot_routes[i] else r)
        if len(robot_routes[i]) > max_len:
            max_len = len(robot_routes[i])
        print(f"max_len: {max_len}, road: {robot_routes[i]}")

    ans = 0
    for j in range(max_len):
        check_xy, flag = [], [False]
        for i in range(robot_N):
            if j >= len(robot_routes[i]): continue
            print(f"j: {j}, i: {i}, robot: {robot_routes[i][j]}, len: {len(robot_routes[i])}, check: {check_xy}")
            x, y = robot_routes[i][j]
            for z, (cx, cy) in enumerate(check_xy):
                if cx == x and cy == y:
                    flag[z] = True
                    break
            else:
                check_xy.append([x,y])
                flag.append(False)
        print(f"flag: {flag}")
        print(f"===")
        for f in flag:
            if f:
                ans += 1
    return ans


# print(solution([[3, 2], [6, 4], [4, 7], [1, 4]],[[4, 2], [1, 3], [2, 4]]))# 1
# print(solution([[3, 2], [6, 4], [4, 7], [1, 4]], [[4, 2], [1, 3], [4, 2], [4, 3]])) # 9
# print(solution([[2, 2], [2, 3], [2, 7], [6, 6], [5, 2]], [[2, 3, 4, 5], [1, 3, 4, 5]])) # 0
# print(solution([[1, 2], [2, 1]], [[1,2], [1,2]])) # 3
print(solution([[1, 1], [1, 3]], [[1, 2, 1, 2], [2, 1, 2, 1]])) # 3
