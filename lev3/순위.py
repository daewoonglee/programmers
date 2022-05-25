def solution(n, results):
    def win_search(k, visited, res=0):
        res += 1
        visited[k-1] = 1
        if k in win:
            for node in win[k]:
                if visited[node-1]: continue
                res = win_search(node, visited, res)
        return res

    def loose_search(k, visited, res=0):
        res += 1
        visited[k-1] = 1
        if k in loose:
            for node in loose[k]:
                if visited[node-1]: continue
                res = loose_search(node, visited, res)
        return res

    # 0.8407392800000001
    # win, loose = {}, {}
    # for r in results:
    #     w, l = r
    #     if w not in win: win[w] = []
    #     if l not in loose: loose[l] = []
    #     win[w].append(l)
    #     loose[l].append(w)
    #
    # ans = 0
    # for i in range(1, n+1):
    #     win_nodes, loose_nodes = 0, 0
    #     loose_nodes += loose_search(i, [0 for _ in range(n)])
    #     win_nodes += win_search(i, [0 for _ in range(n)])
    #     if win_nodes + loose_nodes == n+1: ans += 1
    # return ans

    # code refactoring - 0.483563335
    from collections import defaultdict
    win, loose = defaultdict(set), defaultdict(set)
    for r in results:
        win[r[0]].add(r[1])
        loose[r[1]].add(r[0])
    for i in range(1, n+1):
        for looser in win[i]: loose[looser].update(loose[i])
        for winner in loose[i]: win[winner].update(win[i])
    return sum([1 for i in range(1, n+1) if len(loose[i]) + len(win[i]) == n-1])


print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))    # 2
print(solution(5, [[1, 2], [2, 3], [3, 4], [4, 5]]))            # 5
print(solution(6, [[1, 2], [2, 3], [3, 4], [4, 5], [4,6]]))     # 4

if __name__ == "__main__":
    from timeit import Timer
    query = [[5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]],
             [5, [[1, 2], [2, 3], [3, 4], [4, 5]]],
             [6, [[1, 2], [2, 3], [3, 4], [4, 5], [4,6]]],
             [5, [[1, 2], [1, 3], [1, 4], [1, 5], [2, 3], [2, 4], [2, 5], [3, 4], [3, 5], [4, 5]]]]
    t = Timer(f"for t in {query}: solution(*t)", "from __main__ import solution")
    print(t.timeit(number=10000))
