from itertools import product


def solution(word):
    return sorted([''.join(w) for w in sum([list(product("AEIOU", repeat=i)) for i in range(1, 6)], [])]).index(word)+1


print(solution("A"))
print(solution("AAAE"))
print(solution("I"))
print(solution("EIO"))

