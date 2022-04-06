# Write your code here
from doctest import FAIL_FAST


def is_prime(n):
    return n>1 and all(n%i!=0 for i in range(2, n))