def solution(n, arr):
    positive_cnt, negative_cnt, zero_cnt = 0, 0, 0

    for num in arr:
        if num > 0:
            positive_cnt += 1
        elif num < 0:
            negative_cnt += 1
        else:
            zero_cnt += 1

    print("{:.6f}".format(positive_cnt / n))
    print("{:.6f}".format(negative_cnt / n))
    print("{:.6f}".format(zero_cnt / n))


if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))

    solution(n, arr)