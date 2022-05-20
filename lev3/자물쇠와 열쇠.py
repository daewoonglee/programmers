def solution(key, lock):
    key = [r for k in key for r in k]
    lock = [0 if r else 1 for l in lock for r in l]
    key_idx = [i for i, k in enumerate(key) if k]
    lock_idx = [i for i, l in enumerate(lock) if l]
    N = len(key)
    print(f"key: {key}, lock: {lock}")
    print(f"idx, key: {key_idx}, lock: {lock_idx}")

    for rot in [0, 90, 180, 270]: # 해당 부분 수정 필요
        # rot_key = key
        for n in key_idx:
            for i in range(N): # 특정 n에 대한 n x n 매트릭스 전체 탐
                move_key = [0 for _ in key]
                diff = abs(i-n) if i <= n else i-n
                for j, k in enumerate(key_idx):
                    if i <= n and k-diff >= 0: move_key[k-diff] = 1
                    elif k+diff < N: move_key[k+diff] = 1
                # if n == 7:
                #     print(f"i: {i}, move: {move_key}, count: {move_key.count(1)}, len: {len(lock_idx)}")
                if move_key.count(1) == len(lock_idx):
                    for mk, l in zip(move_key, lock):
                        # print(f"mk: {mk}, l: {l}")
                        if mk != l: break
                    else: return True
            print(f"n: {n}")
        break
    return False

print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 0, 0], [1, 1, 1], [1, 1, 1]]))
# print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))

# 0 0 0  1 0 0
# 1 0 0  1 1 1
# 0 1 1  1 1 1


# 0 0 0  1 1 1
# 1 0 0  1 1 0
# 0 1 1  1 0 1
