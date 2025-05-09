def solution(video_len, pos, op_start, op_end, commands):
    def time_to_sec(txt):
        h, m = txt.split(":")
        return int(h) * 60 + int(m)

    def sec_to_time(s):
        h, m = s // 60, s % 60
        return f"{h:02d}:{m:02d}"

    vid_start = 0
    vid_end, pos, op_start, op_end = [time_to_sec(t) for t in [video_len, pos, op_start, op_end]]
    for command in commands:
        if op_start <= pos <= op_end:
            pos = op_end
        pos = (pos-10 if pos-10 > vid_start else vid_start) if command.startswith("p") else (pos+10 if pos+10 < vid_end else vid_end)

    if op_start <= pos <= op_end:
        pos = op_end
    return sec_to_time(pos)


# print(solution("34:33","13:00","00:55","02:55",["next", "prev"])) #	"13:00"
# print(solution("10:55","00:05","00:15","06:55",["prev", "next", "next"])) #	"06:55"
# print(solution("07:22","04:05","00:15","04:07", ["next"])) #	"04:17"
print(solution("07:22", "00:05", "00:15", "04:07", ["next", "next"]))