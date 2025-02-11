def solution(points, routes):
    def search_route(start_x, start_y, end_x, end_y):
        road = [[start_x-1, start_y-1]]
        while start_x != end_x:
            if start_x > end_x:
                start_x -= 1
            else:
                start_x += 1
            road.append([start_x-1, start_y-1])
        while start_y != end_y:
            if start_y > end_y:
                start_y -= 1
            else:
                start_y += 1
            road.append([start_x-1, start_y-1])
        return road

    # 최단 경로 탐색
    robot_N = len(routes)
    robot_map = dict()
    robot_routes = [[] for _ in range(robot_N)]
    max_len = 0
    for i, route in enumerate(routes):
        for j in range(len(route)-1):
            start, end = route[j], route[j+1]
            robot_map_k = f"{start}_{end}"
            if robot_map_k not in robot_map:
                r = search_route(*points[start-1], *points[end-1])
                robot_map[robot_map_k] = r
            else:
                r = robot_map[robot_map_k]
            robot_routes[i].extend(r[1:] if robot_routes[i] else r)
        if len(robot_routes[i]) > max_len:
            max_len = len(robot_routes[i])
        print(f"max_len: {max_len}, road: {robot_routes[i]}")

    # 충돌 횟수 탐색
    ans = 0
    for j in range(max_len):
        check_xy, flag = [], [False]
        for i in range(robot_N):
            if j >= len(robot_routes[i]): continue
            # print(f"j: {j}, i: {i}, robot: {robot_routes[i][j]}, len: {len(robot_routes[i])}, check: {check_xy}")
            x, y = robot_routes[i][j]
            for z, (cx, cy) in enumerate(check_xy):
                if cx == x and cy == y:
                    flag[z] = True
                    break
            else:
                check_xy.append([x,y])
                flag.append(False)
        for f in flag:
            if f:
                ans += 1
    return ans


# print(solution([[3, 2], [6, 4], [4, 7], [1, 4]],[[4, 2], [1, 3], [2, 4]]))# 1
# print(solution([[3, 2], [6, 4], [4, 7], [1, 4]], [[4, 2], [1, 3], [4, 2], [4, 3]])) # 9
# print(solution([[2, 2], [2, 3], [2, 7], [6, 6], [5, 2]], [[2, 3, 4, 5], [1, 3, 4, 5]])) # 0
# print(solution([[1, 2], [2, 1]], [[1,2], [1,2]])) # 3
print(solution([[1, 1], [1, 3]], [[1, 2, 1, 2], [2, 1, 2, 1]])) # 3
