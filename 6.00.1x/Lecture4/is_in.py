# #!/usr/bin/env python3
# # -*- coding: utf-8 -*-
# """
# Created on Thu Aug  3 16:20:15 2017
#
# @author: Weikang_Wan
# """
#
#
#
# def isIn(char, aStr):
#     '''
#     char: a single character
#     aStr: an alphabetized string
#
#     returns: True if char is in aStr; False otherwise
#     '''
#     #### 刚刚开始的自己写的
#     if len(aStr)<= 1:
#         return char == aStr
#     elif char < aStr[0] or char > aStr[-1]:
#         return False
#
#     elif len(aStr)%2 == 0:
#         if char == aStr[int(len(aStr)/2)]:
#             return True
#         else:
#             if char > aStr[int(len(aStr)/2)]:
#                 return isIn(char,aStr[int(len(aStr)/2)+1:])
#             else:
#                 return isIn(char,aStr[0:int(len(aStr)/2)])
#     else:
#         if char == aStr[int(len(aStr)/2+1)]:
#             return True
#         else:
#             if char > aStr[int(len(aStr)/2+1)]:
#                 return isIn(char,aStr[int(len(aStr)/2+1)+1:])
#             else:
#                 return isIn(char,aStr[0:int(len(aStr)/2+1)])
#
# ##精简 改进版
# def isIn2(char, aStr):
#     if len(aStr)<= 1:
#         return char == aStr
#     elif char < aStr[0] or char > aStr[-1]:
#         return False
#
#     elif char == aStr[int(len(aStr)//2)]:
#         return True
#     else:
#         if char > aStr[int(len(aStr)//2)]:
#             return isIn(char,aStr[int(len(aStr)//2+1):])
#         else:
#             return isIn(char,aStr[0:int(len(aStr)//2)])
#
# print(isIn2('b','abcd'))
#
#
#
# ####  课程答案的版本
# def isIn3(char, aStr):
#    '''
#    char: a single character
#    aStr: an alphabetized string
#
#    returns: True if char is in aStr; False otherwise
#    '''
#    # Base case: If aStr is empty, we did not find the char.
#    if aStr == '':
#       return False
#
#    # Base case: if aStr is of length 1, just see if the chars are equal
#    if len(aStr) == 1:
#       return aStr == char
#
#    # Base case: See if the character in the middle of aStr equals the
#    #   test character
#    midIndex = len(aStr)//2
#    midChar = aStr[midIndex]
#    if char == midChar:
#       # We found the character!
#       return True
#
#    # Recursive case: If the test character is smaller than the middle
#    #  character, recursively search on the first half of aStr
#    elif char < midChar:
#       return isIn(char, aStr[:midIndex])
#
#    # Otherwise the test character is larger than the middle character,
#    #  so recursively search on the last half of aStr
#    else:
#       return isIn(char, aStr[midIndex+1:])







def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string

    returns: True if char is in aStr; False otherwise
    '''
    if len(aStr) <= 1:
        return False
    elif char == aStr[int(len(aStr)/2)]:
        return True
    else:
        if char < aStr[int(len(aStr)/2)]:
            return isIn(char, aStr[0:int(len(aStr)/2)])
        else:
            return isIn(char, aStr[int(len(aStr)/2):])
