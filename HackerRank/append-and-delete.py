def solution(s, t, k):
    diff_idx = len(s)
    for idx in range(min(len(s), len(t))):
        if s[idx] != t[idx]:
            diff_idx = idx
            break

    diff_len = len(s) - diff_idx + len(t) - diff_idx
    if diff_len <= k and (diff_len - k) % 2 == 0 or len(s) + len(t) <= k:
        return "Yes"
    else:
        return "No"


if __name__ == "__main__":
    s = input()
    t = input()
    k = int(input())

    print(solution(s, t, k))