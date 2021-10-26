def solution(n):
    empty_space = n - 1
    sharp_space = 1

    for _ in range(n):
        empty_string = " " * empty_space
        sharp_string = "#" * sharp_space
        print(empty_string + sharp_string)
        empty_space -= 1
        sharp_space += 1


if __name__ == "__main__":
    n = int(input())
    solution(n)