# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 12:13:04 2016

@author: ericgrimson
"""

# x = float(input('Enter a decimal number between 0 and 1: '))
x = 3.372

p = 0
while ((2**p)*x)%1 != 0:
    print('Remainder = ' + str((2**p)*x - int((2**p)*x)))
    p += 1

num = int((2**p)*x)

result = ''
if num == 0:
    result = '0'
while num > 0:
    result = str(num%2) + result
    num = num//2

for i in range(p - len(result)):
    result = '0' + result
    print(result)

result = result[0:-p] + '.' + result[-p:]    #add a decimal point to the binary number

print('The binary representation of the decimal ' + str(x) + ' is ' + str(result))
