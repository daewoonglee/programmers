def solution(name, yearning, photo):
    # 2.4085621010000002
    name_yearn = dict(zip(name, yearning))
    ans = []
    for photo_names in photo:
        yearn = 0
        for photo_name in photo_names:
            if photo_name in name_yearn:
                yearn += name_yearn[photo_name]
        ans.append(yearn)
    return ans


print(solution(["may", "kein", "kain", "radi"], [5, 10, 1, 3], [["may", "kein", "kain", "radi"],["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]]))#[19, 15, 6]
print(solution(["kali", "mari", "don"], [11, 1, 55], [["kali", "mari", "don"], ["pony", "tom", "teddy"], ["con", "mona", "don"]])) #[67, 0, 55]
print(solution(["may", "kein", "kain", "radi"], [5, 10, 1, 3], [["may"],["kein", "deny", "may"], ["kon", "coni"]])) #[5, 15, 0]


if __name__ == "__main__":
    from timeit import Timer
    query = [
        [["may", "kein", "kain", "radi"], [5, 10, 1, 3], [["may", "kein", "kain", "radi"],["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]]],
        [["kali", "mari", "don"], [11, 1, 55], [["kali", "mari", "don"], ["pony", "tom", "teddy"], ["con", "mona", "don"]]],
        [["may", "kein", "kain", "radi"], [5, 10, 1, 3], [["may"],["kein", "deny", "may"], ["kon", "coni"]]],
        [[str(i) for i in range(100)], [i for i in range(100)], [str(i) for i in range(100)]*100],
        [[str(i) for i in range(100)], [i for i in range(100)], [str(i) for i in range(10)]*100]
    ]
    t = Timer(f"for t in {query}: solution(*t)", "from __main__ import solution")
    print(t.timeit(number=1000))
