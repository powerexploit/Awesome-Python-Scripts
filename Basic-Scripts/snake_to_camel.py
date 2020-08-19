import re
def snake_to_camel(string):
        return "".join(word.capitalize() or '_' for word in re.split("-|_", string))

def main():
    string = raw_input("Enter string in snake case:")
    print(snake_to_camel(string))

main()
