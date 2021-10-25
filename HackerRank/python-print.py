def solution(n):
    answer = ""
    for i in range(1, n + 1):
        answer += str(i)

    return answer


if __name__ == '__main__':
    n = int(input())
    print(solution(n))