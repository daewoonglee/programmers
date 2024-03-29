from collections import deque
import itertools


def solution(rectangle, characterX, characterY, itemX, itemY):
    # # 1.403073206
    # N = 51 * 2 # 0.5 구간을 찾기 위해 2배 진행, 50은 문제에서 정의된 최대 크기
    # maps = [[0] * N for _ in range(N)]
    # visited = [[0] * N for _ in range(N)]
    # for r in rectangle:
    #     x1, y1, x2, y2 = r
    #     for i in range(x1*2, x2*2+1):
    #         for j in range(y1*2, y2*2+1):
    #             maps[i][j] = 1
    #
    # move = [[1,0], [-1,0], [0,1], [0,-1]]
    # isvalid = [[1,0], [-1,0], [0,1], [0,-1], [1,1], [-1,-1], [1,-1],[-1,1]]
    # itemX, itemY = itemX*2, itemY*2
    # q = deque([[characterX*2, characterY*2, 1]])
    # while q:
    #     x, y, dep = q.popleft()
    #     if visited[x][y]: continue
    #     visited[x][y] = 1
    #     if x == itemX and y == itemY:
    #         return dep // 2
    #     for m in move:
    #         nx, ny = x+m[0], y+m[1]
    #         if maps[nx][ny] == 1:
    #             for iv in isvalid:
    #                 if maps[nx+iv[0]][ny+iv[1]] == 0:
    #                     q.append([nx, ny, dep+1])
    #                     break
    # return -1

    # code refactoring - 0.862742066
    def is_movable():
        x, y = (cur_pos[0] + next_pos[0]) / 2, (cur_pos[1] + next_pos[1]) / 2
        is_on_any_border = any(
            (x in (x1, x2) and y1 <= y <= y2) or (y in (y1, y2) and x1 <= x <= x2)
            for x1, y1, x2, y2 in rectangle)
        is_inside_any_rect = any(
            x1 < x < x2 and y1 < y < y2 for x1, y1, x2, y2 in rectangle)
        return is_on_any_border and not is_inside_any_rect

    dist_to_item, perimeter = 0, 0
    cur_pos = (characterX, characterY)
    prev_pos = None
    # 시작 -> 종료, 종료 -> 시작 탐색하여 더 짧은 거리 반환 (직사각형 둘레 한바퀴 탐색)
    for dist in itertools.count():
        if cur_pos == (characterX, characterY) and prev_pos:
            perimeter = dist
            break
        elif cur_pos == (itemX, itemY):
            dist_to_item = dist
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            next_pos = (cur_pos[0] + dx, cur_pos[1] + dy)
            if next_pos != prev_pos and is_movable():
                prev_pos, cur_pos = cur_pos, next_pos
                break
    return min(dist_to_item, perimeter - dist_to_item)



"""
[문제 조건]
1 <= rectangle 세로 <= 4, [좌측 하단 x, 좌측 하단 y, 우측 상단 x, 우측 상단 y] 좌표 형태 구성
1 <= x, y <= 50
서로 다른 두 직사각형의 x축 좌표, 혹은 y축 좌표가 같은 경우 X, 직사각형만 입력으로 주어짐
1 <= charcterX, charcterY <= 50
1 <= itemX, itemY <= 50
캐릭터와 아이템의 처음 위치가 같은 경우는 없음
------------------------------------------------------
{(2,1), (7,5)}, {(6,4),(10,10)}가 주어진 경우
외각에 해당하는 좌표가 포함되어 있으면 이동할 수 있음, 외각에 포함된 좌표가 없는 경우 이동할 수 없음
중간에 겹치는 구간을 어떻게 잡을 지 고민 (외각에 포함된 좌표가 있는데 겹친 구간)
가면 안되는 이유는 두개의 직사각형이 겹친 구간이기 때문 -> 겹친 구간을 알아볼 수 있는 조건이 필요

[풀이 조건]
주어진 직사각형은 모두 겹치는 조건이 있음 50x50 map을 하나 만든 뒤 (0 초기화)
합집합으로 하나의 다각형을 찾음 -> 직사각형 탐색하면서 1
이후 출발 위치부터 다각형을 탐색하면서 0과 1이 맞닿은 부분으로만 이동(테두리) 
출발지점부터 목표지점을 찾지 못한다는 가정이 없으니 찾을 때까지 루프 탐색
"""


# print(solution([[2,1,3,4],[1,2,4,3]], 1, 2, 4, 3)) # 6
# print(solution([[1,1,5,7]], 1, 1, 4, 7)) # 9
# print(solution([[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]], 1, 3, 7, 8)) # 17
# print(solution([[1,1,8,4],[2,2,4,9],[3,6,9,8],[6,3,7,7]], 9, 7, 6, 1)) # 11
# print(solution([[2,1,7,5],[6,4,10,10]], 3, 1, 7, 10)) # 15
print(solution([[2,2,5,5],[1,3,6,4],[3,1,4,6]], 1, 4, 6, 3)) # 10
print(solution([[2, 1, 3, 6], [4, 1, 5, 6], [1, 2, 6, 3], [1, 4, 6, 5]], 3, 2, 5, 4)) # 8


if __name__ == "__main__":
    from timeit import Timer
    query = [
        [[[2,1,3,4],[1,2,4,3]], 1, 2, 4, 3],
        [[[1,1,5,7]], 1, 1, 4, 7],
        [[[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]], 1, 3, 7, 8],
        [[[1,1,8,4],[2,2,4,9],[3,6,9,8],[6,3,7,7]], 9, 7, 6, 1],
        [[[2,1,7,5],[6,4,10,10]], 3, 1, 7, 10],
        [[[2,2,5,5],[1,3,6,4],[3,1,4,6]], 1, 4, 6, 3],
        [[[2, 1, 3, 6], [4, 1, 5, 6], [1, 2, 6, 3], [1, 4, 6, 5]], 3, 2, 5, 4]
    ]
    t = Timer(f"for t in {query}: solution(*t)", "from __main__ import solution")
    print(t.timeit(number=1000))
