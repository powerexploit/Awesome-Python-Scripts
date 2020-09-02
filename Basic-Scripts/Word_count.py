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

if __name__ == '__main__':
    count_Words('count_Words.py')
