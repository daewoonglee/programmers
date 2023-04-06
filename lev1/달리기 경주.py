def solution(players, callings):
    player_to_idx = dict()
    idx_to_player = dict()
    for idx, player in enumerate(players):
        player_to_idx[player] = idx
        idx_to_player[idx] = player

    for calling_player in callings:
        idx = player_to_idx[calling_player]
        lead_player = idx_to_player[idx-1]
        player_to_idx[lead_player] = idx
        player_to_idx[calling_player] = idx - 1
        idx_to_player[idx] = lead_player
        idx_to_player[idx - 1] = calling_player

    return list(idx_to_player.values())


"""
callings에 있는 명칭이 있을 때 players 인덱스 -1, 1등은 불리지 않음 (조건 고려X)

player_to_idx={player: idx}
idx_to_player={idx: player}
for callings 돌면서
    idx = player_to_idx[calling_player]
    lead_player = idx_to_player[idx-1]
    player_to_idx[lead_player] = idx # 선두 idx:이름 update
    player_to_idx[calling_player] = idx-1 # 후발 idx:이름 update
    idx_to_player[idx] = lead_player # 선두 이름:idx update
    idx_to_player[idx-1] = calling_player # 후발 이름:idx update
"""


print(solution(["mumu", "soe", "poe", "kai", "mine"], ["kai", "kai", "mine", "mine"])) #["mumu", "kai", "mine", "soe", "poe"]
print(solution(["aaa","bbb","ccc","ddd","eee"], ["eee","ddd","ccc","bbb"])) #["aaa","bbb","ccc","ddd","eee"]
