def solution(food):
    # ans = ""
    # for i, f in enumerate(food[1:]):
    #     ans += f"{i+1}" * (f//2)
    # return ans + "0" + ans[::-1]

    ans = [str(i+1) * (f//2) for i, f in enumerate(food[1:])]
    return "".join(ans + ["0"] + ans[::-1])


print(solution([1,3,4,6]))
print(solution([1,7,1,2]))
