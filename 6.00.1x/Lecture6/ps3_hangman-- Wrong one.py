# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "/Users/wanweikang/Desktop/Python/Python —EDX/asset-v1_Lecture6/words.txt"


def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()


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
        letterslist = letterslist + [secretWord[i:i + 1]]
    result = False
    for letters in letterslist:
        if letters in lettersGuessed:
            result =True
    return result


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
        secretlist = secretlist + [secretWord[i:i + 1]]

    for letters in lettersGuessed:
        if letters in secretlist:

            for k in range(len(secretlist)):

                if secretlist[k] == letters:
                    guessedWord[k] = letters  ###  循环替换
                else:
                    pass

            for char2 in secretlist:
                if char2 == letters:
                    secretlist[secretlist.index(
                        char2)] = '_'  ####  L.index(e) returns the index of the !!! first  !!! occurrence of e in L.

    guessedWord2 = ''
    for j in range(len(guessedWord)):
        guessedWord2 += str(guessedWord[j])
    return guessedWord2


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    AvilableLetters = 'abcdefghigklmnopqrstuvwxyz'
    AvilableList = []
    for i in range(len(AvilableLetters)):
        AvilableList += [AvilableLetters[i:i + 1]]

    for letters in lettersGuessed:
        if letters in AvilableList:
            AvilableList.remove(letters)

    AvilableList2 = ''
    for j in range(len(AvilableList)):
        AvilableList2 += str(AvilableList[j])
    return AvilableList2


def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    print(secretWord)
    print('Welcome to the game, Hangman!')
    print('I am thinking of a word that is ', len(secretWord), ' letters long.')

    lettersGuessed = []

    for i in range(8):
        print('-------------')
        print('You have ', 8 - i, 'guesses left.')
        print('Available letters: ', getAvailableLetters(lettersGuessed))
        guess = getAvailableLetters(lettersGuessed)[6]

        if  guess in lettersGuessed:
            print("Oops! You've already guessed that letter:", getGuessedWord(secretWord, lettersGuessed))

        else:
            lettersGuessed += [guess]


        if isWordGuessed(secretWord, lettersGuessed):
            print('Good guess:', getGuessedWord(secretWord, lettersGuessed))
            if getGuessedWord(secretWord, lettersGuessed) == secretWord:
                print('Congratulations, you won!')
                break

            else:
                pass

        else:
            print('Oops! That letter is not in my word', getGuessedWord(secretWord, lettersGuessed))

    print('------------')
    if getGuessedWord(secretWord, lettersGuessed) == secretWord:
        print('Haha, I win')
    else:
        pass


secretWord = chooseWord(wordlist)

hangman(secretWord)












# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

# secretWord = chooseWord(wordlist).lower()
# hangman(secretWord)
