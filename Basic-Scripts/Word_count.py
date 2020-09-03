# Author:- Prasad V Patil
# The following is a python script, which helps to count number of words, number of lines and number of characters from a file.


def count_Words(fileName):  
    number_of_words = 0
    number_of_characters = 0
    number_of_lines = 0

    with open(fileName, 'r') as file:
        for line in file:
            wordlist = line.split()
            number_of_lines += 1
            number_of_words += len(wordlist)
            number_of_characters += len(line)

    print ("Number of Words: ", number_of_words)
    print ("Number of Lines: ", number_of_lines)
    print ("Number of Characters: ", number_of_characters)

    
#Main Program    
if __name__ == '__main__':
    fileName = input("Enter file name: ")
    count_Words(filename)
    
    '''
    If this python file is given as file name,
    i.e, 
    count_Words('Word_count.py')
    Then, the following will be the output.
    '''
    
    #OUTPUT :-
    
    # Number of Words:  55
    # Number of Lines:  18
    # Number of Characters:  548
    
