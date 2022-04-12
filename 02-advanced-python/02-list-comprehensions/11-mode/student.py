# Write your code here
from multiprocessing.sharedctypes import Value


def hoeveelheid(ns):
    result = {}
    for n in ns:
        if n not in result:
            result[n] = 0
        result[n] += 1
    return result


def mode(ns):
    hh = hoeveelheid(ns)
    return max(hh.items(), key=lambda pair: pair[1])[0]
