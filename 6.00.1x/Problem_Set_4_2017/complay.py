
def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.

    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.

    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.

    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.

        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the
          game with the selected hand, using compPlayHand.

    4) After the computer or user has played the hand, repeat from step 1

    wordList: list (string)
    """

    def compPlayHand(hand, wordList, n):
        """
        Allows the computer to play the given hand, following the same procedure
        as playHand, except instead of the user choosing a word, the computer
        chooses it.

        1) The hand is displayed.
        2) The computer chooses a word.
        3) After every valid word: the word and the score for that word is
        displayed, the remaining letters in the hand are displayed, and the
        computer chooses another word.
        4)  The sum of the word scores is displayed when the hand finishes.
        5)  The hand finishes when the computer has exhausted its possible
        choices (i.e. compChooseWord returns None).

        hand: dictionary (string -> int)
        wordList: list (string)
        n: integer (HAND_SIZE; i.e., hand size required for additional points)
        """
        # Keep track of the total score
        totalScore = 0
        # As long as there are still letters left in the hand:
        while (calculateHandlen(hand) > 0):
            # Display the hand
            print("Current Hand: ", end=' ')
            displayHand(hand)
            # computer's word
            word = compChooseWord(hand, wordList, n)
            # If the input is a single period:
            if word == None:
                # End the game (break out of the loop)
                break

            # Otherwise (the input is not a single period):
            else:
                # If the word is not valid:
                if (not isValidWord(word, hand, wordList)):
                    print('This is a terrible error! I need to check my own code!')
                    break
                # Otherwise (the word is valid):
                else:
                    # Tell the user how many points the word earned, and the updated total score
                    score = getWordScore(word, n)
                    totalScore += score
                    print('"' + word + '" earned ' + str(score) + ' points. Total: ' + str(totalScore) + ' points')
                    # Update hand and show the updated hand to the user
                    hand = updateHand(hand, word)
                    print()
        # Game is over (user entered a '.' or ran out of letters), so tell user the total score
        print('Total score: ' + str(totalScore) + ' points.')

    n = HAND_SIZE

    while True:
        asks = input('Enter n to deal a new hand, r to replay the last hand, or e to end game:')
        if asks == 'n':
            while True:
                asks2 = input('Enter u to have yourself play, c to have the computer play:')
                if asks2 == 'u':
                    hand = dealHand(HAND_SIZE)
                    playHand(hand, wordList, n)
                elif asks2 == 'c':
                    hand = dealHand(HAND_SIZE)
                    compPlayHand(hand, wordList, n)
                else:
                    print('Invalid command')
        elif asks == 'r':
            while True:
                asks2 = input('Enter u to have yourself play, c to have the computer play: ')
                if asks2 == 'u':
                    if hand == {}:
                        print('You have not played a hand yet. Please play a new hand first!')
                    else:
                        playHand(hand, wordList, n)
                elif asks2 == 'c':
                    if hand == {}:
                        print('You have not played a hand yet. Please play a new hand first!')
                    else:
                        compPlayHand(hand, wordList, n)
                else:
                    print('Invalid command')


        elif asks == 'e':
            break

        else:
            print('Invalid command.')
