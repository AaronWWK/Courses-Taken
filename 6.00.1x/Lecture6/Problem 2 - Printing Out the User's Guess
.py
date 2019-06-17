def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    guessedWord = []
    for i in range(len(secretWord)):
        guessedWord += ['_ ']

    secretlist = []
    for i in range(len(secretWord)):
        secretlist = secretlist + [secretWord[i:i+1]]


    for letters in lettersGuessed:
        if letters in secretlist:

            for k in range(len(secretlist)):

                if secretlist[k] == letters:
                    guessedWord[k]= letters        ###  循环替换
                else:
                    pass



            for char2 in secretlist:
                if char2 == letters:
                    secretlist[secretlist.index(char2)]= '_'    ####  L.index(e) returns the index of the !!! first  !!! occurrence of e in L.


    guessedWord2 = ''
    for j in range(len(guessedWord)):
        guessedWord2 += str(guessedWord[j])
    return guessedWord2

secretWord = 'apple'
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
print(getGuessedWord(secretWord, lettersGuessed))
##'_ pp_ e'
