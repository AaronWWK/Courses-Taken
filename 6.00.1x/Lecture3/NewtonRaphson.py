# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 12:14:22 2016

@author: ericgrimson
"""
"""
General approximation algorithm to find roots of a polynomial in one variable
p(x) = anxn + an-1xn-1 + ... + a1x + a0
􏰀Want to find r such that p(r) = 0
􏰀For example, to find the square root of 24, find the root of p(x) = x2 – 24
􏰀Newton showed that if g is an approximation to the root, then
g – p(g)/p’(g)
is a better approximation; where p’ is derivative of p
"""
epsilon = 0.01
y = 24.0
#p(x) = guess^2 - y
#p'(x) = 2guess

guess = y/2.0
numGuesses = 0

while abs(guess*guess - y) >= epsilon:
    numGuesses += 1
    guess = guess - (((guess**2) - y)/(2*guess))
print('numGuesses = ' + str(numGuesses))
print('Square root of ' + str(y) + ' is about ' + str(guess))
