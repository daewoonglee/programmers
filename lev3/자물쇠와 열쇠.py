def solution(key, lock):
    key = [r for k in key for r in k]
    lock = [r for l in lock for r in l]
    key_idx = [i for i, k in enumerate(key) if k]
    lock_idx = [i for i, l in enumerate(lock) if not l]
    N = len(key)
    print(f"key: {key}, lock: {lock}")
    print(f"idx, key: {key_idx}, lock: {lock_idx}")

    for rot in [0, 90, 180, 270]:
        rot_key = key
        visited = [0 for _ in range(len(key))]
        dfs = [key_idx[0]]
        while dfs:
            n = dfs.pop()
            if visited[n] == 1: continue
            visited[n] = 1


            rot_key_idx = [i for i, k in enumerate(rot_key) if k]
            if len(rot_key_idx) == len(lock_idx):
                for rki, li in zip(rot_key_idx, lock_idx):
                    if rki != li: break
                else:
                    return True

            if n-1 >= n%N: dfs.append(n-1)
            if n+1 < n%N+(N-1): dfs.append(n+1)
            if n-N >= 0: dfs.append(n-N)
            if n+N < N: dfs.append(n+N)
        break
    return False


print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))

# 풀이
# 키를 순차적으로 회전과 이동을 한다
#   0도 회전한 상태에서 "이동"하며 확인, 이를 90도 180도 270도에서 반복
#       > 이동은 어떻게 ? (상하좌우)
#       > 특정 열쇠 돌기를 기준으로 이동 할 수 있는 경우를 dfs로 진행, 모든 열쇠 돌기 반복
# 자물쇠와 부합되는지 확인
#   -> 자물쇠 홈 갯수와 열쇠 돌기 갯수가 안맞는지 확인
#       > 자물쇠 돌기와 키 돌기가 안 맞나는지
#       > 자물쇠 홈을 모두 채웠는 지
#   -> 되면 T, 안되면 회전과 이동 반복
#   -> 모든 루프를 다 돌면 부합되는 경우는 없다고 판단하여 F

# 조건
# 회전과 이동 가능
# 자물쇠 영역을 벗어난 부분의 열쇠는 영향을 주지 않음
# 자물쇠 영역 내에선 모든 홈 부분을 채워야함
# 자물쇠  돌기와 키 돌기 만나면 안됨

# 0 0 0  1 1 1
# 1 0 0  1 1 0
# 0 1 1  1 0 1
