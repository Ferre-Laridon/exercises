with open('input.txt') as f:
    with open('output.txt', 'w') as output:
        for line in f:
            name, data = line.split(':')
            fraction, tekens = data.split(' ')
            ingewisseld, verdiend = map(int, fraction.split('/'))

            ingewisseld += tekens.count('-')
            verdiend += tekens.count('+')
            
            output.write(f"{name}:{ingewisseld}/{verdiend}\n")