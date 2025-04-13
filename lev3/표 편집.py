def solution(n, k, cmd):
    def move_idx(cnt, i):
        cnt, step = [cnt, 1] if cnt > 0 else [cnt*-1, 0]
        for _ in range(cnt):
            i = node_data[i][step]
        return i

    def update_node(i, c):
        prev_node, next_node = node_data[i]
        if prev_node is not None:
            node_data[prev_node][1] = next_node if c == "C" else i
        if next_node is not None:
            node_data[next_node][0] = prev_node if c == "C" else i
        return next_node if next_node else prev_node

    def del_row(i):
        logs[i] = 0
        delete_list.append(i)
        return update_node(i, "C")

    def restore_row(i):
        logs[i] = 1
        update_node(i, "Z")

    logs = [1] * n
    idx = k
    delete_list = []
    node_data = [[i-1,i+1] for i in range(n)]
    node_data[0][0] = None
    node_data[-1][1] = None
    move_cnt = 0
    for cmd_line in cmd:
        if len(cmd_line) == 1:
            idx = move_idx(move_cnt, idx) # 명령어 실행 전 index move & 표의 범위를 벗어난 이동은 입력으로 주어지지 않음
            move_cnt = 0
            if cmd_line == "C": # 표의 모든 행을 제거하여, 행이 하나도 남지 않는 경우는 입력으로 주어지지 않음
                idx = del_row(idx)
            else: # delete_list가 null인 경우는 주어지지 않음
                restore_row(delete_list.pop())
        else:
            c, m = cmd_line.split()
            move_cnt += int(m) if c == "D" else int(m)*-1 # 이동 값 누적하여 계산
    return "".join(["O" if l else "X" for l in logs])


print(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"])) # OOOOXOOO
# print(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"])) # OOXOXOOO
# print(solution(5, 4, ["U 4", "C", "C", "C", "C", "C", "Z"])) # XXXXO
# print(solution(11, 0, ["D 10", "C"])) # OOOOOOOOOOX
# print(solution(5, 2, ["C", "C", "U 1", "C"])) # OXXXO
# print(solution(5, 2, ["C", "C", "C", "C", "C", "Z", "Z", "C"])) # XOXXX
# print(solution(5, 4, ["C", "Z", "U 2", "C", "C", "U 1", "C", "Z", "U 1", "C"])) # XXOOO