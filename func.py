#!/usr/bin/env python3

import  random

def isprime(n):

    if n <= 1:
        return False
    for x in range(2, n):
        if n % x == 0:
            return False
    else:
        return True

#call prime
number = random.randrange(0, 100)
prime = isprime( number)
if isprime(number):
    print("number {} is prime".format(number))
else:
    print("number {} is not prime".format(number))



def fac(n):
    if n < 0:
        return -1
    else:
        if n == 0:
            return 1
        else:
            return n * fac(n - 1)

#fac() call
facto = random.randrange(1, 10)

print(str(facto), "Factorial is {}".format(fac(facto)))