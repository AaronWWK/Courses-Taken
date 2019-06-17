# # -*- coding: utf-8 -*-
# """
# Created on Wed Jun 15 09:15:09 2016
#
# @author: ericgrimson
# """
#
# x = 6
#
# if x != 5:
#     print('i am here')
# else:
#     print('no I am not')

def outer():
    num = 10
    def inner():
        nonlocal num
        print(num)
        num = 100
        print(num)
    inner()
    print(num)
outer()
print(outer)
