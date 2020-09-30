import re
def snake_to_camel(string):
    """
    Parameters: 
    snake_to_camel (str): takes a string. 
    
    Returns:
    string value in camel case by removing underscore or dash and capitalizing every word

    """
    return "".join(word.capitalize() or '_' for word in re.split("-|_", string))

if __name__ == "__main__":
    string = input("Enter string in snake case:")
    print(snake_to_camel(string))

