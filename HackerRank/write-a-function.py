def is_leap(year):
    leap = False

    # Write your logic here
    # 4로 나누어지며 100으로 나누어지지 않고 400으로 나누어지면 윤년이다.

    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        leap = True

    return leap


if __name__ == "__main__":
    year = int(input())
    print(is_leap(year))