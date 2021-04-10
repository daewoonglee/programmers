"""
문제 설명
방금그곡
라디오를 자주 듣는 네오는 라디오에서 방금 나왔던 음악이 무슨 음악인지 궁금해질 때가 많다.
그럴 때 네오는 다음 포털의 '방금그곡' 서비스를 이용하곤 한다. 방금그곡에서는 TV, 라디오 등에서 나온 음악에 관해 제목 등의 정보를 제공하는 서비스이다.

네오는 자신이 기억한 멜로디를 가지고 방금그곡을 이용해 음악을 찾는다.
그런데 라디오 방송에서는 한 음악을 반복해서 재생할 때도 있어서 네오가 기억하고 있는 멜로디는 음악 끝부분과 처음 부분이 이어서 재생된 멜로디일 수도 있다.
반대로, 한 음악을 중간에 끊을 경우 원본 음악에는 네오가 기억한 멜로디가 들어있다 해도 그 곡이 네오가 들은 곡이 아닐 수도 있다.
그렇기 때문에 네오는 기억한 멜로디를 재생 시간과 제공된 악보를 직접 보면서 비교하려고 한다.

다음과 같은 가정을 할 때 네오가 찾으려는 음악의 제목을 구하여라.

방금그곡 서비스에서는 음악 제목, 재생이 시작되고 끝난 시각, 악보를 제공한다.
네오가 기억한 멜로디와 악보에 사용되는 음은 C, C#, D, D#, E, F, F#, G, G#, A, A#, B 12개이다.
각 음은 1분에 1개씩 재생된다. 음악은 반드시 처음부터 재생되며 음악 길이보다 재생된 시간이 길 때는 음악이 끊김 없이 처음부터 반복해서 재생된다.
음악 길이보다 재생된 시간이 짧을 때는 처음부터 재생 시간만큼만 재생된다.
음악이 00:00를 넘겨서까지 재생되는 일은 없다.
조건이 일치하는 음악이 여러 개일 때에는 라디오에서 재생된 시간이 제일 긴 음악 제목을 반환한다. 재생된 시간도 같을 경우 먼저 입력된 음악 제목을 반환한다.
조건이 일치하는 음악이 없을 때에는 “(None)”을 반환한다.

입력 형식
입력으로 네오가 기억한 멜로디를 담은 문자열 m과 방송된 곡의 정보를 담고 있는 배열 musicinfos가 주어진다.

m은 음 1개 이상 1439개 이하로 구성되어 있다.
musicinfos는 100개 이하의 곡 정보를 담고 있는 배열로, 각각의 곡 정보는 음악이 시작한 시각, 끝난 시각, 음악 제목, 악보 정보가 ','로 구분된 문자열이다.
음악의 시작 시각과 끝난 시각은 24시간 HH:MM 형식이다.
음악 제목은 ',' 이외의 출력 가능한 문자로 표현된 길이 1 이상 64 이하의 문자열이다.
악보 정보는 음 1개 이상 1439개 이하로 구성되어 있다.

출력 형식
조건과 일치하는 음악 제목을 출력한다.

입출력 예시
m	                musicinfos	                                                answer
"ABCDEFG"	        ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]	"HELLO"
"CC#BCC#BCC#BCC#B"	["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]	"FOO"
"ABC"	            ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]	"WORLD"

설명
첫 번째 예시에서 HELLO는 길이가 7분이지만 12:00부터 12:14까지 재생되었으므로 실제로 CDEFGABCDEFGAB로 재생되었고, 이 중에 기억한 멜로디인 ABCDEFG가 들어있다.
세 번째 예시에서 HELLO는 C#DEFGABC#DEFGAB로, WORLD는 ABCDE로 재생되었다. HELLO 안에 있는 ABC#은 기억한 멜로디인 ABC와 일치하지 않고, WORLD 안에 있는 ABC가 기억한 멜로디와 일치한다.

해설 보러가기
"""


