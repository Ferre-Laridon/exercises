from datetime import datetime
import json
from statistics import mean


with open('input.txt') as file:
    data = [ (datetime.strptime(date, '%d/%m/%Y'), temps) for date, temps in json.load(file).items() ]

with open('output.txt', 'w') as f:
    for _, temps in sorted(data, key=lambda p: p[0]):
        f.write(str(round(mean(temps))) + '\n')
