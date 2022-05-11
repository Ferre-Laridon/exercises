import json
import sys
import csv


data = list(csv.DictReader(sys.stdin))
print(json.dumps(data))