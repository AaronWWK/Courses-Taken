#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 15:43:00 2017

@author: Weikang_Wan
"""

def gcdIter(a, b):
    '''
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    '''
    small = min(a,b)

    while small >1:
        if a%small == 0 and b%small == 0:
            print('The divisor of a and b is',small)
            return small
        else:
            small -= 1
    print('The divisor of a and b is 1')
    return small




def gcdRecur(a, b):
    '''
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    divisor = 1
    Big = max(a,b)
    Small = min (a,b)

    if min(a,b) == 0:
        return Big
    else:
        divisor = gcdRecur(Small,Big%Small)
    return divisor


print(gcdRecur(132414,345))
