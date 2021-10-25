def minion_game(string):
    len_string = len(string)
    stuart_score = 0
    kevin_score = 0

    for idx, char in enumerate(string):
        if char in ("A", "E", "I", "O", "U"):
            kevin_score += len_string - idx
        else:
            stuart_score += len_string - idx

    if stuart_score < kevin_score:
        print("Kevin", kevin_score)
    elif stuart_score > kevin_score:
        print("Stuart", stuart_score)
    else:
        print("Draw")


if __name__ == '__main__':
    s = input()
    minion_game(s)