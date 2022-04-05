def solution(rows, columns, queries):
    ans = []
    mat = [i for i in range(1, rows*columns+1)]
    for query in queries:
        x1, y1, x2, y2 = [q-1 for q in query]
        x, y = x1, y1
        pre = mat[x * columns + y]
        min_n = pre
        for _ in range((x2-x1+1)*2+(y2-y1-1)*2):
            if y != y1 and x == x2: y -= 1
            elif y == y2: x += 1
            elif x == x1: y += 1
            elif y == y1: x -= 1

            cur = x * columns + y
            temp = mat[cur]
            mat[cur] = pre
            pre = temp

            if min_n > pre: min_n = pre
        ans.append(min_n)
    return ans


print(solution(6, 6, [[2,2,5,4],[3,3,6,6],[5,1,6,3]]))
print(solution(3, 3, [[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]]))
print(solution(100, 97, [[1,1,100,97]]))

