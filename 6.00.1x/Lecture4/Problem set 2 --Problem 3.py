#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  4 10:19:13 2017

@author: Weikang_Wan
"""


"""
def lp(b,air):
    ##Input Balance
    ##Output monthly payment through bisection method


    def lowest_payment(lp):
        mir = air /12
        lb =b /12
        ub =(b*(1+mir)**12)/12
        lp = (lb+ub)/2
        b0=b
        for i in range(12):
            b0 = b0 - lp
            b0 = b0 + 0.2/12*b0  ##年利率 20%   lp：每个月最低还款数
        if b0 > 0.001:
            lb = lp
            lp2 = (lb+ub)/2
            return lowest_payment(lp2)
        elif b0 < -0.001:
            ub = lp
            lp2 = (lb+ub)/2
            return lowest_payment(lp2)
        else:
            return lp
    return round(lowest_payment(lp),2)

print('Lowest Payment:',lp(4737,0.2))

"""

def lp(b,air):
    ##Input Balance
    ##Output monthly payment through bisection method
    mir = air /12
    lb =b /12
    ub =(b*(1+mir)**12)/12
    lp = (lb+ub)/2
    def lowest_payment(a,ub,lb,lp):
        ub2= ub
        lb2= lb
        b0=b
        a2 = a+1
        for i in range(12):
            b0 = b0 - lp
            b0 = b0 + mir*b0  ##年利率 20%   lp：每个月最低还款数
        if b0 > 0.001:
            lb2 = lp
            lp2 = (lb+ub)/2

            return lowest_payment(a2,ub2,lb2,lp2)
        elif b0 < -0.001:
            ub2 = lp
            lp2 = (lb+ub)/2

            return lowest_payment(a2,ub2,lb2,lp2)
        else:

            return lp

    return round(lowest_payment(a,ub,lb,lp),2)
a=1
balance = 320000
annualInterestRate = 0.2
print('Lowest Payment:',lp(balance,annualInterestRate))



##############   终于写对了！！！！！！！





"""

b = 999999
air = 0.18
mir = air /12
lb =b /12
ub =(b*(1+mir)**12)/12
##  True
while True:
    lp = (ub + lb)/2
    b0 = b
    for i in range(12):
        b0 -=lp
        b0 += mir*b0
    if abs(b0)< 0.01:
        print(round(lp,2))
        break
    elif b0 > 0:
        lb = lp
    else:
        ub = lp




b = 999999
air = 0.18
mir = air /12
lb =b /12
ub =(b*(1+mir)**12)/12
b0=b
while abs(b0)> 0.01:
    lp = (ub + lb)/2
    b0 = b
    for i in range(12):
        b0 -=lp
        b0 += mir*b0

    if b0 > 0:
        lb = lp
    else:
        ub = lp
print(round(lp,2))
"""
