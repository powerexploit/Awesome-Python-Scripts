#import od module
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
    '''

    Args:The string
        s: String which is to be checked if it has all balanced brackets or no.

    Returns: "YES" if the brackets are balanced in the string else it returns "NO".

    '''
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

#main program
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input()) #takes the input ie number of test cases from user

    for t_itr in range(t):
        s = input()  #string taken as input from the user

        result = isBalanced(s) #isBalanced(s) function will return "YES" if the brackets are balanced else it will return "NO

        fptr.write(result + '\n')

    fptr.close()
