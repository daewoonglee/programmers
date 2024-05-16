def solution(bandage, health, attacks):
    attack_seq = [0] * (attacks[-1][0] + 1)
    for i, damage in attacks:
        attack_seq[i] = damage

    hp = health
    heal = 0
    for i in range(attacks[-1][0]+1):
        if attack_seq[i]:
            if hp - attack_seq[i] <= 0:
                return -1
            hp -= attack_seq[i]
            heal = 0
        else:
            heal += 1
            hp = hp+bandage[1] if hp+bandage[1] < health else health
            if heal == bandage[0]:
                hp = hp+bandage[-1] if hp+bandage[-1] < health else health
                heal = 0
    return hp


# print(solution([5, 1, 5], 30, [[2, 10], [9, 15], [10, 5], [11, 5]])) # 5
# print(solution([3, 2, 7], 20, [[1, 15], [5, 16], [8, 6]])) # -1
# print(solution([4, 2, 7], 20, [[1, 15], [5, 16], [8, 6]])) # -1
print(solution([1, 1, 1], 5, [[1, 2], [3, 2]])) # 3
