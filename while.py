#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

words = ['one', 'two', 'three', 'four', 'five']

n = 0
while(n < 5):
    print(words[n])
    n += 1

a, b = 0, 1
while b < 1000:
    print(b, end = ' ', flush = True)

    #temp = b
    #b = b + a
    #a = temp
    a, b = b, a + b
    #same code different lengths

print() # line ending

secret = 'tmuweh'
pw = ''
count = 0;
max_attempt = 5

auth = False
while pw != secret:
    count += 1
    if count > max_attempt:
        print("Sorry you lavished your 5 trials")
        break
    pw = input(f"<{max_attempt - count} trials left>What's the secret word? ")
else:
    auth = True

print("Authorized!" if auth else "Calling the police now!")
