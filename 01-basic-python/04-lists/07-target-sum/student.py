# Write your code here
from operator import truediv


def target_sum(xs, target):
    for x in xs:
        for y in xs:
            if x+y==target: 
                return True
    return False