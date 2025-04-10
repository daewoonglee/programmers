def solution(n, k, cmd):
    def move_idx(cnt, i):
        cnt, step = [cnt, 1] if cnt > 0 else [cnt*-1, -1]
        while cnt > 0: # table을 벗어나는 경우의 인덱스 이동은 존재 X
            i += step
            if logs[i]:
                cnt -= 1
        return i

    def del_row(i):
        logs[i] = 0
        delete_list.append(i)
        while i < n:
            if logs[i]: break
            i += 1
        else:
            while i > 0:
                i -= 1
                if logs[i]: break
        return i

    logs = [1] * n
    idx = k
    delete_list = []
    move_cnt = 0
    for cmd_line in cmd:
        if len(cmd_line) == 1:
            idx = move_idx(move_cnt, idx) # 명령어 실행 전 move 실행
            move_cnt = 0
            if cmd_line == "C":
                idx = del_row(idx)
            else: # delete_list가 null인 경우는 주어지지 않음
                del_idx = delete_list.pop()
                logs[del_idx] = 1
        else:
            c, m = cmd_line.split()
            move_cnt += int(m) if c == "D" else int(m)*-1 # 이동 값 누적하여 계산
    return "".join(["O" if l else "X" for l in logs])


# print(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"])) # OOOOXOOO
# print(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"])) # OOXOXOOO
# print(solution(5, 4, ["U 4", "C", "C", "C", "C", "C", "Z"])) # XXXXO
# print(solution(11, 0, ["D 10", "C"])) # OOOOOOOOOOX
print(solution(5, 2, ["C", "C", "U 1", "C"])) # OXXXO
