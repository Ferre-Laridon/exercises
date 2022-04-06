# Write your code here
def nth_longest_string(n, strings):
    return sorted(strings, key=lambda s: len(s))[-n]