# -*- coding: utf-8 -*-
"""
Created on Wed May 18 20:32:38 2016

@author: ericgrimson
"""

def selSort(L):
    for i in range(len(L) - 1):
        print(L)
        minIndx = i
        minVal= L[i]
        j = i + 1
        while j < len(L):
            if minVal > L[j]:
                minIndx = j
                minVal= L[j]
            j += 1
        temp = L[i]
        L[i] = L[minIndx]
        L[minIndx] = temp




def selection_sort(L):
    temp = []
    L2 = L.copy()
    min_ = 0
    num = 0
    for i in range(0,len(L)):
        min_ = min(L2)
        temp.append(min_)
        L2.remove(min_)
        num +=1
    print(temp)
    print(num)






# -------  1/17/2019  ---------
# def selection_sort(L):
#     sorted = []
#     L_copy = L.copy()
#
#     while len(L_copy) > 1:
#         for i in range(len(L_copy)):
#             if L_copy[1] > L_copy[i]:
#                 temp = L_copy[1]
#                 L_copy[1] = L_copy[i]
#                 L_copy[i] = temp
#         sorted.append(L_copy[1])
#         #print(sorted)
#         L_copy.remove(L_copy[1])
#         print(L_copy)
#     sorted.append(L_copy[0])
#     print(sorted)



test = [1, 5, 3, 8, 4, 9, 6, 2]
selection_sort(test)
