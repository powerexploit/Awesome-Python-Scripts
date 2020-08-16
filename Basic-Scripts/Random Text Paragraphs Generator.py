#!bin/bash/python3

try:
    # Importing random module for generating Random Text, Word by Word, character by character
    import random

    space_character = ' ' 
    letters_ordinals = list(range(ord('A'), ord('Z')+1)) + list(range(ord('a'), ord('z')+1))    # Ordinals of character lie in range(65-65+25, then 97-97+25 characters)
    OutputFileName = "Random_Text"  # Set any file name you'd like to have random text into.

    # Safely trying to open file for read/write mode with "w+" to ensure that file will be created if it does not exist
    # If no file could be accessed, simply exiting the program with exit() 
    try:
        fileHandle = open(OutputFileName+".txt", "w+")
    except:
        OutputFileName += "_"   # Can add any new number to be appended at the fileName
        try: fileHandle = open(OutputFileName+".txt", "w+")
        except: exit()
        finally: print("Thank you for your time! Please Retry later!")

    number_of_paragraphs = input("Enter the number of paragraphs to be written: ")
    try: number_of_paragraphs = int(number_of_paragraphs)
    except: number_of_paragraphs = 10
    lengthRangeOfEachWord = [1, 15]

    # Writing paragraphs with every word, character-by-character
    for paragraph_iteration in range(number_of_paragraphs):
        for words_count in range(random.randint(50, 100)):
            for word_count in range(random.randint(*lengthRangeOfEachWord)):
                fileHandle.write(chr(random.choice(letters_ordinals)))
            fileHandle.write(space_character)
        fileHandle.write("\n")      # Using Newine to separate paragraphs

    # Flushing any active buffer, and safely closing the file.
    fileHandle.flush()
    fileHandle.close()

except: print(" [ Unexpected Error Occured! Safely Hanging up, until next time! ] ")
else:
    # Mentioning the final confirmation
    print(" [ Should be Done! Please check the file same directory where this program is executed. ] ")
finally:
    # Ending with a greeting
    print("\t\t Thank you!")