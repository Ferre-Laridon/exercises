# Write your code here
from ntpath import join
import string
from tokenize import String


def countdown(n):
    return ', '.join(str(i) for i in range(n, 0, -1))