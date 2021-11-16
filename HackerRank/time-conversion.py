def solution(s):
    time = s[:-2].split(":")
    day = s[-2:]

    if day == 'AM':
        if time[0] == '12':
            time[0] = '00'

    if day == 'PM':
        if 1 <= int(time[0]) <= 11:
            time[0] = str(int(time[0]) + 12)

    return ":".join(time)


if __name__ == "__main__":
    s = input()
    print(solution(s))