from string import ascii_lowercase, ascii_uppercase


def solution(s, k):
    lower_letters = list(ascii_lowercase)
    upper_letters = list(ascii_uppercase)

    answer = list(s)
    for idx, alpha in enumerate(answer):
        if 'a' <= alpha <= 'z':
            answer[idx] = lower_letters[(lower_letters.index(alpha) + k) % 26]

        if 'A' <= alpha <= 'Z':
            answer[idx] = upper_letters[(upper_letters.index(alpha) + k) % 26]

    return "".join(answer)


if __name__ == "__main__":
    n = int(input())
    s = input()
    k = int(input())

    print(solution(s, k))