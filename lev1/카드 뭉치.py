def solution(cards1, cards2, goal):
    N1 = len(cards1)
    N2 = len(cards2)
    i1 = i2 = 0

    # 0.04525750099999999
    for g in goal:
        if i1 < N1 and cards1[i1] == g:
            i1 += 1
        elif i2 < N2 and cards2[i2] == g:
            i2 += 1
        else:
            return "No"
    return "Yes"

    # i1 + 1 < N1 or i2 + 1 < N2는 틀린 조건문, 문제 만족하지 못함
    # i1 + 1 <= N1 and i2 + 1 <= N2가 맞으며 이렇게 되면 속도가 오히려 느림
    # for g in goal:
    #     if cards1[i1] == g and i1 + 1 < N1:
    #         i1 += 1
    #     elif cards2[i2] == g and i2 + 1 < N2:
    #         i2 += 1
    #     else:
    #         return "No"
    # return "Yes"


# print(solution(["i", "drink", "water"], ["want", "to"], ["i", "want", "to", "drink", "water"])) # Yes
# print(solution(["i", "water", "drink"], ["want", "to"], ["i", "want", "to", "drink", "water"])) # No
# print(solution(["i1"], ["i2"], ["i1", "i2", "i3"])) # No
print(solution(["i1", "i2"], ["i3", "i4"], ["i1", "i2"])) # No


if __name__ == "__main__":
    from timeit import Timer
    query = [
        [["i", "drink", "water"], ["want", "to"], ["i", "want", "to", "drink", "water"]],
        [["i", "water", "drink"], ["want", "to"], ["i", "want", "to", "drink", "water"]],
        [["i1"], ["i2"], ["i1", "i2", "i3"]],
        [["i1", "i2"], ["i3", "i4"], ["i1", "i2"]],
        [[f"i{i}" for i in range(1, 11)], [f"j{i}" for i in range(1, 11)], [[f"i{i}" for i in range(1, 11)], [f"j{i}" for i in range(1, 11)]]],
    ]
    t = Timer(f"for t in {query}: solution(*t)", "from __main__ import solution")
    print(t.timeit(number=10000))
