output = ""
for i in range(10001):
    # calculate decimal, binary and hexadecimal values
    dec = str(i)
    binair = str(bin(i))
    hexa = str(hex(i))

    # make row
    output += dec.rjust(10) + \
        binair.rjust(20) + hexa.rjust(10) + '\n'

with open('output.txt', 'w') as f:
    f.write(output)