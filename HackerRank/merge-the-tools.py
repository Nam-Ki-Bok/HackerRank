def merge_the_tools(string, k):
    # your code goes here
    start_idx = 0
    end_idx = k
    length = end_idx - start_idx

    while end_idx <= len(string):
        answer = ""
        check_dict = dict()
        for idx in range(start_idx, end_idx):
            if string[idx] not in check_dict:
                check_dict[string[idx]] = True
                answer += string[idx]
        start_idx += length
        end_idx += length
        print(answer)


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)