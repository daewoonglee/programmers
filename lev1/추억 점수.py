def solution(name, yearning, photo):
    name_yeaarn = {n: y for n, y in zip(name, yearning)}
    ans = []
    for photo_names in photo:
        yearn = 0
        for photo_name in photo_names:
            if photo_name in name_yeaarn:
                yearn += name_yeaarn[photo_name]
        ans.append(yearn)
    return ans


# print(solution(["may", "kein", "kain", "radi"], [5, 10, 1, 3], [["may", "kein", "kain", "radi"],["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]]))#[19, 15, 6]
print(solution(["kali", "mari", "don"], [11, 1, 55], [["kali", "mari", "don"], ["pony", "tom", "teddy"], ["con", "mona", "don"]])) #[67, 0, 55]
print(solution(["may", "kein", "kain", "radi"], [5, 10, 1, 3], [["may"],["kein", "deny", "may"], ["kon", "coni"]])) #[5, 15, 0]
