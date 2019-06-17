# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 11:40:08 2016

@author: ericgrimson
"""

cube = 27
guess_list = []
for guess in range(cube+1):
    if guess**3 == cube:
        print("Cube root of", cube, "is", guess)
        # guess_list.append(guess)
        break
print(guess)
# if len(guess_list) == 0:
#     print('No root of cube')
