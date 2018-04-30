#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

x = 42
y = 73

if x < y:
    z = 20
    print('x < y: x is {} and y is {}'.format(x, y))
    print("I am pack of the if block")
print("I am not a part of the if block")

#blocks do not define scopes in python

print("I am z and my value is ", format(z),"defined in the if block and printed out of it")