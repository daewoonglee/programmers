def defence(n, k, enemy, rnd):
    if n < 0:
        # print(f"BREAK !!! n < 0, n: {n}, k: {k}, enemy: {enemy}, rnd: {rnd}\n")
        return rnd-1
    elif rnd >= len(enemy):
        return rnd

    # print(f"n: {n}, k: {k}, enemy: {enemy}, rnd: {rnd}")
    return max(defence(n-enemy[rnd], k, enemy, rnd + 1), defence(n, k-1, enemy, rnd+1) if k > 0 else rnd)


def solution(n, k, enemy):
    game_round = 0
    return max(defence(n-enemy[game_round], k, enemy, game_round+1), defence(n, k-1, enemy, game_round+1))


print(solution(7, 3, [4, 2, 4, 5, 3, 3, 1])) # 5
print(solution(7, 3, [4, 4, 4, 5, 2, 1, 1])) # 6
print(solution(7, 3, [2, 4, 3, 3, 5, 4, 3])) # 5
print(solution(7, 3, [4, 2, 3, 2, 5, 3, 6])) # 6
print(solution(2, 4, [3, 3, 3, 3])) # 4
