# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 11:51:57 2016

@author: ericgrimson


"""
low = 0
high = 100
ans = int((high + low)/2)
guessed = False
print('Please think of a number between 0 and 100!') 


while not guessed:
    ans = (high + low)/2
    print('Is your secret number '+ str(ans)+'?')
    s = (input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too high. Enter 'c' to indicate I guessed correctly."))

    if s == 'l':
        low = ans
        
    elif s == 'h':
        high = ans
        
    elif s == 'c':
        guessed = True
    else:
        print('Sorry, I did not understand your input.')
pirnt('Game over. Your secret number was: ' + str(ans))
        
