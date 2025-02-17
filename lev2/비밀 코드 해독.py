from itertools import combinations


def solution(n, q, ans):
    code_digit = set(range(1, n+1))
    for query, collect in zip(q, ans):
        if collect == 0:
            code_digit -= set(query)

    secret_code = 0
    for comb_digit in combinations(code_digit, 5):
        for query, collect in zip(q, ans):
            if len(set(query) & set(comb_digit)) != collect: break
        else: secret_code += 1
    return secret_code


# print(solution(10, [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [3, 7, 8, 9, 10], [2, 5, 7, 9, 10], [3, 4, 5, 6, 7]], [2, 3, 4, 3, 3])) # 3
print(solution(15, [[2, 3, 9, 12, 13], [1, 4, 6, 7, 9], [1, 2, 8, 10, 12], [6, 7, 11, 13, 15], [1, 4, 10, 11, 14]], [2, 1, 3, 0, 1])) # 5
