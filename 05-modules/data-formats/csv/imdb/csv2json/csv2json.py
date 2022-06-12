import json
import re
import sys
import csv

result = []
with open(sys.argv[1], 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        result.append(json.dumps(row))
print(result)