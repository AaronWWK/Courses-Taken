def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...

    letterslist = []
    for i in range(len(secretWord)):
        letterslist = letterslist + [secretWord[i:i+1]]
    result = True
    for letters in letterslist:
        if letters not in lettersGuessed:
            result = False
    return result



secretWord = 'squelching'
lettersGuessed = ['s']
print(isWordGuessed(secretWord, lettersGuessed))
