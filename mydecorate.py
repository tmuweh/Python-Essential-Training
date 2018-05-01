
import time
import random


def duration(f):

    t1 = time.time()
    f()
    t2 = time.time()
    print(f"It took me { (t2 - t1) * 1000} ms to calculate the above factorial!")

@duration
def factorial100():

    num_list = []
    fact = 1
    for num in range(1, 11):
        num_list.append(num)
    print(num_list)
    for i in num_list:
        fact *= i
    print(fact)

def main():
    factorial100()

if __name__ == '__name__': main()

