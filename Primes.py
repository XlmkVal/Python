def check_primes_v1(num):
    """ Returns true or false, depending if the provided number is prime"""
    if num == 1:
        return False # number 1 is excluded, as it is a unit
    if num % 2 == 0:
        return False # check if the number is even
    for i in range(3,n-1,2):
        if num % i == 0:
            return False
    return True

def check_primes_v2(num):
    """ Improved Algorithm for finding if a number is prime"""

import time

tStart = time.time()
for n in range(5, 100000):
    print(f"{n}: {check_primes_v1(n)}")


tFin = time.time()
print(tFin - tStart)

