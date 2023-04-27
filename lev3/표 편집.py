def solution(n, k, cmd):
    def move_table(m_val, m_num, i):
        # table을 벗어나는 경우의 인덱스 이동은 존재 X
        while m_val > 0:
            i += m_num
            if table[i] != 0:
                m_val -= 1
        return i

    def delete_table(m_num, i):
        while table[i] == 0:
            i += m_num
            if i < 0: return 0  # table 행이 모두 삭제된 경우
        return i

    table = [1] * n
    tail_n = n-1
    idx = k
    deleted_list = []
    for cmd_line in cmd:
        if len(cmd_line) == 1:
            if cmd_line == "C": #해당 행 삭제
                table[idx] = 0 #삭제
                deleted_list.append(idx)

                if idx != tail_n:
                    move_num = 1
                else: # idx==tail은 마지막 행, 마지막 행은 위 행으로 커서 이동
                    move_num = -1
                    tail_n -= 1
                idx = delete_table(move_num, idx+move_num)
            else: # Z
                # deleted_list가 empty인 상태에서 Z가 호출되는 경우는 X
                deleted_idx = deleted_list.pop()
                table[deleted_idx] = 1
                if deleted_idx > tail_n:
                    tail_n += 1
        else:
            move_cmd, move_val = cmd_line.split()
            # D: 위에서 아래로 이동 (idx+N), U: 아래에서 위로 이동 (idx-N)
            move_num = 1 if move_cmd == "D" else -1
            idx = move_table(int(move_val), move_num, idx)

    return "".join(["O" if t == 1 else "X" for t in table])


"""
delete, insert 과정이 있으면 효율성 문제 발생 여지 다분 (5<=n<=1,000,000, 1<=cmd<=200,000)

1. cmd 배열에 해당하는 table 배열 생성(1로 초기화)
2. table 배열 기준 삭제는 0, 추가는 1로 업데이트
3. U, D일 경우 idx+=1을하며 이동, 이 때 table이 0이라면 skip
4. z는 stack으로 삭제된 배열 인덱스 저장하여 z 호출 시 pop하면서 진행
5. table 배열 기준 1은 'O', 0은 'X'로 답 반환
"""


# print(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"])) #"OOOOXOOO"
# print(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"])) #"OOXOXOOO"
print(solution(5, 0, ["C","C","C","C","C"])) #XXXXX
print(solution(5, 4, ["C","C","C","C","C"])) #XXXXX

