def isBalanced(s):
    open_brackets = ['(', '[', '{']
    close_brackets = [')', ']', '}']
    open_brackets_stack = list()

    for bracket in s:
        if bracket in open_brackets:
            open_brackets_stack.append(bracket)

        if bracket in close_brackets:
            if open_brackets_stack:
                open_bracket = open_brackets_stack[-1]
                close_bracket = bracket
                if open_brackets.index(open_bracket) == close_brackets.index(close_bracket):
                    open_brackets_stack.pop()
                else:
                    return "NO"
            else:
                return "NO"

    return "NO" if open_brackets_stack else "YES"


if __name__ == "__main__":
    s = input()
    print(isBalanced(s))
