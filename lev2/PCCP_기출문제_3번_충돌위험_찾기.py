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

    robot_routes = []
    max_len, max_idx = 0, 0
    N, M = max([point[0] for point in points]), max([point[1] for point in points])
    route_idx = 0
    for route in routes:
        for i in range(len(route)-1):
            start, end = route[i], route[i+1]
            road_map = [[0] * M for _ in range(N)]
            start_x, start_y = points[start-1]
            end_x, end_y = points[end-1]
            queue = deque([[start_x-1, start_y-1, []]])
            r = bfs(queue, end_x-1, end_y-1)
            robot_routes.append(r)
            if len(r) > max_len:
                max_len = len(r)
                max_idx = route_idx
            route_idx += 1
            print(f"max_len: {max_len}, idx: {max_idx}, start: {start}, end: {end}, road: {r}")

    ans = 0
    for j, (robot_x, robot_y) in enumerate(robot_routes[max_idx]):
        check_x = [robot_x]
        check_y = [robot_y]
        print(f"max_idx: {max_idx}, check: {check_x}, {check_y}")
        flag = [False]
        for i in range(len(routes)):
            if i == max_idx or j >= len(robot_routes[i]): continue
            rx, ry = robot_routes[i][j]
            temp_x = []
            temp_y = []
            print(f"checkxy: {check_x}, {check_y}")
            for z, (cx, cy) in enumerate(zip(check_x, check_y)):
                print(f"checkxy: {check_x}, {check_y}, z: {z}, cx: {cx}, cy: {cy}, rx: {rx}, ry: {ry}")
                print(f"FLAG {rx not in check_x}, {ry not in check_y}")
                if cx == rx and cy == ry:
                    flag[z] = True
                elif rx not in check_x and ry not in check_y:
                    temp_x.append(rx)
                    temp_y.append(ry)
                    print(f"tempx: {temp_x}, y: {temp_y}")
            check_x.extend(temp_x)
            check_y.extend(temp_y)
            flag.extend([False]*len(temp_x))
            print("FIN")
        for f in flag:
            if f:
                ans += 1
        print(f"ans: {ans}\n")
    return ans


# print(solution([[3, 2], [6, 4], [4, 7], [1, 4]],[[4, 2], [1, 3], [2, 4]]))# 1
# print(solution([[3, 2], [6, 4], [4, 7], [1, 4]], [[4, 2], [1, 3], [4, 2], [4, 3]])) # 9
print(solution([[2, 2], [2, 3], [2, 7], [6, 6], [5, 2]], [[2, 3, 4, 5], [1, 3, 4, 5]])) # 0
