#!/usr/local/bin/python3
# return statement
import random


possibleAnswer = [
    'It is certain',
    'It is decidedly so',
    'Yes',
    'Reply hazy try again',
    'Ask again later',
    'Concentrate and ask again',
    'My reply is no',
    'Outlook not so good',
    'Very doubtful'
]

def getAnswer(answerIndex):
    return possibleAnswer[answerIndex]


r = random.randint(0, 8)
fortune = getAnswer(r)
print(fortune)
