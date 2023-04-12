import math


def solution(enroll, referral, seller, amount):
    def dfs(k):
        if k not in seller_graph:
            return []

        interests = []
        for name in seller_graph[k]:
            profit_interests = dfs(name)
            if name in seller_dict:
                profit_interests.extend(seller_dict[name])
            for pi in profit_interests:
                if pi >= 10:
                    interest = math.floor(pi*0.1)
                    pi -= interest
                    interests.append(interest)
                ans[name] += pi
        return interests

    seller_graph = {}
    for e, r in zip(enroll, referral):
        if r not in seller_graph:
            seller_graph[r] = list()
        seller_graph[r].append(e)

    # 중복된 seller 더하기
    seller_dict = dict()
    for k, v in zip(seller, amount):
        if k not in seller_dict:
            seller_dict[k] = []
        seller_dict[k].append(v*100)

    ans = {k: 0 for k in enroll}
    dfs("-")
    return list(ans.values())


"""
1. enroll <-> regerral 관계 그래프 형성
2. seller 중복된 경우 하나로 합산하여 계산
3. 각 seller마다 상위 노드로 올라가며 이익금 배분 10%
4. seller 순서로 각자가 벌어들인 이익금 반환

이익금 계산은 bottom to up 구조를 가짐, 맨 마지막 노드 위치를 탐색해야함
- -> john, mary
mary -> edward, emily, jaimie
edward -> sam, young
jaimie -> tod
"""

# print(solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],
#                ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],
#                ["young", "john", "tod", "emily", "mary"],
#                [12, 4, 2, 5, 10])) #[360, 958, 108, 0, 450, 18, 180, 1080]
# print(solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],
#                ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],
#                ["sam", "emily", "jaimie", "edward"],
#                [2, 3, 5, 4])) #[0, 110, 378, 180, 270, 450, 0, 0]
# print(solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young", "a"],
#                ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward", "tod"],
#                ["young", "a", "john", "a", "tod", "emily", "mary", "a"],
#                [12, 1, 4, 1, 2, 5, 10, 2])) #[360, 958, 108, 0, 450, 22, 216, 1080, 360]
# print(solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young", "a"],
#                ["-", "john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],
#                ["young", "a", "john", "a", "tod", "emily", "mary", "a"],
#                [12, 1, 4, 1, 2, 5, 10, 2]))
print(solution(["john", "mary", "emily", "tod", "edward"],
               ["-", "john", "john", "mary", "mary"],
               ["mary", "tod", "edward", "mary"],
               [1,1,1,1]))
