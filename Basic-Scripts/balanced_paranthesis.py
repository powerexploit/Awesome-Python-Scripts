openBracketList = ["[", "{", "("]
closeBracketList = ["]", "}", ")"]


def checkParanthsis(data: str) -> str:
    """
    checkParanthsis() : Will take a string as an arguement and each time when an open parentheses is encountered 
    will push it in the stack, and when closed parenthesis is encountered, 
    will match it with the top of stack and pop it. 

    Parameters: 
    data (str): takes a string. 
  
    Returns: 
    str: Returns a string value whether string passed is balanced or Unblanaced. 
	"""
    stack = []
    for index in data:
        if index in openBracketList:
            stack.append(index)
        elif index in closeBracketList:
            position = closeBracketList.index(index)
            if (len(stack) > 0) and (
                openBracketList[position] == stack[len(stack) - 1]
            ):
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
