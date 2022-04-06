# Write your code here
def slug(name):
    deel = name.split(' ')
    fname = deel[0]
    lname = deel[1:]
    return '-'.join(s.lower() for s in lname + [fname])