def solution(points, routes):
    def search_route(route):
        global max_len, robot_map
        road = []
        for i in range(len(route)-1):
            robot_map_k = f"{route[i]}_{route[i+1]}"
            temp_road = [points[route[i]-1]]
            if robot_map_k not in robot_map:
                start_x, start_y = points[route[i]-1]
                end_x, end_y = points[route[i+1]-1]

                dx = -1 if start_x > end_x else 1
                dy = -1 if start_y > end_y else 1

                while start_x != end_x:
                    start_x += dx
                    temp_road.append([start_x, start_y])

                while start_y != end_y:
                    start_y += dy
                    temp_road.append([start_x, start_y])
                robot_map[robot_map_k] = temp_road

            road.extend(robot_map[robot_map_k][1:] if road else robot_map[robot_map_k])
            if max_len < len(road):
                max_len = len(road)
        return road

    global max_len, robot_map
    # 최단 경로 탐색
    robot_map = dict()
    max_len = 0
    robot_routes = [search_route(r) for r in routes]

    # 충돌 횟수 탐색
    ans = 0
    for j in range(max_len):
        check_xy, flag = [], [False]
        for i in range(len(routes)):
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
        ans += sum(flag)
    return ans


# print(solution([[3, 2], [6, 4], [4, 7], [1, 4]],[[4, 2], [1, 3], [2, 4]]))# 1
# print(solution([[3, 2], [6, 4], [4, 7], [1, 4]], [[4, 2], [1, 3], [4, 2], [4, 3]])) # 9
# print(solution([[2, 2], [2, 3], [2, 7], [6, 6], [5, 2]], [[2, 3, 4, 5], [1, 3, 4, 5]])) # 0
# print(solution([[1, 2], [2, 1]], [[1,2], [1,2]])) # 3
print(solution([[1, 1], [1, 3]], [[1, 2, 1, 2], [2, 1, 2, 1]])) # 3
