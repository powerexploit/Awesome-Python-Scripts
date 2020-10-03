import os

'''
SAMPLE INPUT =
3
{[()]}
{[(])}
{{[[(())]]}}

SAMPLE OUTPUT=
YES
NO
YES


'''
def isBalanced(s):
    table = {')': '(', ']': '[', '}': '{'}
    stack = []
    for x in s:
        if stack and table.get(x) == stack[-1]:
            stack.pop()
        else:
            stack.append(x)
    if stack:
        return "NO"
    else:
        return "YES"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
