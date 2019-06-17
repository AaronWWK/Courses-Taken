# -*- coding: utf-8 -*-
"""
Created on Tue Jun 14 14:06:53 2016

@author: WELG
"""

def bubble_sort(L):
    swap = False  # serve as a flag, if there is a element in the list that's not sorted, the swap will continue
    num = 0
    while not swap:
        swap = True
        #print(L)
        for j in range(1, len(L)):
            print(L)
            num += 1
            if L[j-1] > L[j]:
                swap = False
                temp = L[j]
                L[j] = L[j-1]
                L[j-1] = temp
    print(num)

def bubble_sort2(L):
    num = 0
    '''When the largers number is bubbled to the end of the list, there is no need to check it
       so the len of the list is shorten by 1 for each recursion'''
    for i in range(len(L)-1, 0 ,-1 ):  # 0 index array's last item, backward, if forward, should be range(0,len(len(L)))
        for j in range(i):
            num += 1
            print(L)
            #print(L[0:j])
            if L[j] > L[j+1]:
                temp = L[j]
                L[j] = L[j+1]
                L[j+1] = temp
    print(num)

test = [1, 5, 3, 8, 4, 2, 9, 6]
#bubble_sort(test)
bubble_sort2(test)
