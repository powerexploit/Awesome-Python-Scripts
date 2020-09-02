def countWords(fileName):
    number_of_words = 0
    number_of_characters = 0
    number_of_lines = 0

    with open(fileName, 'r') as file:
        for line in file:
            wordlist = line.split()
            number_of_lines += 1
            number_of_words += len(wordlist)
            number_of_characters += len(line)

    print ("Words: ", number_of_words)
    print ("Lines: ", number_of_lines)
    print ("Characters: ", number_of_characters)

if __name__ == '__main__':
    countWords('quad.txt')
