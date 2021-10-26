def solution(arr):
    answer = list()
    arr.sort()
    answer.append(sum(arr[0:4]))
    answer.append(sum(arr[len(arr) - 4:len(arr)]))
    return answer


if __name__ == "__main__":
    arr = list(map(int, input().split()))
    result = solution(arr)

    print(*result)