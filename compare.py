#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/
import random

x = random.randrange(20, 100, 5)
y = random.randrange(20, 100, 5)

if x < y:
    print(f'x:{x} is less than y:{y}')
else:
    print(f'x:{x} is not less than y:{y}')

if x > y:
    print(f'x:{x} is greater than y:{y}')
else:
    print(f'x:{x} is not greater than y:{y}')

if x <= y:
    print(f'x:{x} is less than or equal to y:{y}')
else:
    print(f'x:{x} is not less than or equal to y:{y}')

if x >= y:
    print(f'x:{x} is greater than or equal to y:{y}')
else:
    print(f'x:{x} is not greater than or equal to y:{y}')

if x != y:
    print(f'x:{x} is not equal to y:{y}')
else:
    print(f'x:{x} is equal to y:{y}')

if x == y:
    print(f'x:{x} is equal to y:{y}')
else:
    print(f'x:{x} is not equal to y:{y}')