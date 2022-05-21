def solution(key, lock):
    def rotation(key_1d):
        rot_key = [0 for _ in key_1d]
        N = int(len(key_1d) ** 0.5)
        for i, k in enumerate(key_1d):
            if not k: continue
            q, d = i // N, i % N
            print(f"q: {q}, d: {d}, idx: {d*N+q if q != N-1 else d*N}")
            rot_key[d*N+N-1-q] = 1
        rot_key_idx = [i for i, k in enumerate(rot_key) if k]
        return rot_key, rot_key_idx

    lock_flat = [0 if r else 1 for l in lock for r in l]
    lock_home = lock_flat.count(1)
    key_flat = [r for k in key for r in k]
    key_idx = [i for i, k in enumerate(key_flat) if k]
    print(f"lock_flat: {lock_flat}")
    print(f"key_idx: {key_idx}")
    N = len(lock_flat)
    for _ in range(4):
        for n in key_idx:
            for i in range(N):
                move_key = [0 for _ in key_flat]
                diff = abs(i-n) if i <= n else i-n
                for j, k in enumerate(key_idx): # 수정 필요
                    if i <= n and k-diff >= 0: move_key[k-diff] = 1
                    elif k+diff < N: move_key[k+diff] = 1
                print(f"n: {n}, i: {i}, move: {move_key}, count: {move_key.count(1)}")
                if move_key.count(1) == lock_home:
                    for mk, l in zip(move_key, lock_flat):
                        if mk != l: break
                    else: return True
            print("==")
        key_flat, key_idx = rotation(key_flat)
        print(f"key_idx: {key_idx}")

    return False


# print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))
# print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 0, 0], [1, 1, 1], [1, 1, 1]]))
print(solution([[1, 1], [1, 0]], [[0, 0], [1, 1]]))

# 1 1
# 1 0

#   0    90     180     270
# 000   010     110     001
# 100   100     001     001
# 011   100     000     010

# 3 (1,0) = 1 (0,1)
# 7 (2,1) = 3 (1,2)
# 8 (2,2) = 6 (2,0)
#   (y,x) =   (x, N-1-y)

# 1 (0,1) = 5 (1,2)
# 3 (1,2) = 1 (1,0)
# 6 (2,0) = 0 (0,0)
