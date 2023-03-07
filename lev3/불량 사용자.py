from itertools import combinations, permutations


def solution(user_id, banned_id):
    def is_matched(val):
        for i, banned in enumerate(banned_id):
            if visited[i] or len(banned) != len(val):
                continue
            for b, v in zip(banned, val):
                if b != "*" and b != v:
                    break
            else:
                visited[i] = 1
                return True
        return False

    N = len(banned_id)
    permutation_list = permutations(user_id, N)
    ans = set()
    for values in permutation_list:
        visited = [0] * N
        for value in values:
            if not is_matched(value):
                break
        else:
            ans.add(tuple(sorted(list(values))))

    return len(ans)


"""
banned에 포함될 수 있는 경우의 수 계산
    이 때 확정 아이디 경우의 수와 중복 아이디 경우의 수 계산
"""

# print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"])) # 2
# print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"])) # 2
# print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"])) # 3
print(solution(["frodo", "fradi", "crodo", "abc456", "def456", "efg456","abc123", "frodoc"], ["*rodo", "*rodo", "***456", "******"])) # 9
# print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*****", "*****", "*****", "******", "******"])) # 1
# print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*****"])) # 3
print(solution(["frodo1", "fradi1", "crodo1", "abc123", "frodoc"], ["******", "******"])) # 10
