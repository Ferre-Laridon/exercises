# Write your code here
def remove_duplicates(xs):
    result = []
    found = set()
    for x in xs:
        if x not in found:
            result.append(x)
            found.add(x)
    return result