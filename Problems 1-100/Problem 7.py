# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#
# What is the 10 001st prime number?

from sympy import sieve
import sys

a = [i for i in sieve.primerange(1, 1000000)]
try:
    print('the 10001st prime number is', a[10000])
except IndexError:
    print(sys.exc_info()[:2])


