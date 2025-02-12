from collections import Counter


def solution(points, routes):
    def search_route():
        N, M = max(p[0] for p in points), max(p[1] for p in points)
        robot_routes = [[[] for _ in range(M)] for _ in range(N)]
        for route in routes:
            depth = 0
            start_x, start_y = points[route[0] - 1]
            robot_routes[(start_x - 1)][start_y - 1].append(depth)

            for i in range(len(route) - 1):
                start_x, start_y = points[route[i] - 1]
                end_x, end_y = points[route[i+1] - 1]

                dx = -1 if start_x > end_x else 1
                dy = -1 if start_y > end_y else 1

                while start_x != end_x:
                    depth += 1
                    start_x += dx
                    robot_routes[(start_x - 1)][start_y - 1].append(depth)
                while start_y != end_y:
                    depth += 1
                    start_y += dy
                    robot_routes[(start_x - 1)][start_y - 1].append(depth)
        return robot_routes

    # 최단 경로 탐색
    route_paths = search_route()

    # 충돌 횟수 탐색
    return sum([sum(1 for v in Counter(rp).values() if v > 1) for route_path in route_paths for rp in route_path if rp])


# print(solution([[3, 2], [6, 4], [4, 7], [1, 4]],[[4, 2], [1, 3], [2, 4]]))# 1
# print(solution([[3, 2], [6, 4], [4, 7], [1, 4]], [[4, 2], [1, 3], [4, 2], [4, 3]])) # 9
# print(solution([[2, 2], [2, 3], [2, 7], [6, 6], [5, 2]], [[2, 3, 4, 5], [1, 3, 4, 5]])) # 0
# print(solution([[1, 2], [2, 1]], [[1,2], [1,2]])) # 3
print(solution([[1, 1], [1, 3]], [[1, 2, 1, 2], [2, 1, 2, 1]])) # 3
