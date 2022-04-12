# Write your code here
import re


def remove_repeated_words(string):
    return re.sub(r'([A-Za-z]+)( \1)+', r'\1', string)