def solution(m, musicinfos):
    # 18.384347578
    # m = m.replace("C#", "c").replace("D#", "d").replace("F#", "f").replace("G#", "g").replace("A#", "a")
    #
    # new_music_infos = []
    # for info in musicinfos:
    #     start, end, name, sheet = info.split(",")
    #     t1, t2 = start.split(":"), end.split(":")
    #     hour = int(t2[0]) - int(t1[0])
    #     minute = int(t2[1]) - int(t1[1])
    #     t = hour * 60 + minute
    #     sheet = sheet.replace("C#", "c").replace("D#", "d").replace("F#", "f").replace("G#", "g").replace("A#", "a")
    #     new_music_infos.append([t, name, sheet * (t//len(sheet)) + sheet[:t%len(sheet)]])
    # new_music_infos.sort(key=lambda x: x[0], reverse=True)
    #
    # for nmi in new_music_infos:
    #     time, name, sheet = nmi
    #     if m in sheet:
    #         return name
    # return "(None)"

    # using list version - 20.955843533
    new_m = []
    for ch in m:
        if ch == "#":
            new_m[-1] += "#"
        else:
            new_m.append(ch)

    new_music_infos1 = []
    for info in musicinfos:
        start, end, name, sheet = info.split(",")
        t1, t2 = start.split(":"), end.split(":")
        hour = int(t2[0]) - int(t1[0])
        minute = int(t2[1]) - int(t1[1])
        t = hour * 60 + minute

        new_sheet = []
        for ch in sheet:
            if ch == "#":
                new_sheet[-1] += "#"
            else:
                new_sheet.append(ch)
        new_music_infos1.append([t, name, new_sheet * (t//len(new_sheet)) + new_sheet[:t%len(new_sheet)]])
    new_music_infos1.sort(key=lambda x: x[0], reverse=True)

    for nmi in new_music_infos1:
        time, name, sheet = nmi
        N = len(sheet)
        for i in range(N-len(new_m)+1):
            if new_m == sheet[i: i+len(new_m)]:
                return name
    return "(None)"


# print(solution("ABCDEFG", ["13:00,13:05,WORLD,ABCDEF", "12:00,12:14,HELLO,CDEFGAB"]))         # hello
# print(solution("ABCDEFG", ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]))         # hello
# print(solution("CC#BCC#BCC#BCC#B", ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"])) # foo
# print(solution("ABC", ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]))            # world

# print(solution("ABC", ["10:00,10:03,H2,CAB", "11:00,11:04,H1,ABC", "12:00,12:03,H0,BCA"]))   # H1
# print(solution("ABC", ["11:00,11:03,H1,ABC", "12:00,12:03,H0,BCA", "10:00,10:03,H2,CAB"]))   # H1
# print(solution("ABC", ["10:00,10:03,H2,CAB", "12:00,12:03,H0,BCA", "11:00,11:03,H1,ABC"]))   # H1
# print(solution("ABC", ["10:00,10:03,H2,CAB", "11:00,11:03,H1,ABC", "12:00,12:03,H0,BCA"]))   # H1

# print(solution("AB", ["12:00,12:03,H0,ABCDE", "13:00,13:02,H1,ABCDEFG"]))            # H0
# print(solution("BA", ["12:00,12:03,H0,ABCDE", "13:00,13:02,H1,ABCDEFG"]))            # None
# print(solution("ABC", ["00:00,00:04,HI,ABC#ABC"]))                                   # None

print(solution("AA#B", ["13:50,14:00,H0,AA#BCC#DEFF#GG#", "14:00,14:10,H1,AA#BCC#DEFF#GG#"]))   # H0


if __name__ == '__main__':
    from timeit import Timer
    t = Timer("for t in [['AA#B', ['13:50,14:00,H0,AA#BCC#DEFF#GG#', '14:00,14:10,H1,AA#BCC#DEFF#GG#']], "
              "['AB', ['12:00,12:03,H0,ABCDE', '13:00,13:02,H1,ABCDEFG']], "
              "['ABCDEFG', ['13:00,13:05,WORLD,ABCDEF', '12:00,12:14,HELLO,CDEFGAB']]] "
              ": solution(*t)", "from __main__ import solution")
    print(t.timeit())