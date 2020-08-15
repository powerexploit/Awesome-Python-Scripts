#This is the program to find out if the string  contains: alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters.
if __name__ == '__main__':
    s = input()
    res = ["False", "False", "False", "False", "False"]
    for i in s:
        if i.isalnum():
            res[0] = "True"
        if i.isalpha():
            res[1] = "True"
        if i.isdigit():
            res[2] = "True"
        if i.islower():
            res[3] = "True"
        if i.isupper():
            res[4] = "True"
    print(*res, sep="\n")

    #Input Format will be A single line containig a string.
    #Output Format will be as follows:
    #In the first line, print True if string has any alphanumeric characters. Otherwise, print False.
    #In the second line, print True if string  has any alphabetical characters. Otherwise, print False.
    #In the third line, print True if string  has any digits. Otherwise, print False.
    #In the fourth line, print True if string has any lowercase characters. Otherwise, print False.
    #In the fifth line, print True if string  has any uppercase characters. Otherwise, print False.