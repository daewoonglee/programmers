def solution(park, routes):
    # 0.30875342100000003
    N, M = len(park), len(park[0])
    x, y = 0, 0
    for i, rows in enumerate(park):
        for j, r in enumerate(rows):
            if r == "S":
                x, y = i, j
                break

    direction = {"E": (0, 1), "W": (0, -1), "S": (1, 0), "N": (-1, 0)}
    for route in routes:
        d, m = route.split()
        dx, dy = direction[d]
        mx, my = x + dx * int(m), y + dy * int(m)
        if 0 <= mx < N and 0 <= my < M:
            nx, ny = x, y
            for _ in range(int(m)):
                nx += dx
                ny += dy
                if park[nx][ny] == "X":
                    break
            else:
                x, y = nx, ny
    return [x, y]


print(solution(["SOO","OOO","OOO"], ["E 2","S 2","W 1"])) #[2,1]
print(solution(["SOO","OXX","OOO"], ["E 2","S 2","W 1"])) #[0,1]
print(solution(["OSO","OOO","OXO","OOO"], ["E 2","S 3","W 1"])) #[0,0]
print(solution(["OOO","OOO","OOO","OOS"], ["N 3"])) # [0,2]
print(solution(["OOO","OOO","OOX","OOS"], ["N 3"])) # [3,2]
print(solution(["OOO","SXO","OOO","OOO"], ["E 2"])) # [1,0]


if __name__ == "__main__":
    from timeit import Timer
    query = [
        [["SOO","OOO","OOO"], ["E 2","S 2","W 1"]],
        [["SOO","OXX","OOO"], ["E 2","S 2","W 1"]],
        [["OSO","OOO","OXO","OOO"], ["E 2","S 3","W 1"]],
        [["OOO","OOO","OOO","OOS"], ["N 3"]],
        [["OOO","OOO","OOX","OOS"], ["N 3"]],
        [["OOOOOOOO","OOOOOOOO","OOOOOOOO","OOOOOOOO","OOOOOOOO","OOOOOOOS"],["N 3","E 2","S 2","W 1","N 1","N 5","S 3"]]
    ]
    t = Timer(f"for t in {query}: solution(*t)", "from __main__ import solution")
    print(t.timeit(number=10000))
