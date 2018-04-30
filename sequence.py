#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

#List
x = [ 1, 2, 3, 4, 5 ]
x[4] = 45
for i in x:
    print('i is {}'.format(i))

#Tuples

y = (1, 2, 3, 4, 5 )
for i in y:
    print('i is {}'.format(i))

#range
z = range(0, 10)
for i in z:
    print(i)

#dictionary

dic = {'one': 1, 'two': 2, 'three': 3}

for k, v in dic.items():
    print(k, v)

seq = [x, y, z, dic]
for i in seq:
    print(type(i))
    print(id(i)) #use to see if the same objects

    if isinstance(i , tuple):
        print("Tuple")
    elif isinstance(i, list):
        print("list")
    else:
        print("Range")