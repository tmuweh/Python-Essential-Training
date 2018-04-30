#!/usr/bin/env python3

from decimal import  *

#Dealing with money. not floating points

a = Decimal('.10')
b = Decimal('.30')
x = a + a + a - b

print("x is {}". format(x))
print(type(x))