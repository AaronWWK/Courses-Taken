def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE..
    AvilableLetters = 'abcdefghigklmnopqrstuvwxyz'
    AvilableList = []
    for i in range(len(AvilableLetters)):
        AvilableList += [AvilableLetters[i:i+1]]

    for letters in lettersGuessed:
        if letters in AvilableList:
            AvilableList.remove(letters)

    AvilableList2 = ''
    for j in range(len(AvilableList)):
        AvilableList2 += str(AvilableList[j])
    return AvilableList2





lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
print(getAvailableLetters(lettersGuessed))
