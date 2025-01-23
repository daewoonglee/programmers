import datetime


def solution(video_len, pos, op_start, op_end, commands):
    vid_start = datetime.datetime.strptime("1900-01-01 00:00:00", '%Y-%m-%d %H:%M:%S')
    video_len, pose, op_start, op_end = [datetime.datetime.strptime(t, "%M:%S") for t in [video_len, pos, op_start, op_end]]

    for command in commands:
        if op_start <= pose <= op_end:
            pose = op_end
        pose += datetime.timedelta(seconds=10) * (-1 if command.startswith("p") else 1)
        if pose <= vid_start:
            pose = vid_start
        elif pose >= video_len:
            pose = video_len

    if op_start <= pose <= op_end:
        pose = op_end
    return pose.strftime("%M:%S")


# print(solution("34:33","13:00","00:55","02:55",["next", "prev"])) #	"13:00"
# print(solution("10:55","00:05","00:15","06:55",["prev", "next", "next"])) #	"06:55"
# print(solution("07:22","04:05","00:15","04:07", ["next"])) #	"04:17"
print(solution("07:22", "00:05", "00:15", "04:07", ["next", "next"]))