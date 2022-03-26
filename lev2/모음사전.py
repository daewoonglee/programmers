from itertools import product


def solution(word):
    # 51.662038234993815
    #return sorted([''.join(w) for w in sum([list(product("AEIOU", repeat=i)) for i in range(1, 6)], [])]).index(word)+1

    # 0.1288360711187124
    ans = 0
    for i, n in enumerate(word):
        ans += (5 ** (5 - i) - 1) / (5 - 1) * "AEIOU".index(n) + 1
    return ans


#print(solution("A"))
#print(solution("AAAE"))
#print(solution("I"))
#print(solution("EIO"))
print(solution("AAE"))
print(solution("UUUUU"))


if __name__ == "__main__":
    from timeit import Timer
    query = ["A", "AAAE", "I", "EIO", "AAE", "U", "IUUUU", "UUUUU"]
    t = Timer(f"for t in {query}: solution(t)", "from __main__ import solution")
    print(t.timeit(number=10000))

