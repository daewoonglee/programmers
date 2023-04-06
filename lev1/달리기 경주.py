def solution(players, callings):
    # # 0.102966658
    # player_to_idx = dict()
    # idx_to_player = list()
    # for idx, player in enumerate(players):
    #     player_to_idx[player] = idx
    #     idx_to_player.append(player)
    #
    # for tracker in callings:
    #     idx = player_to_idx[tracker]
    #     lead_player = idx_to_player[idx-1]
    #     player_to_idx[lead_player], player_to_idx[tracker] = idx, idx - 1
    #     idx_to_player[idx], idx_to_player[idx - 1] = lead_player, tracker
    # return idx_to_player

    # 0.07918229900000001
    player_to_idx = {player: i for i, player in enumerate(players)}
    for tracker in callings:
        idx = player_to_idx[tracker]
        lead_player = players[idx-1]
        player_to_idx[lead_player], player_to_idx[tracker] = idx, idx-1
        players[idx-1], players[idx] = tracker, lead_player
    return players


print(solution(["mumu", "soe", "poe", "kai", "mine"], ["kai", "kai", "mine", "mine"])) #["mumu", "kai", "mine", "soe", "poe"]
print(solution(["aaa","bbb","ccc","ddd","eee"], ["eee","ddd","ccc","bbb"])) #["aaa","bbb","ccc","ddd","eee"]


if __name__ == "__main__":
    from timeit import Timer
    query = [
        [["mumu", "soe", "poe", "kai", "mine"], ["kai", "kai", "mine", "mine"]],
        [["aaa","bbb","ccc","ddd","eee"], ["eee","ddd","ccc","bbb"]],
        [["aaa","bbb","ccc","ddd","eee"], ["eee","eee","eee","eee","ddd","ddd","ddd","ddd","ccc","ccc","ccc","ccc","bbb","bbb","bbb","bbb"]],
        [["aaa","bbb","ccc","ddd","eee"], ["bbb","ccc"]]
    ]
    t = Timer(f"for t in {query}: solution(*t)", "from __main__ import solution")
    print(t.timeit(number=10000))
