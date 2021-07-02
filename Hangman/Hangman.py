import random
import re
with open('dictionary.txt') as file:
    word = list(file)
answer = str(random.choice(word).strip())
#print(answer)
answerchar = []

for x in range(0,len(answer)):
    answerchar.append("-")

print("Welcome to Hangman!")
print('The word has',len(answer),'characters')

guessnumber = 5
i = 0
guess = re.compile(r'[A-Z]+')
guessedlist = []
print("You have",guessnumber,"guesses left")

while i in range(0,guessnumber):
    guessletter = str(input("Guess your letter: ").upper())
    if guess.match(guessletter) == None:
        print("Invalid characters")
        continue
    elif len(guessletter) != 1:
        print("Please enter only one character")
        continue
    elif guessletter in guessedlist:
        print("This character has been guessed")
        continue
    else:
        guessedlist.append(guessletter)
        #print(guessedlist)
    for j in range(0,len(answer)):
        if answer[j] == guessletter:
            answerchar[j] = guessletter
    answerstr = ' '.join(answerchar)
    if re.search(guessletter,answerstr) and re.search("-",answerstr):
        if guessnumber == 1:
            print("You guessed it right! You have",guessnumber,"guess left")
            print(answerstr)
        else:
            print("You guessed it right! You have",guessnumber,"guesses left")
            print(answerstr)
    elif re.search("-",answerstr):
        guessnumber -= 1
        if guessnumber > 1:
            print("You guessed it wrong! You have",guessnumber,"guesses left")
            print(answerstr)
        elif guessnumber == 1:
            print("You guessed it wrong! You have",guessnumber,"guess left")
            print(answerstr)
        else:
            print("You guessed it wrong! You lose!")
            print("The answer is",answer,"!")
            break
    else:
        print("You win! The answer is",answer,"!")
        break
print(input("End"))
