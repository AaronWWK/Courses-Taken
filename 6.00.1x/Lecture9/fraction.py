# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 19:51:18 2016

@author: ericgrimson
"""

class fraction(object):
    def __init__(self, numer, denom):
        self.numer = numer
        self.denom = denom
    def __str__(self):
        return str(self.numer) + ' / ' + str(self.denom)
    def getNumer(self):       #user defined
        return self.numer
    def getDenom(self):
        return self.denom
    def __add__(self, other):  # inside python, just use '+' to operate,
                               # just like '__str__', use print() to get str
        numerNew = other.getDenom() * self.getNumer() \
                   + other.getNumer() * self.getDenom()
        denomNew = other.getDenom() * self.getDenom()
        return fraction(numerNew, denomNew)
    def __sub__(self, other):
        numerNew = other.getDenom() * self.getNumer() \
                   - other.getNumer() * self.getDenom()
        denomNew = other.getDenom() * self.getDenom()
        return fraction(numerNew, denomNew)
    def convert(self):
        return self.getNumer() / self.getDenom()


onehalf = fraction(1,2)
onethirds = fraction(1,3)
print(onehalf)
print(onethirds)
print(onehalf.getDenom())
fuck = onehalf + onethirds
print(fuck)
print(onehalf.convert())
