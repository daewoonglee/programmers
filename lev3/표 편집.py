def solution(n, k, cmd):
    def move_idx(cnt, i):
        cnt, step = [cnt, 1] if cnt > 0 else [cnt*-1, 0]
        for _ in range(cnt):
            i = node_data[i][step]
        return i

    def del_row(i):
        logs[i] = 0
        delete_list.append(i)

    def update_node(i):
        if i-1 >= 0 and node_data[i][0] is not None:
            node_data[node_data[i][0]][1] = node_data[i][1]
        if i+1 < n and node_data[i][1] is not None:
            node_data[node_data[i][1]][0] = node_data[i][0]
        return node_data[i][1] if node_data[i][1] else node_data[i][0]

    logs = [1] * n
    idx = k
    delete_list = []
    node_data = [[i-1,i+1] for i in range(n)]
    node_data[0][0] = None
    node_data[-1][1] = None
    move_cnt = 0
    for cmd_line in cmd:
        if len(cmd_line) == 1:
            idx = move_idx(move_cnt, idx) # 명령어 실행 전 index move
            print(f"MOVE: {idx}, CMD: {cmd_line}, move cnt: {move_cnt}")
            move_cnt = 0
            if cmd_line == "C":
                print(f"cmd: {cmd_line}, idx: {idx}, node: {node_data}")
                del_row(idx)
                idx = update_node(idx)
                print(f"cmd: {cmd_line}, idx: {idx}, node: {node_data}\n")
            else: # delete_list가 null인 경우는 주어지지 않음
                del_idx = delete_list.pop()
                logs[del_idx] = 1
                _ = update_node(del_idx)
                if idx is None:
                    idx = del_idx
        else:
            c, m = cmd_line.split()
            move_cnt += int(m) if c == "D" else int(m)*-1 # 이동 값 누적하여 계산
    return "".join(["O" if l else "X" for l in logs])


# print(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"])) # OOOOXOOO
# print(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"])) # OOXOXOOO
# print(solution(5, 4, ["U 4", "C", "C", "C", "C", "C", "Z"])) # XXXXO
# print(solution(11, 0, ["D 10", "C"])) # OOOOOOOOOOX
# print(solution(5, 2, ["C", "C", "U 1", "C"])) # OXXXO
print(solution(5, 2, ["C", "C", "C", "C", "C", "Z", "Z", "C"])) # XOXXX
