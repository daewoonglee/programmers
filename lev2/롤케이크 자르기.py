from collections import Counter, defaultdict


def solution(topping):
    # # 3.848447209
    # ans = 0
    # cnt_dic = Counter(topping)
    # piece1 = set()
    # piece2 = len(cnt_dic)
    # for t in topping[:-1]:
    #     piece1.add(t)
    #     cnt_dic[t] -= 1
    #     if cnt_dic[t] == 0:
    #         piece2 -= 1
    #     if len(piece1) == piece2: ans += 1
    # return ans

    # code refactoring - 0.7669939809999999
    cnt_dic = {}
    for i, top in enumerate(topping):
        if top in cnt_dic:
            cnt_dic[top][1] = i
        else:
            cnt_dic[top] = [i, i] # [first, last]

    db = sorted(sum(cnt_dic.values(), []))
    # print(f"Db: {db}, len: {len(db)}")
    # print(f"idx: {len(db)//2}, db[idx]: {db[len(db)//2]}, idx2: {len(db)//2-1}, db[idx2]: {db[len(db)//2-1]}")
    return db[len(db) // 2] - db[len(db) // 2 - 1]


print(solution([1, 2, 1, 3, 1, 4, 1, 2])) # 2
print(solution([1, 2, 3, 1, 4])) # 0
print(solution([1, 2, 3, 4])) # 1
print(solution([1])) # 0


if __name__ == "__main__":
    from timeit import Timer
    query = [
        [1, 2, 1, 3, 1, 4, 1, 2],
        [1, 2, 3, 1, 4],
        [1, 2, 3, 4],
        [1],
        [1]*1000,
        [1, 2, 1, 3, 1, 4, 1, 2] * 1000
    ]
    t = Timer(f"for t in {query}: solution(t)", "from __main__ import solution")
    print(t.timeit(number=1000))
