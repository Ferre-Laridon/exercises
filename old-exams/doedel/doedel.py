import csv
from collections import Counter


counts = Counter()

with open('input.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        # count the number of times yes appears in all columns but the first one
        for key in row.keys():
            if key != 'name' and row[key] == 'yes':
                counts[key] += 1
    
# print results sorted by the number of times yes appears in each column
sorted_by_date = sorted(counts.items(), key=lambda x: x[1], reverse=True)

with open('output.txt', 'w') as f:
    for key, value in sorted_by_date:
        f.write(f'{key} {value}\n')