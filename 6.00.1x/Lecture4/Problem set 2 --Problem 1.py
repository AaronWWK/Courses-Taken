#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 17:40:23 2017

@author: Weikang_Wan
"""


balance = 42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

for i in range(12):
    balance = balance + annualInterestRate/12*balance
    balance = balance*(1- monthlyPaymentRate)

print('Remaining balance:',round(balance,2))
