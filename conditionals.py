#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

import random

#generate random numbers and store in x and y
x = random.randrange(1, 10)
y = random.randrange(1, 10)

if x > y:
    print('x greater than y: x is {} and y is {}'.format(x, y))
elif x == y:
    print("x equals y: x is {} and y is {}".format(x, y))
else:
    print("x less than y: x is {} and y is {}".format(x, y))