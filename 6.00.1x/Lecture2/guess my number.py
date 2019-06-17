print('Please think of a number between 0 and 100!')
big = 100
small = 0

result = False
while result == False:
    middle = int((big + small)/2)
    print('Is your secret number',middle,'?')
    answer = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. + \
                   Enter 'c' to indicate I guessed correctly.")
    if answer == 'h':
        big = middle
    elif answer == 'l':
        small = middle
    elif answer == 'c':
        result = True
        print('Game over. Your secret number was:',middle)
    else:
        print('Sorry, I did not understand your input.')

    print(result)
