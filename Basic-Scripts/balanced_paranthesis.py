open_bracket_list = ["[", "{", "("]
close_bracket_list = ["]", "}", ")"]


def checkParanthsis(data):
    stack = []
    for i in data:
        if i in open_bracket_list:
            stack.append(i)
        elif i in close_bracket_list:
            pos = close_bracket_list.index(i)
            if (len(stack) > 0) and (open_bracket_list[pos] == stack[len(stack) - 1]):
                stack.pop()
            else:
                return "Unbalanced"
    if len(stack) == 0:
        return "Balanced"
    else:
        return "Unbalanced"


if __name__ == "__main__":

    data = input()
    result = checkParanthsis(data)
    print(result)
