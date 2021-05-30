"""
문제 설명
고속도로를 이동하는 모든 차량이 고속도로를 이용하면서 단속용 카메라를 한 번은 만나도록 카메라를 설치하려고 합니다.
고속도로를 이동하는 차량의 경로 routes가 매개변수로 주어질 때,
모든 차량이 한 번은 단속용 카메라를 만나도록 하려면 최소 몇 대의 카메라를 설치해야 하는지를 return 하도록 solution 함수를 완성하세요.

제한사항
차량의 대수는 1대 이상 10,000대 이하입니다.
routes에는 차량의 이동 경로가 포함되어 있으며 routes[i][0]에는 i번째 차량이 고속도로에 진입한 지점,
routes[i][1]에는 i번째 차량이 고속도로에서 나간 지점이 적혀 있습니다.
차량의 진입/진출 지점에 카메라가 설치되어 있어도 카메라를 만난것으로 간주합니다.
차량의 진입 지점, 진출 지점은 -30,000 이상 30,000 이하입니다.

입출력 예
routes	                                    return
[[-20,15], [-14,-5], [-18,-13], [-5,-3]]	2

입출력 예 설명
-5 지점에 카메라를 설치하면 두 번째, 네 번째 차량이 카메라를 만납니다.
-15 지점에 카메라를 설치하면 첫 번째, 세 번째 차량이 카메라를 만납니다.
"""


def solution(routes):
    # 0.068917424
    # routes.sort(key=lambda x: x[0])
    # start, end = routes[0]
    # ans = 1
    # for route in routes[1:]:
    #     if not start <= route[0] <= end:
    #         ans += 1
    #         start, end = route
    #     if start < route[0]:
    #         start = route[0]
    #     if end > route[1]:
    #         end = route[1]
    # return ans

    # code refactoring 01 - 0.05102672
    # routes.sort(key=lambda x: x[1])
    # ans = 1
    # end = routes[0][1]
    # for route in routes[1:]:
    #     if end < route[0]:
    #         ans += 1
    #         end = route[1]
    # return ans

    # code refactoring 02 - 0.05274352400000001
    routes.sort(key=lambda x: x[0], reverse=True)
    ans = 1
    end = routes[0][0]
    for route in routes[1:]:
        if end > route[1]:
            end = route[0]
        else:
            ans += 1
    return ans


# print(solution([[-20, 15], [-14, -5], [-18, -13], [-5, -3]]))   # 2
print(solution([[-20, -19], [-14, -5], [-18, -13], [-5, -3]]))  # 3
# print(solution([[-20, 15], [-14, -5], [-18, -13]]))             # 1
# print(solution([[-18, -14], [-14, -10], [-10, -5]]))            # 2


if __name__ == '__main__':
    from timeit import Timer
    query = [[[-20, 15], [-14, -5], [-18, -13], [-5, -3]],
             [[-20, -19], [-14, -5], [-18, -13], [-5, -3]],
             [[-20, 15], [-14, -5], [-18, -13]],
             [[-18, -14], [-14, -10], [-10, -5]]]
    t = Timer(f"for t in {query}: solution(t)", "from __main__ import solution")
    print(t.timeit(number=10000))
