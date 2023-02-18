def solution(cards1, cards2, goal):
    N1 = len(cards1)
    N2 = len(cards2)
    i1 = i2 = 0
    for g in goal:
        if i1 < N1 and cards1[i1] == g:
            i1 += 1
        elif i2 < N2 and cards2[i2] == g:
            i2 += 1
        else:
            return "No"
    return "Yes"


"""
goal 배열 탐색하며 card1 or card2 단어와 배열이 동일한 지 비교
모두 소문자로만 구성되어 있다는 조건이 있기 때문에 대소문자 고려X
"""

print(solution(["i", "drink", "water"], ["want", "to"], ["i", "want", "to", "drink", "water"])) # Yes
print(solution(["i", "water", "drink"], ["want", "to"], ["i", "want", "to", "drink", "water"])) # No
